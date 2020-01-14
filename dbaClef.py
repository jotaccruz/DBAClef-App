#pyinstaller --windowed --onefile --icon=DBAClef.ico dbaClef.py
#pyinstaller --windowed --onefile --add-binary "dbaClef.png;files" --i DBAClef.ico dbaClef.py
#conda install -c anaconda beautifulsoup4 

"""
Python 3.7.4
Created on Fri Nov  8 10:57:06 2019
A program that helps DBA to apply best practice to SQL Server:
    
@author: juan.cruz2

User can:
    List Current status
    Search an specific configuration
    Set an specific configuration
    Some utilities
    Close
"""

#import backend
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import dbaClefSource
from dbaClefSource import *
import dbaClefOS
from dbaClefOS import *
import wmi
from wmi import *
import dbaClefWeb
from dbaClefWeb import *
import PIL
from PIL import Image,ImageTk
import webbrowser

window=Tk()

#Funtions----------------------------------------------------------------------
#------------------------------------------------------------------------------
#---
def getRbselected(mode):
    if (mode == 0):
        #view_command()
    #else:
        cleanall(InventoryTree)
        cleanall(StatusTree1)
        cleanall(StatusTree2)
        cleanall(StatusTree3)
        cleanall(StatusTree4)
        cleanall(serverNbTab1Tree1)
        cleanall(serverNbTab1Tree2)
        cleanall(serverNbTab2Tree1)
        cleanall(serverNbTab3Tree1)
        cleanall(serverNbTab4Tree1)
        cleanall(serverNbTab5Tree1)
        cleanall(serverNbTab5Tree2)
        cleanall(serverNbTab5Tree3)
        cleanall(serverNbTab6Tree1)
        cleanall(serverNbTab6Tree2)
        cleanall(serverNbTab6Tree3)
        cleanall(serverNbTab6Tree4)
        cleanall(serverNbTab6Tree5)
        cleanall(serverNbTab6Tree6)
        cleanall(serverNbTab6Tree7)
        cleanall(serverNbTab6Tree8)
        cleanall(serverNbTab7Tree1)
        cleanall(serverNbTab7Tree2)
        cleanall(serverNbTab7Tree3)
        cleanall(serverNbTab8Tree1)
        cleanall(serverNbTab9Tree1)
        cleanall(serverNbTab9Tree2)
        cleanall(serverNbTab9Tree3)
        cleanall(serverNbTab10Tree1)

#---
def cleanall(widget):
    for i in widget.get_children():
        widget.delete(i)

#---

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def About():
    tkinter.messagebox.showinfo(title="dbaClef", message="Telus International - dbaClef v 1.0",)

def hello():
    webbrowser.open("https://docs.google.com/document/d/17QOtcPCKPlMlFKxTCVttlI-f-g5WccGF")
    # create a canvas
    #m1 = PanedWindow(window)
    #m1.grid(row=0, column=0)

    #left = Label(m1, text="left ane")
    #m1.grid(row=0, column=0)
    
    #m2 = PanedWindow(m1, orient=VERTICAL)
    #m1.add(m2)
    
    #top = Label(m2, text="top pane")
    #m2.add(top)
    
    #bottom = Label(m2, text="bottom pane")
    #m2.add(bottom)


def set_inventory():
    tkinter.messagebox.askquestion(title="dbaClef", message="Telus International - dbaClef v 1.0",)

#---
def basic_analyze_command():
    return

#---
def view_command():
    for i in InventoryTree.get_children():
        InventoryTree.delete(i)
    
    query="SELECT srv_name as SERVER, 'GLOBALSOLARWINDS' as INSTANCE, srv_ip as IP,"+\
            "'1433' as PORT, srv_user as USER, SRV_PWD as PWD, srv_os as OS"+\
            " FROM lgm_servers WHERE"+\
            " srv_name in"+\
            " ('SCAEDYAK02','SUSWEYAK05');"
    #print (query)
    #query="SELECT srv_name as SERVER, srv_ip as IP, srv_os as OS,"\
    #       "srv_type as ENGINE, srv_location as LOCATION, srv_domain "\
    #        "as DOMAIN FROM lgm_servers WHERE"+ \
    #        " srv_location = 'GCP' and srv_active=1 and srv_name in"+\
    #        " ('SUSWEYAK03','SUSWEYAK05');"
    mysqlserver=ip.get()
    mysqlusername=user.get()
    mysqlpsw=pas.get()
    for row in dbservers(query,mysqlserver,mysqlusername,mysqlpsw):
        InventoryTree.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]),tags = ('color'))
    InventoryTree.tag_configure('color', background='#aba9f8')

#---
def get_selected_command(event):
    return

#---
def get_detail_command(mode):

    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Instance": e2.get(),
                "User": "test",
                "Pwd": ""
                }
        wmiuser=''
        wmipass=''
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            
            #WMI Authentication
            wmiuser = simpledialog.askstring("WMI Credential", "Username (ti\\username)", parent=window)
            wmipass = simpledialog.askstring("WMI Credential", "Password:", show='*', parent=window)
        except IndexError:
            pass

#Tab Status
#Last startup
    sqlexec1="SELECT\
    CAST(create_date AS VARCHAR(100)) as Last_Startup,\
    CAST(DATEDIFF(hh,create_date,getdate())/24. as numeric (23,2)) AS days_uptime\
    FROM    sys.databases\
    WHERE   database_id = 2;"
    for i in StatusTree1.get_children():
        StatusTree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1):
        StatusTree1.insert("", END, values=(row[0],row[1]))
        
#CPUs
    sqlexec1="DECLARE @StringToExecute NVARCHAR(4000);\
    CREATE TABLE #test (cpu_count int,physical_memory_GB int,sql_memory_GB numeric(5,2));\
    IF EXISTS ( SELECT  *\
	FROM sys.all_objects o\
    INNER JOIN sys.all_columns c ON o.object_id = c.object_id\
    WHERE   o.name = 'dm_os_sys_info'\
    AND c.name = 'physical_memory_kb' )\
	BEGIN\
    SET @StringToExecute = '\
    SELECT\
    cpu_count,\
    CAST(ROUND((physical_memory_kb / 1024.0 / 1024), 1) AS INT) as physical_memory_GB,\
	CAST((CONVERT(int,value_in_use)/1024.0) as numeric(5,2)) as SQLMEM\
    FROM sys.dm_os_sys_info\
	CROSS APPLY sys.configurations\
	WHERE [name] =''max server memory (MB)''';\
	END\
    ELSE IF EXISTS ( SELECT  *\
    FROM    sys.all_objects o\
    INNER JOIN sys.all_columns c ON o.object_id = c.object_id\
    WHERE o.name = 'dm_os_sys_info'\
    AND c.name = 'physical_memory_in_bytes' )\
    BEGIN\
    SET @StringToExecute = '\
    SELECT\
    cpu_count,\
    CAST(ROUND((physical_memory_in_bytes / 1024.0 / 1024.0 / 1024.0 ), 1) AS INT) as physical_memory_GB,\
	CAST((CONVERT(int,value_in_use)/1024.0) as numeric(5,2)) as SQLMEM\
    FROM sys.dm_os_sys_info\
	CROSS APPLY sys.configurations\
	WHERE [name] =''max server memory (MB)''';\
    END\
    INSERT INTO #test\
    EXECUTE(@StringToExecute);"

    sqlexec3="SELECT cpu_count ,physical_memory_GB,sql_memory_GB FROM #test;"
    
    for i in StatusTree2.get_children():
        StatusTree2.delete(i)
        
    for row in mssqldetail2sql(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec3):
        StatusTree2.insert("", END, values=(row[0],row[1],row[2]))

#Version
    sqlexec1="IF EXISTS (SELECT * FROM sys.dm_os_performance_counters)\
    SELECT\
	TOP 1 CAST(SERVERPROPERTY('ProductVersion') AS NVARCHAR(100)) as ProductVersion,\
	CAST(SERVERPROPERTY('ProductLevel') AS NVARCHAR(100)) as PatchLevel,\
	CAST(SERVERPROPERTY('Edition') AS VARCHAR(100)) as Edition,\
	CASE WHEN (CAST(SERVERPROPERTY('IsClustered') AS VARCHAR(100))=0) THEN 'NOT' ELSE 'YES' END as IsClustered,\
	CASE WHEN (CAST(COALESCE(SERVERPROPERTY('IsHadrEnabled'),0) AS VARCHAR(100))=1) THEN 'YES' ELSE 'NOT' END as AlwaysOnEnabled,\
	'' AS Warning\
	FROM sys.dm_os_performance_counters;\
    ELSE\
	SELECT\
    TOP 1 CAST(SERVERPROPERTY('ProductVersion') AS NVARCHAR(100)) as ProductVersion,\
	CAST(SERVERPROPERTY('ProductLevel') AS NVARCHAR(100)) as PatchLevel,\
	CAST(SERVERPROPERTY('Edition') AS VARCHAR(100)) as Edition,\
	CASE WHEN (CAST(SERVERPROPERTY('IsClustered') AS VARCHAR(100))=0) THEN 'NOT' ELSE 'YES' END as IsClustered,\
	CASE WHEN (CAST(COALESCE(SERVERPROPERTY('IsHadrEnabled'),0) AS VARCHAR(100))=1) THEN 'YES' ELSE 'NOT' END as AlwaysOnEnabled,\
	'WARNING - No records found in sys.dm_os_performance_counters' AS Warning;"
    for i in StatusTree3.get_children():
        StatusTree3.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1):
        StatusTree3.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))

#Missing updates
    
    sqlexec1="DECLARE @ProductVersion VARCHAR(100)\
    SELECT @ProductVersion = CAST(SERVERPROPERTY('productversion') AS varchar(100))\
    DECLARE @Major VARCHAR(100)\
    DECLARE @Minor VARCHAR(100)\
    SELECT @Minor = PARSENAME(@ProductVersion, 1)\
    SELECT @Major = PARSENAME(@ProductVersion, 4)\
    SELECT\
    CASE WHEN @Major IS NULL THEN @ProductVersion ELSE LEFT(@ProductVersion,LEN(@ProductVersion)-CHARINDEX('.',REVERSE(@ProductVersion))) END AS VERSION;"
    
    for i in StatusTree4.get_children():
        StatusTree4.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1):
        version = mssqlversioncomplete(row[0])
        #version = mssqlversioncomplete("12.0.6259")
        #print (version)
    for dic in version:
        list=[]
        if 'Version' in dic:
            list.append(dic['Version'])
            
        if 'SupportedUntil' in dic:
            list.append(dic['SupportedUntil'])
        else:
            list.append('')
            
        if 'Name' in dic:
            list.append(dic['Name'])
        else:
            list.append('')
            
        if 'SP' in dic:
            list.append(dic['SP'])
        else:
            list.append('')
            
        if 'CU' in dic:
            list.append(dic['CU'])
        else:
            list.append('')
            
        if 'KBList' in dic:
            list.append(dic['KBList'])
        else:
            list.append('')
            
        StatusTree4.insert("",END,values=(list),tags = ('need'))
        StatusTree4.tag_configure('need', background='#f86d7e')

#Tab Services----------------------------------------------------------
#------------------------------------------------------------------------------

#Hostname
    sqlexec="SELECT CONVERT(nvarchar(250),@@servername) AS 'ServerName\InstanceName',CONVERT(nvarchar(250),SERVERPROPERTY('servername')) AS 'ServerName',CONVERT(nvarchar(250),SERVERPROPERTY('machinename')) AS 'Windows_Name',CONVERT(nvarchar(250),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')) AS 'NetBIOS_Name',CONVERT(nvarchar(250),ISNULL(SERVERPROPERTY('instanceName'),'DEFAULT')) AS 'InstanceName',CONVERT(nvarchar(250),SERVERPROPERTY('IsClustered')) AS 'IsClustered'"

    for i in serverNbTab1Tree1.get_children():
        serverNbTab1Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[1]!=row[2]):
            serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],),tags = ('need'))
        else:
            serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],),tags = ('good'))
    serverNbTab1Tree1.tag_configure('need', background='#f86d7e')

#Services
    for i in serverNbTab1Tree2.get_children():
        serverNbTab1Tree2.delete(i)
        
    for row in mssqlinfo(mode, selected_row['Server'], wmiuser, wmipass):
        if (row['State'] == "Stopped"):
            serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('need',))
        else:
            serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('good',))

    serverNbTab1Tree2.tag_configure('need', background='#f86d7e')    
    
#Tab Disks---------------------------------------------------------------------
#------------------------------------------------------------------------------

    for i in serverNbTab2Tree1.get_children():
        serverNbTab2Tree1.delete(i)
        
    for row in diskinfo(mode, selected_row['Server'], wmiuser, wmipass):
        if (row['DriveType'] == 3):
            if (row['BlockSize'] != 65536 and row['DriveLetter'] != "C:"):
                serverNbTab2Tree1.insert("", END, values=(row['SystemName'],\
                                                          row['Name'],\
                                                          row['DriveLetter'],\
                                                          row['FileSystem'],\
                                                          row['Label'],\
                                                          row['Capacity'],\
                                                          row['FreeSpace'],\
                                                          row['BlockSize'],\
                                                          "64"),\
            tags = ('need',))
            else:
                serverNbTab2Tree1.insert("", END, values=(row['SystemName'],\
                                                          row['Name'],\
                                                          row['DriveLetter'],\
                                                          row['FileSystem'],\
                                                          row['Label'],\
                                                          row['Capacity'],\
                                                          row['FreeSpace'],\
                                                          row['BlockSize'],\
                                                          ""),\
            tags = ('good',))

    serverNbTab2Tree1.tag_configure('need', background='#f5e45e')

#Tab Page File-----------------------------------------------------------------
#------------------------------------------------------------------------------
    
    for i in serverNbTab3Tree1.get_children():
        serverNbTab3Tree1.delete(i)
        
    for row in pageinfo(mode, selected_row['Server'], wmiuser, wmipass):
        serverNbTab3Tree1.insert("", END, values=(row['SystemName'],\
                                                      row['Automatic'],\
                                                      row['Caption'],\
                                                      row['Status'],\
                                                      row['CurrentUsage'],\
                                                      row['PeakUsage'],\
                                                      row['InitialSize'],\
                                                      row['MaximumSize']),\
        tags = ('good',))

    serverNbTab3Tree1.tag_configure('need', background='#f86d7e')

#Tab Default Paths-------------------------------------------------------------
#------------------------------------------------------------------------------
    sqlexec="USE master;\
    IF EXISTS (\
    SELECT * \
    FROM INFORMATION_SCHEMA.ROUTINES \
    WHERE SPECIFIC_SCHEMA = N'dbo'\
    AND SPECIFIC_NAME = N'get_defaultpathdb' \
    )\
    DROP PROCEDURE dbo.get_defaultpathdb;"
    sqlexec0="CREATE PROCEDURE dbo.get_defaultpathdb\
	@p1 int = 0, \
	@p2 int = 0\
    AS\
    BEGIN\
	INSERT INTO #RDPaths\
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultData';\
	INSERT INTO #DPaths(Type,Location)\
	VALUES('DefaultData',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')))-1));\
	INSERT INTO #RDPaths\
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultLog';\
	INSERT INTO #DPaths(Type,Location)\
	VALUES('DefaultLog',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')))-1));\
	INSERT INTO #RDPaths\
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'BackupDirectory';\
	INSERT INTO #DPaths(Type,Location)\
	VALUES('Error',SERVERPROPERTY('ErrorLogFileName'));\
	DECLARE @Bandera int = 0\
	DECLARE @Location nvarchar(250) = ''\
	SELECT @Bandera=1,@Location=CONCAT(CONVERT(NVARCHAR(250),a.Location),'-->',CONVERT(NVARCHAR(250),b.Location))\
	FROM #RDPaths a CROSS JOIN #DPaths b\
	WHERE a.Type='DefaultData'\
	AND a.Type=b.Type\
	AND a.Location<>b.Location\
	IF @Bandera=1\
	BEGIN\
	BEGIN TRAN\
	UPDATE #DPaths SET Location=@Location,Restart=1 WHERE Type='DefaultData'\
	COMMIT\
	END\
	SELECT @Bandera=0\
	SELECT @Location=''\
	SELECT @Bandera=1,@Location=CONCAT(CONVERT(NVARCHAR(250),a.Location),'-->',CONVERT(NVARCHAR(250),b.Location))\
	FROM #RDPaths a CROSS JOIN #DPaths b\
	WHERE a.Type='DefaultLog'\
	AND a.Type=b.Type\
	AND a.Location<>b.Location\
	IF @Bandera=1\
	UPDATE #DPaths SET Location=@Location,Restart=1 WHERE Type='DefaultLog'\
    END;COMMIT;"
    mssqlexec(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    mssqlexec(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec0)

    sqlexec1="CREATE TABLE #DPaths(Type nvarchar(50),Location sql_variant, \
    Restart integer);CREATE TABLE #RDPaths(Type nvarchar(50),\
        Location sql_variant);EXECUTE master.dbo.get_defaultpathdb;"
        
    sqlexec2="CREATE TABLE #DPath(Type nvarchar(50),Location nvarchar(250),\
    Restart integer);INSERT INTO #DPath(Type,Location,Restart) SELECT Type,\
        CONVERT(NVARCHAR(250),Location),Restart FROM #DPaths;INSERT INTO \
        #DPath(Type,Location) SELECT Type,CONVERT(NVARCHAR(250),Location) \
        FROM #RDPaths WHERE Type='BackupDirectory';"
        
    sqlexec3="SELECT Type, Location, Restart, CASE WHEN (ISNULL(Restart,0)=1)\
    THEN 'Required' ELSE 'No' END AS Restart FROM #DPath;"

    for i in serverNbTab4Tree1.get_children():
        serverNbTab4Tree1.delete(i)
        
    for row in mssqldetailsp(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (row[2]==1):
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('need',))
        else:
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('good',))
    
    mssqlexec(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    serverNbTab4Tree1.tag_configure('need', background='#f86d7e')

#Alerts Tab--------------------------------------------------------------------
#------------------------------------------------------------------------------

#Operator
    sqlexec="SELECT name,email_address,CASE WHEN enabled=0 THEN 'No' ELSE \
    'Yes' END AS Enabled,CASE WHEN pager_days=0 THEN 'All' ELSE 'Some days' \
    END AS Notifications FROM msdb.dbo.sysoperators WHERE enabled = 1"

    for i in serverNbTab5Tree1.get_children():
        serverNbTab5Tree1.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree1.insert("", END, values=(row[0],row[1],row[2],row[3]))
        rows=1
    
    if rows==0:
        serverNbTab5Tree1.insert("", END, values=("Missing","","","",),tags = ('need'))
    
    serverNbTab5Tree1.tag_configure('need', background='#f86d7e')
    
#Alerts
    sqlexec="SELECT id,name,severity,CASE WHEN enabled=0 THEN 'No' ELSE 'Yes'\
    END AS Enabled FROM msdb.dbo.sysalerts"
    
    for i in serverNbTab5Tree3.get_children():
        serverNbTab5Tree3.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree3.insert("", END, values=(row[1],row[2],row[3]))
        rows=1
    
    if rows==0:
        serverNbTab5Tree3.insert("", END, values=("Missing","","",),tags = ('need'))
    
    serverNbTab5Tree3.tag_configure('need', background='#f86d7e')
    
#Failsafe Operator
    sqlexec1="CREATE TABLE #AlertInfo (FailSafeOperator NVARCHAR(255),\
    NotificationMethod INT,ForwardingServer NVARCHAR(255),ForwardingSeverity \
    INT,PagerToTemplate NVARCHAR(255),PagerCCTemplate NVARCHAR(255),\
    PagerSubjectTemplate NVARCHAR(255),PagerSendSubjectOnly NVARCHAR(255),\
    ForwardAlways INT);"
        
    sqlexec2="INSERT  INTO #AlertInfo EXEC [master].[dbo].[sp_MSgetalertinfo] \
    @includeaddresses = 0;"
        
    sqlexec3="SELECT ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),\
    'No Fail safe Operator')) AS \
    FailSafeOperator, CASE WHEN ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),'No Fail safe Operator'))='No Fail safe Operator' \
    THEN '1' ELSE '0' END as Semaphore FROM #AlertInfo;"

    for rows in serverNbTab5Tree2.get_children():
        serverNbTab5Tree2.delete(rows)
        
    for rows in mssqldetailsp(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (rows[1]=='1'):
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('need'))
        else:
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('good'))
    
    serverNbTab5Tree2.tag_configure('need', background='#f86d7e')

#DBMail Tab--------------------------------------------------------------------
#------------------------------------------------------------------------------

#SQL Server Agent enabled  
    sqlexec="SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled' ELSE 'Enabled' END AS SQLAgentEnabled FROM sys.configurations WHERE [name] ='Agent XPs';"

    for i in serverNbTab6Tree1.get_children():
        serverNbTab6Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree1.insert("", END, values=(row[0]), tags = ('need'))
        else:
            serverNbTab6Tree1.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree1.tag_configure('need', background='#f86d7e')
                                    
#SQL Server Agent status
    sqlexec="IF (SELECT CAST(SERVERPROPERTY('Edition') AS VARCHAR(30))) NOT LIKE 'Express Edition%' BEGIN SELECT CASE WHEN status_desc = 'Running' THEN 'Running' ELSE 'Stopped' END AS SQLAgentStarted FROM sys.dm_server_services WHERE servicename LIKE 'SQL Server Agent%' END ELSE BEGIN SELECT 'Express Edition' SQLAgentStarted END;"

    for i in serverNbTab6Tree2.get_children():
        serverNbTab6Tree2.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Running'):
            serverNbTab6Tree2.insert("", END, values=(row[0]), tags = ('good'))
        else:
            serverNbTab6Tree2.insert("", END, values=(row[0]), tags = ('need'))
    
    serverNbTab6Tree2.tag_configure('need', background='#f86d7e')

#SQL Database Mail is enabled
    sqlexec="SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled' ELSE 'Enabled' END AS DBMailEnabled  FROM sys.configurations WHERE [name] ='Database Mail XPs';"

    for i in serverNbTab6Tree3.get_children():
        serverNbTab6Tree3.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree3.insert("", END, values=(row[0]), tags = ('need'))
        else:
            serverNbTab6Tree3.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree3.tag_configure('need', background='#f86d7e')

#@SQL Agent Mail Enabled     
    sqlexec="SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled FROM msdb.dbo.sysmail_profile;"

    for i in serverNbTab6Tree4.get_children():
        serverNbTab6Tree4.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree4.insert("", END, values=(row[0]), tags = ('need'))
        else:
            serverNbTab6Tree4.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree4.tag_configure('need', background='#f86d7e')

#Mail Account Enabled
    sqlexec="SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS MailAccountEnabled FROM msdb.dbo.sysmail_account;"

    for i in serverNbTab6Tree5.get_children():
        serverNbTab6Tree5.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree5.insert("", END, values=(row[0]), tags = ('need'))
        else:
            serverNbTab6Tree5.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree5.tag_configure('need', background='#f86d7e')

#SQL Server Agent is enabled to use Database Mail
    sqlexec1="CREATE TABLE #SQLAgentMailEnabled (SQLAgentMailEnabled nvarchar(15),Datos INT);"
    
    sqlexec2="INSERT INTO #SQLAgentMailEnabled EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent', N'UseDatabaseMail';"
    
    sqlexec3="IF EXISTS (SELECT SQLAgentMailEnabled FROM #SQLAgentMailEnabled) BEGIN SELECT CASE WHEN Datos=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled FROM #SQLAgentMailEnabled END ELSE BEGIN SELECT 'Express Edition' AS SQLAgentMailEnabled END;"
    
    for i in serverNbTab6Tree6.get_children():
        serverNbTab6Tree6.delete(i)
        
    for row in mssqldetailsp(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (row[0]=='Enabled'):
            serverNbTab6Tree6.insert("", END, values=(row[0]), tags = ('good'))
        else:
            serverNbTab6Tree6.insert("", END, values=(row[0]), tags = ('need'))
    
    serverNbTab6Tree6.tag_configure('need', background='#f86d7e')

#SQL Server Agent is enabled to use Database Mail and Mail Profile is assigned
    sqlexec1="CREATE TABLE #SQLAgentMailProfileEnabled (SQLAgentMailProfileEnabled nvarchar(20),dat sysname);"
    
    sqlexec2="INSERT INTO #SQLAgentMailProfileEnabled EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',N'DatabaseMailProfile';"
    
    sqlexec3="IF EXISTS (SELECT SQLAgentMailProfileEnabled FROM #SQLAgentMailProfileEnabled) BEGIN SELECT CASE WHEN COUNT(SQLAgentMailProfileEnabled)=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailProfileEnabled FROM #SQLAgentMailProfileEnabled END ELSE BEGIN SELECT 'Express Edition' SQLAgentMailProfileEnabled END;"

    for i in serverNbTab6Tree7.get_children():
        serverNbTab6Tree7.delete(i)
        
    for row in mssqldetailsp(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (row[0]=='Enabled'):
            serverNbTab6Tree7.insert("", END, values=(row[0]), tags = ('good'))
        else:
            serverNbTab6Tree7.insert("", END, values=(row[0]), tags = ('need'))
    
    serverNbTab6Tree7.tag_configure('need', background='#f86d7e')

#get email retry interval configuration value
    sqlexec="SELECT paramvalue as retry_sec FROM msdb.dbo.sysmail_configuration WHERE paramname = 'AccountRetryDelay';"

    for i in serverNbTab6Tree8.get_children():
        serverNbTab6Tree8.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree8.insert("", END, values=(row[0],),tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab6Tree8.insert("", END, values=("","Missing",),tags = ('need'))
    
    serverNbTab6Tree8.tag_configure('need', background='#f86d7e')

#General Check
#--PENDING CONFIGURATIONS.
    sqlexec="SELECT name NAME, description AS DESCR, CONVERT(nvarchar(100),value) AS VALUE, CONVERT(nvarchar(100),value_in_use) AS VALUEINUSE FROM sys.configurations where value <> value_in_use;"

    for i in serverNbTab7Tree1.get_children():
        serverNbTab7Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab7Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],),tags = ('need'))
    serverNbTab7Tree1.tag_configure('need', background='#f86d7e')

#--REMOTE ADMIN
#--BACKUP COMPRESSION
#--AD HOC
#--MAXDOP

    sqlexec="SELECT name AS [NAME], description AS [DESC], CASE WHEN (value_in_use=0) THEN 'OFF' ELSE 'ON' END AS [STATUS] FROM sys.configurations WHERE name IN (N'remote admin connections',N'backup compression default','optimize for ad hoc workloads') UNION SELECT name AS [NAME], description AS [DESC], CASE value_in_use WHEN 0 THEN 'AUTO' WHEN 1 THEN 'OFF' ELSE CONVERT(nvarchar(100),value_in_use) END AS [STATUS] FROM sys.configurations WHERE name IN (N'max degree of parallelism');"

    for i in serverNbTab7Tree2.get_children():
        serverNbTab7Tree2.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[2]=='OFF'):
            serverNbTab7Tree2.insert("", END, values=(row[0],row[1],row[2],),tags = ('need'))
        else:
            serverNbTab7Tree2.insert("", END, values=(row[0],row[1],row[2],),tags = ('good'))
    serverNbTab7Tree2.tag_configure('need', background='#f5e45e')

#--IFI STATUS
    sqlexec1="IF OBJECT_ID('tempdb..#IFI') IS NOT NULL DROP TABLE #IFI; CREATE TABLE #IFI (LogDate datetime, ProcessInfo nvarchar(250), Text nvarchar(500));"
        
    sqlexec2="INSERT INTO #IFI EXEC sys.xp_readerrorlog 0, 1, N'Database Instant File Initialization';"
        
    sqlexec3="SELECT CASE WHEN (CHARINDEX( 'disabled',Text))=0 THEN 'Enabled' ELSE RIGHT(LEFT(Text,CHARINDEX( 'disabled',Text)+7),8) END AS [IFI-STATUS] FROM #IFI"

    for i in serverNbTab7Tree3.get_children():
        serverNbTab7Tree3.delete(i)
        
    for rows in mssqldetailsp(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (rows[0]=='disabled'):
            serverNbTab7Tree3.insert("", END, values=(rows[0], ),tags = ('need'))
        else:
            serverNbTab7Tree3.insert("", END, values=(rows[0], ),tags = ('good'))
   
    serverNbTab7Tree3.tag_configure('need', background='#f86d7e')

#Databases
#--DATABASES
    sqlexec="SELECT database_id ID,name NAME,isnull(suser_sname(owner_sid),'~~UNKNOWN~~') OWNER,convert(nvarchar(11), create_date) CREATION,compatibility_level COMPATIBILITY,state_desc STATUS,recovery_model_desc RECOVERY,page_verify_option_desc VERIFICATION,log_reuse_wait_desc LRWAIT FROM master.sys.databases WHERE name NOT IN ('DBAdmin') ORDER BY create_date ASC;"

    for i in serverNbTab8Tree1.get_children():
        serverNbTab8Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[2]!='sa'):
            serverNbTab8Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],),tags = ('need'))
        else:
            serverNbTab8Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],),tags = ('good'))
            
    serverNbTab8Tree1.tag_configure('need', background='#f86d7e')

#Logins
#--Sysadmin Logins
    sqlexec="SELECT name NAME, type_desc TYPE, CASE WHEN is_disabled = 0 THEN 'ENABLED' ELSE 'DISABLED' END STATUS, convert(nvarchar(11), create_date) CREATION, default_database_name DB FROM master.sys.server_principals WHERE    IS_SRVROLEMEMBER ('sysadmin',name) = 1 ORDER BY is_disabled ASC,type_desc ASC, create_date ASC;"

    for i in serverNbTab10Tree1.get_children():
        serverNbTab10Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='BUILTIN\\Users' or row[0]=='NT AUTHORITY\\SYSTEM'):
            serverNbTab10Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('need'))
        else:
            serverNbTab10Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('good'))
            
    serverNbTab10Tree1.tag_configure('need', background='#f86d7e')

#DBA Tools
#--DBAdmin
    sqlexec="SELECT database_id ID,'DBAdmin' NAME,isnull(suser_sname(owner_sid),'~~UNKNOWN~~') OWNER,convert(nvarchar(11), create_date) CREATION,compatibility_level COMPATIBILITY,state_desc STATUS,recovery_model_desc RECOVERY,page_verify_option_desc VERIFICATION,log_reuse_wait_desc LRWAIT FROM master.sys.databases WHERE name IN ('DBAdmin');"

    for i in serverNbTab9Tree1.get_children():
        serverNbTab9Tree1.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[2]!='sa'):
            serverNbTab9Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],),tags = ('need'))
        else:
            serverNbTab9Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],),tags = ('good'))
        rows=1

    if rows==0:
        serverNbTab9Tree1.insert("", END, values=("","Missing","","","","","","","",),tags = ('need'))
    
    serverNbTab9Tree1.tag_configure('need', background='#f86d7e')

#--Service Restart Notification
    sqlexec="SELECT jo.name NAME,isnull(suser_sname(jo.owner_sid),'~~UNKNOWN~~') OWNER,CASE WHEN jo.enabled=1 THEN 'ENABLE' ELSE 'DISABLE' END AS STATUS,description DESCR FROM msdb.dbo.sysjobs jo CROSS APPLY msdb.dbo.sysjobschedules josc CROSS APPLY msdb.dbo.sysschedules sc WHERE jo.job_id=josc.job_id AND josc.schedule_id=sc.schedule_id AND (jo.name LIKE 'Service Restart Notification' OR sc.freq_type=64);"

    for i in serverNbTab9Tree2.get_children():
        serverNbTab9Tree2.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab9Tree2.insert("", END, values=(row[0],row[1],row[2],row[3],),tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab9Tree2.insert("", END, values=("Missing","","","",),tags = ('need'))
    
    serverNbTab9Tree2.tag_configure('need', background='#f86d7e')
            
#--sp_whoisactive
    sqlexec="IF EXISTS (SELECT * FROM sys.databases o WHERE o.name = 'DBAdmin') BEGIN SELECT name,info FROM DBAdmin.dbo.sysobjects WHERE name LIKE 'sp_whoisactive' END ELSE BEGIN SELECT 'Missing' name,'' info END;"

    for i in serverNbTab9Tree3.get_children():
        serverNbTab9Tree3.delete(i)
    
    for row in mssqldetail(selected_row['Server'],selected_row['Instance'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]!='Missing'):
            serverNbTab9Tree3.insert("", END, values=(row[0],row[1],),tags = ('good'))
        else:
            serverNbTab9Tree3.insert("", END, values=(row[0],row[1],),tags = ('need'))

    serverNbTab9Tree3.tag_configure('need', background='#f86d7e')


####### main ------------------------------------------------------------------
    
menubar = Menu(window)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="1 Server List", command=view_command)
filemenu.add_command(label="2 Default path", command=hello)
filemenu.add_command(label="3 DBAdmin", command=hello)
filemenu.add_command(label="4 DBMail", command=hello)
filemenu.add_command(label="5 Alerts", command=hello)
filemenu.add_command(label="6 sp_whoisactive", command=hello)
filemenu.add_command(label="7 ServerName", command=hello)
filemenu.add_command(label="8 Invetory", command=set_inventory)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label="Setup", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Basic", command= basic_analyze_command)
editmenu.add_command(label="Advance", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Analyze", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="WIN - SQL Server - Standard Setup", command=hello)
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
window.config(menu=menubar)
window.wm_title("dbaClef")

if getattr(sys, 'frozen', False): # Running as compiled
    running_dir = sys._MEIPASS + "/files/" # Same path name than pyinstaller option
else:
    running_dir = "./" # Path name when run with Python interpreter
iconFileName = running_dir + "dbaClef.png"
if os.path.isfile(iconFileName):
    photo = PhotoImage(file = iconFileName)
    #window.wm_iconbitmap(resource_path("dbaClef.ico"))
    window.iconphoto(False,photo)

#Frame Controls
inventoryframe = ttk.LabelFrame(window, width=250, height=200,text="Server")
inventoryframe.grid(row=0,column=0,padx=5, pady=5)

inventory2frame = ttk.LabelFrame(inventoryframe, width=250, height=200,text="")
inventory2frame.grid(row=0,column=0,padx=5, pady=5, rowspan=2)

inventory3frame = ttk.LabelFrame(inventoryframe, width=250, height=200,text="")
inventory3frame.grid(row=0,column=1,padx=5, pady=5, sticky='n')

statusframe = ttk.LabelFrame(window, width=525, height=192,text="Status")
statusframe.grid(row=0,column=1,padx=5, pady=5)

#RadioButton Controls
ConnMode = IntVar()
ConnMode.set(1)

Radiobutton(inventory2frame, text="Inventory", variable=ConnMode, value=0, command= lambda : getRbselected(ConnMode.get())).grid(row=0,column=0,padx=5, pady=5, sticky="W",columnspan=2)
Radiobutton(inventory3frame, text="Local", variable=ConnMode, value=1,command= lambda : getRbselected(ConnMode.get())).grid(row=0,column=0,padx=5, pady=5, sticky="W")

#Texts
labelip=ttk.Label(inventory2frame,text="Ip", wraplength=10)
labelip.grid(row=1,column=0,padx=5, pady=5, sticky='w')
ip_text=StringVar(value='172.25.20.17')
ip=ttk.Entry(inventory2frame,textvariable=ip_text,width=20)
ip.grid(row=1,column=1,padx=5, pady=5,sticky="w")

labelport=ttk.Label(inventory2frame,text="Port", wraplength=50)
labelport.grid(row=2,column=0,padx=5, pady=5, sticky='w')
port_text=StringVar(value='3306')
port=ttk.Entry(inventory2frame,textvariable=port_text,width=20)
port.grid(row=2,column=1,padx=5, pady=5,sticky="w")

labeluser=ttk.Label(inventory2frame,text="User", wraplength=50)
labeluser.grid(row=3,column=0,padx=5, pady=5, sticky='w')
user_text=StringVar()
user=ttk.Entry(inventory2frame,textvariable=user_text,width=20)
user.grid(row=3,column=1,padx=5, pady=5,sticky="w")

labelpass=ttk.Label(inventory2frame,text="Password", wraplength=50)
labelpass.grid(row=4,column=0,padx=5, pady=5, sticky='w')
pass_text=StringVar()
pas=ttk.Entry(inventory2frame,textvariable=pass_text,width=20,show='*')
pas.grid(row=4,column=1,padx=5, pady=5,sticky="w")


labelinstance=ttk.Label(inventory3frame,text="Instance", wraplength=50)
labelinstance.grid(row=1,column=0,padx=5, pady=5, sticky='w')
instance=StringVar()
e2=ttk.Entry(inventory3frame,textvariable=instance,width=20)
e2.grid(row=1,column=1,padx=5, pady=5,sticky="w")

#Bottoms
DetailButton = ttk.Button(inventoryframe, text='Connect', underline = 0, command= lambda: get_detail_command(ConnMode.get()))
DetailButton.grid(row=1, column=1, sticky="e", padx=5, pady=5,)

InventoryButton = ttk.Button(inventory2frame, text='Load', underline = 0, command= lambda: view_command())
InventoryButton.grid(row=0, column=1, sticky="e", padx=5, pady=5,)

#ScanButton = Button(inventoryframe, text='Scan', underline = 0, \
#                      command=get_detail_command)
#ScanButton.grid(row=2, column=2, sticky="s", padx=5, pady=5)

#ExitButton = Button(inventoryframe, text='Exit', underline = 0, \
#                      command=window.destroy)
#ExitButton.grid(row=3, column=2, sticky="s", padx=5, pady=5)

#TreeViews
InventoryTree=ttk.Treeview(inventoryframe,show='headings',height=3)
InventoryTree.grid(row=6,column=0,padx=5, pady=5,rowspan=6,columnspan=3)
InventoryTree['columns'] = ('Server', 'Instance', 'Ip', 'Port', 'User', 'Pwd','Os')
InventoryTree['displaycolumns'] = ('Server', 'Instance', 'Ip', 'Port', 'Os')
InventoryTree.column("Server", minwidth=0,width=85)
InventoryTree.heading("Server", text="SERVER",)
InventoryTree.column("Instance", minwidth=0,width=140)
InventoryTree.heading("Instance", text="INSTANCE",)
InventoryTree.column("Ip", minwidth=0,width=80)
InventoryTree.heading("Ip", text="IP",)
InventoryTree.column("Port", minwidth=0,width=40)
InventoryTree.heading("Port", text="PORT",)
InventoryTree.column("Os", minwidth=0,width=80)
InventoryTree.heading("Os", text="OS",)
InventoryTree.heading("User", text="USER")
InventoryTree.heading("Pwd", text="PWD")

#if (selected_mode == 1):
#    InventoryTree.state(('disabled',))
#else:
#    InventoryTree.state(('!disabled',))
    
InventoryTree.bind('<Double-Button-1>',lambda x: DetailButton.invoke())

#Img = Image.open("dbserver2.jpg")
#Image = ImageTk.PhotoImage(Img)

#dbSrvButton1 = ttk.Button(statusframe, image=Image)
#dbSrvButton1.grid(row=0,column=0,padx=5, pady=5,sticky="w")

#dbSrvButton2 = ttk.Button(statusframe, image=Image)
#dbSrvButton2.grid(row=0,column=1,padx=5, pady=5,sticky="w")

StatusTree1=ttk.Treeview(statusframe,show='headings',height=1)
StatusTree1.grid(row=0,column=0,padx=5, pady=5,rowspan=2,columnspan=2,sticky="w")
StatusTree1['columns'] = ('Last_Startup', 'days_uptime')
StatusTree1['displaycolumns'] = ('Last_Startup','days_uptime')
StatusTree1.column("Last_Startup", minwidth=0,width=120)
StatusTree1.heading("Last_Startup", text="LAST STARTUP",)
StatusTree1.column("days_uptime", minwidth=0,width=90)
StatusTree1.heading("days_uptime", text="DAYS UPTIME",)

StatusTree2=ttk.Treeview(statusframe,show='headings',height=1)
StatusTree2.grid(row=0,column=2,padx=5, pady=5,rowspan=2,columnspan=1,sticky="w")
StatusTree2['columns'] = ('cpu_count', 'physical_memory_GB','sql_memory_GB')
StatusTree2['displaycolumns'] = ('cpu_count', 'physical_memory_GB','sql_memory_GB')
StatusTree2.column("cpu_count", minwidth=0,width=40)
StatusTree2.heading("cpu_count", text="CPUs",)
StatusTree2.column("physical_memory_GB", minwidth=0,width=100)
StatusTree2.heading("physical_memory_GB", text="P MEMORY GB",)
StatusTree2.column("sql_memory_GB", minwidth=0,width=100)
StatusTree2.heading("sql_memory_GB", text="SQL MEMORY GB",)

StatusTree3=ttk.Treeview(statusframe,show='headings',height=1)
StatusTree3.grid(row=4,column=0,padx=5, pady=5,rowspan=2,columnspan=5,sticky="w")
StatusTree3['columns'] = ('ProductVersion', 'PatchLevel', 'Edition', 'IsClustered', 'AlwaysOnEnabled', 'Warning')
StatusTree3['displaycolumns'] = ('ProductVersion', 'PatchLevel', 'Edition', 'IsClustered', 'AlwaysOnEnabled', 'Warning')
StatusTree3.column("ProductVersion", minwidth=0,width=75)
StatusTree3.heading("ProductVersion", text="VERSION",)
StatusTree3.column("PatchLevel", minwidth=0,width=55)
StatusTree3.heading("PatchLevel", text="PATCH",)
StatusTree3.column("Edition", minwidth=0,width=150)
StatusTree3.heading("Edition", text="EDITION",)
StatusTree3.column("IsClustered", minwidth=0,width=60)
StatusTree3.heading("IsClustered", text="CLUSTER",)
StatusTree3.column("AlwaysOnEnabled", minwidth=0,width=75)
StatusTree3.heading("AlwaysOnEnabled", text="ALWAYS ON",)
StatusTree3.column("Warning", minwidth=0,width=100)
StatusTree3.heading("Warning", text="WARNING",)

StatusTree4=ttk.Treeview(statusframe,show='headings',height=3)
StatusTree4.grid(row=6,column=0,padx=5, pady=5,rowspan=2,columnspan=5,sticky="w")
StatusTree4['columns'] = ('Version', 'Eos', 'Name', 'Sp', 'Cu', 'KBList',)
StatusTree4['displaycolumns'] = ('Version', 'Eos', 'Name', 'Sp', 'Cu', 'KBList', )
StatusTree4.column("Version", minwidth=0,width=75)
StatusTree4.heading("Version", text="VERSION",)
StatusTree4.column("Eos", minwidth=0,width=70)
StatusTree4.heading("Eos", text="EOS",)
StatusTree4.column("Name", minwidth=0,width=70)
StatusTree4.heading("Name", text="NAME",)
StatusTree4.column("Sp", minwidth=0,width=50)
StatusTree4.heading("Sp", text="SP",)
StatusTree4.column("Cu", minwidth=0,width=45)
StatusTree4.heading("Cu", text="CU",)
StatusTree4.column("KBList", minwidth=0,width=60)
StatusTree4.heading("KBList", text="KBLIST",)

detailframe = ttk.LabelFrame(window, width=600, height=600, text="Detail")
detailframe.grid(row=2,column=0,padx=5, pady=5, columnspan=2, sticky="w")

serverNb=ttk.Notebook(detailframe)
serverNb.grid(row=0,column=0, sticky="e",padx=5, pady=5)

serverNbTab1=Frame(serverNb)
serverNbTab2=Frame(serverNb)
serverNbTab3=Frame(serverNb)
serverNbTab4=Frame(serverNb)
serverNbTab5=Frame(serverNb)
serverNbTab6=Frame(serverNb)
serverNbTab7=Frame(serverNb)
serverNbTab8=Frame(serverNb)
serverNbTab9=Frame(serverNb)
serverNbTab10=Frame(serverNb)

##Special Settings Tab
#Instance
serverNbTab1Tree1=ttk.Treeview(serverNbTab1,show='headings',height=1,)
serverNbTab1Tree1.grid(row=0,column=0,padx=5, pady=5,sticky="W")
serverNbTab1Tree1['columns'] = ('ServerInstance', 'ServerName', 'WindowsName', 'NetBiosName','InstanceName')
serverNbTab1Tree1.heading("ServerInstance", text="SERVER\INSTANCE")
serverNbTab1Tree1.column("ServerInstance", minwidth=0,width=225)
serverNbTab1Tree1.heading("ServerName", text="SERVERNAME")
serverNbTab1Tree1.column("ServerName", minwidth=0,width=200)
serverNbTab1Tree1.heading("WindowsName", text="WINDOWSNAME")
serverNbTab1Tree1.column("WindowsName", minwidth=0,width=150)
serverNbTab1Tree1.heading("NetBiosName", text="NETBIOSNAME")
serverNbTab1Tree1.column("NetBiosName", minwidth=0,width=100)
serverNbTab1Tree1.heading("InstanceName", text="INSTANCENAME")
serverNbTab1Tree1.column("InstanceName", minwidth=0,width=150)

#Services
serverNbTab1Tree2=ttk.Treeview(serverNbTab1,show='headings',height=9,)
serverNbTab1Tree2.grid(row=1,column=0,padx=5, pady=5, sticky='w')
serverNbTab1Tree2['columns'] = ('SystemName', 'DisplayName', 'Description', 'Started','StartMode','StartName','State','Status',)
serverNbTab1Tree2['displaycolumns'] = ('DisplayName', 'Description','StartMode','StartName','State',)
serverNbTab1Tree2.heading("SystemName", text="SERVER")
serverNbTab1Tree2.column("SystemName", minwidth=0,width=125)
serverNbTab1Tree2.heading("DisplayName", text="SERVICE")
serverNbTab1Tree2.column("DisplayName", minwidth=0,width=180)
serverNbTab1Tree2.heading("Description", text="DESC")
serverNbTab1Tree2.column("Description", minwidth=0,width=270)
serverNbTab1Tree2.heading("Started", text="STARTED")
serverNbTab1Tree2.column("Started", minwidth=0,width=50)
serverNbTab1Tree2.heading("StartMode", text="START")
serverNbTab1Tree2.column("StartMode", minwidth=0,width=60)
serverNbTab1Tree2.heading("StartName", text="ACCOUNT")
serverNbTab1Tree2.column("StartName", minwidth=0,width=250)
serverNbTab1Tree2.heading("State", text="STATE")
serverNbTab1Tree2.column("State", minwidth=0,width=60)
#serverNbTab1Tree2.heading("PathName", text="PATH")
#serverNbTab1Tree2.column("PathName", minwidth=0,width=180)

#Disks Tab
serverNbTab2Tree1=ttk.Treeview(serverNbTab2,show='headings',height=12,)
serverNbTab2Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab2Tree1['columns'] = ('SName', 'Name', 'DLetter','FSystem',
                 'Label', 'Capacity', 'FSpace', 'BSize','SUBSize')
serverNbTab2Tree1['displaycolumns'] = ('Name', 'DLetter','FSystem',
                 'Label', 'Capacity', 'FSpace', 'BSize','SUBSize')
serverNbTab2Tree1.heading("SName", text="SERVER")
serverNbTab2Tree1.column("SName", minwidth=0,width=150)
serverNbTab2Tree1.heading("Name", text="NAME")
serverNbTab2Tree1.column("Name", minwidth=0,width=50)
serverNbTab2Tree1.heading("DLetter", text="DLETTER")
serverNbTab2Tree1.column("DLetter", minwidth=0,width=75)
serverNbTab2Tree1.heading("FSystem", text="FSYSTEM")
serverNbTab2Tree1.column("FSystem", minwidth=0,width=75)
serverNbTab2Tree1.heading("Label", text="LABEL")
serverNbTab2Tree1.column("Label", minwidth=0,width=250)
serverNbTab2Tree1.heading("Capacity", text="CAPACITY GB")
serverNbTab2Tree1.column("Capacity", minwidth=0,width=100)
serverNbTab2Tree1.heading("FSpace", text="FSPACE GB")
serverNbTab2Tree1.column("FSpace", minwidth=0,width=75)
serverNbTab2Tree1.heading("BSize", text="BSIZE KB")
serverNbTab2Tree1.column("BSize", minwidth=0,width=75)
serverNbTab2Tree1.heading("SUBSize", text="SUBSIZE KB")
serverNbTab2Tree1.column("SUBSize", minwidth=0,width=75)

#Page File Tab
serverNbTab3Tree1=ttk.Treeview(serverNbTab3,show='headings',height=12,)
serverNbTab3Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab3Tree1['columns'] = ('SName', 'Automatic', 'Caption','Status',
                 'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximumSize')
serverNbTab3Tree1['displaycolumns'] = ('Automatic', 'Caption','Status'
                 ,'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximumSize')
serverNbTab3Tree1.heading("SName", text="SERVER")
serverNbTab3Tree1.column("SName", minwidth=0,width=150)
serverNbTab3Tree1.heading("Automatic", text="AUTO")
serverNbTab3Tree1.column("Automatic", minwidth=0,width=50)
serverNbTab3Tree1.heading("Caption", text="FNAME")
serverNbTab3Tree1.column("Caption", minwidth=0,width=250)
serverNbTab3Tree1.heading("Status", text="STATUS")
serverNbTab3Tree1.column("Status", minwidth=0,width=75)
serverNbTab3Tree1.heading("CurrentUsage", text="CUSAGE GB")
serverNbTab3Tree1.column("CurrentUsage", minwidth=0,width=150)
serverNbTab3Tree1.heading("PeakUsage", text="PUSAGE GB")
serverNbTab3Tree1.column("PeakUsage", minwidth=0,width=100)
serverNbTab3Tree1.heading("InitialSize", text="ISIZE GB")
serverNbTab3Tree1.column("InitialSize", minwidth=0,width=75)
serverNbTab3Tree1.heading("MaximumSize", text="MSIZE GB")
serverNbTab3Tree1.column("MaximumSize", minwidth=0,width=75)

#Defaulth Paths Tab
serverNbTab4Tree1=ttk.Treeview(serverNbTab4,show='headings',height=12,)
serverNbTab4Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab4Tree1['columns'] = ('Type', 'Location','Restart')
serverNbTab4Tree1['displaycolumns'] = ('Type', 'Location','Restart')
serverNbTab4Tree1.heading("Type", text="TYPE")
serverNbTab4Tree1.column("Type", minwidth=0,width=100)
serverNbTab4Tree1.heading("Location", text="LOCATION")
serverNbTab4Tree1.column("Location", minwidth=0,width=600)
serverNbTab4Tree1.heading("Restart", text="RESTART")
serverNbTab4Tree1.column("Restart", minwidth=0,width=75)

#Alerts Tab
#Operator
serverNbTab5Tree1=ttk.Treeview(serverNbTab5,show='headings',height=1, )
serverNbTab5Tree1.grid(row=0,column=0,padx=5, pady=5, )
serverNbTab5Tree1['columns'] = ('Name', 'Email','Enabled','Notification')
serverNbTab5Tree1['displaycolumns'] = ('Name', 'Email','Enabled',\
                 'Notification')
serverNbTab5Tree1.heading("Name", text="OPERATOR")
serverNbTab5Tree1.column("Name", minwidth=0,width=85)
serverNbTab5Tree1.heading("Email", text="EMAIL")
serverNbTab5Tree1.column("Email", minwidth=0,width=200)
serverNbTab5Tree1.heading("Enabled", text="ENABLED")
serverNbTab5Tree1.column("Enabled", minwidth=0,width=75)
serverNbTab5Tree1.heading("Notification", text="NOTIFICATION")
serverNbTab5Tree1.column("Notification", minwidth=0,width=100)

#Failsafe Operator
serverNbTab5Tree2=ttk.Treeview(serverNbTab5,show='headings',height=1,)
serverNbTab5Tree2.grid(row=0,column=1,padx=5, pady=5)
serverNbTab5Tree2['columns'] = ('FailSafeOperator')
serverNbTab5Tree2['displaycolumns'] = ('FailSafeOperator')
serverNbTab5Tree2.heading("FailSafeOperator", text="FAIL SAFE OPERATOR")
serverNbTab5Tree2.column("FailSafeOperator", minwidth=0,width=175)

#Alerts
serverNbTab5Tree3=ttk.Treeview(serverNbTab5,show='headings',height=9, )
serverNbTab5Tree3.grid(row=1,column=0,padx=5, pady=5,columnspan=2)
serverNbTab5Tree3['columns'] = ('Name', 'Severity','Enabled','')
serverNbTab5Tree3['displaycolumns'] = ('Name', 'Severity','Enabled','')
serverNbTab5Tree3.heading("Name", text="ALERT")
serverNbTab5Tree3.column("Name", minwidth=0,width=250)
serverNbTab5Tree3.heading("Severity", text="SEVERITY")
serverNbTab5Tree3.column("Severity", minwidth=0,width=100)
serverNbTab5Tree3.heading("Enabled", text="ENABLED")
serverNbTab5Tree3.column("Enabled", minwidth=0,width=100)

scrollbar_vertical = ttk.Scrollbar(serverNbTab5, orient="vertical", \
                                   command=serverNbTab5Tree3.yview)
scrollbar_vertical.grid(row=1, column=2, sticky="ns")
serverNbTab5Tree3.configure(yscrollcommand=scrollbar_vertical.set)

#DBEmail Tab
#Dashboard
serverNbTab6Tree1=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree1.grid(row=0,column=0,padx=5, pady=5, )
serverNbTab6Tree1['columns'] = ('SQLAgentEnabled')
serverNbTab6Tree1['displaycolumns'] = ('SQLAgentEnabled')
serverNbTab6Tree1.heading("SQLAgentEnabled", text="SQL Agent Enabled")
serverNbTab6Tree1.column("SQLAgentEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree2=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree2.grid(row=0,column=1,padx=5, pady=5, )
serverNbTab6Tree2['columns'] = ('SQLAgentStarted')
serverNbTab6Tree2['displaycolumns'] = ('SQLAgentStarted')
serverNbTab6Tree2.heading("SQLAgentStarted", text="SQL Agent Started")
serverNbTab6Tree2.column("SQLAgentStarted", minwidth=0,width=145,anchor="center")

serverNbTab6Tree3=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree3.grid(row=0,column=2,padx=5, pady=5, )
serverNbTab6Tree3['columns'] = ('DBMailEnabled')
serverNbTab6Tree3['displaycolumns'] = ('DBMailEnabled')
serverNbTab6Tree3.heading("DBMailEnabled", text="DBMail")
serverNbTab6Tree3.column("DBMailEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree4=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree4.grid(row=0,column=3,padx=5, pady=5, )
serverNbTab6Tree4['columns'] = ('MailProfileEnabled')
serverNbTab6Tree4['displaycolumns'] = ('MailProfileEnabled')
serverNbTab6Tree4.heading("MailProfileEnabled", text="Mail Profile")
serverNbTab6Tree4.column("MailProfileEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree5=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree5.grid(row=1,column=0,padx=5, pady=5, )
serverNbTab6Tree5['columns'] = ('MailAccountEnabled')
serverNbTab6Tree5['displaycolumns'] = ('MailAccountEnabled')
serverNbTab6Tree5.heading("MailAccountEnabled", text="Mail Account")
serverNbTab6Tree5.column("MailAccountEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree6=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree6.grid(row=1,column=1,padx=5, pady=5, )
serverNbTab6Tree6['columns'] = ('SQLAgentMailEnabled')
serverNbTab6Tree6['displaycolumns'] = ('SQLAgentMailEnabled')
serverNbTab6Tree6.heading("SQLAgentMailEnabled", text="SQL Agent Mail")
serverNbTab6Tree6.column("SQLAgentMailEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree7=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree7.grid(row=1,column=2,padx=5, pady=5, )
serverNbTab6Tree7['columns'] = ('SQLAgentMailProfileEnabled')
serverNbTab6Tree7['displaycolumns'] = ('SQLAgentMailProfileEnabled')
serverNbTab6Tree7.heading("SQLAgentMailProfileEnabled", \
                          text="SQL Agent Mail Profile")
serverNbTab6Tree7.column("SQLAgentMailProfileEnabled", minwidth=0,width=145,anchor="center")

serverNbTab6Tree8=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree8.grid(row=1,column=3,padx=5, pady=5, )
serverNbTab6Tree8['columns'] = ('retry_sec')
serverNbTab6Tree8['displaycolumns'] = ('retry_sec')
serverNbTab6Tree8.heading("retry_sec", text="Retry Sec")
serverNbTab6Tree8.column("retry_sec", minwidth=0,width=145,anchor="center")

#--#General Check Tab
#--REMOTE ADMIN
#--BACKUP COMPRESSION
#--AD HOC
#--MAXDOP
GenCheckLabel=ttk.Label(serverNbTab7,text="RemAdmin/BkpCompress/Adhoc/MaxDop")
GenCheckLabel.grid(row=0,column=0,padx=5, pady=5, sticky='w',)

serverNbTab7Tree2=ttk.Treeview(serverNbTab7,show='headings',height=4, )
serverNbTab7Tree2.grid(row=1,column=0,padx=5, pady=5, sticky='w')
serverNbTab7Tree2['columns'] = ('Name','Desc','Status',)
serverNbTab7Tree2['displaycolumns'] = ('Name','Desc','Status',)
serverNbTab7Tree2.heading("Name", text="NAME")
serverNbTab7Tree2.column("Name", minwidth=0,width=145)
serverNbTab7Tree2.heading("Desc", text="DESC")
serverNbTab7Tree2.column("Desc", minwidth=0,width=250)
serverNbTab7Tree2.heading("Status", text="STATUS")
serverNbTab7Tree2.column("Status", minwidth=0,width=145)

#--IFI Status
serverNbTab7Tree3=ttk.Treeview(serverNbTab7,show='headings',height=1, )
serverNbTab7Tree3.grid(row=1,column=1,padx=5, pady=5, sticky='n')
serverNbTab7Tree3['columns'] = ('IFIStatus',)
serverNbTab7Tree3['displaycolumns'] = ('IFIStatus',)
serverNbTab7Tree3.heading("IFIStatus", text="IFI Status")
serverNbTab7Tree3.column("IFIStatus", minwidth=0,width=145, anchor="center")

#--PENDING CONFIGURATIONS.
GenCheckLabel=ttk.Label(serverNbTab7,text="Pending Configurations")
GenCheckLabel.grid(row=2,column=0,padx=5, pady=5, sticky='w', columnspan=2)

serverNbTab7Tree1=ttk.Treeview(serverNbTab7,show='headings',height=4, )
serverNbTab7Tree1.grid(row=3,column=0,padx=5, pady=5, columnspan=2)
serverNbTab7Tree1['columns'] = ('Name','Desc','Value','ValueInUse',)
serverNbTab7Tree1['displaycolumns'] = ('Name','Desc','Value','ValueInUse',)
serverNbTab7Tree1.heading("Name", text="NAME")
serverNbTab7Tree1.column("Name", minwidth=0,width=145)
serverNbTab7Tree1.heading("Desc", text="DESC")
serverNbTab7Tree1.column("Desc", minwidth=0,width=250)
serverNbTab7Tree1.heading("Value", text="VALUE")
serverNbTab7Tree1.column("Value", minwidth=0,width=145)
serverNbTab7Tree1.heading("ValueInUse", text="VINUSE")
serverNbTab7Tree1.column("ValueInUse", minwidth=0,width=145)

#--#Databases Tab
#--Databases
serverNbTab8Tree1=ttk.Treeview(serverNbTab8,show='headings',height=12, )
serverNbTab8Tree1.grid(row=0,column=0,padx=5, pady=5, )
serverNbTab8Tree1['columns'] = ('Id','Name','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab8Tree1['displaycolumns'] = ('Id','Name','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab8Tree1.heading("Id", text="ID")
serverNbTab8Tree1.column("Id", minwidth=0,width=50,anchor="w")
serverNbTab8Tree1.heading("Name", text="NAME")
serverNbTab8Tree1.column("Name", minwidth=0,width=160,anchor="w")
serverNbTab8Tree1.heading("Owner", text="OWNER")
serverNbTab8Tree1.column("Owner", minwidth=0,width=175,anchor="w")
serverNbTab8Tree1.heading("Creation", text="CREATION")
serverNbTab8Tree1.column("Creation", minwidth=0,width=75,anchor="w")
serverNbTab8Tree1.heading("Compat", text="COMPAT")
serverNbTab8Tree1.column("Compat", minwidth=0,width=70,anchor="w")
serverNbTab8Tree1.heading("Status", text="STATUS")
serverNbTab8Tree1.column("Status", minwidth=0,width=70,anchor="w")
serverNbTab8Tree1.heading("Recovery", text="RECOVERY")
serverNbTab8Tree1.column("Recovery", minwidth=0,width=70,anchor="w")
serverNbTab8Tree1.heading("Verification", text="VERIFICATION")
serverNbTab8Tree1.column("Verification", minwidth=0,width=85,anchor="w")
serverNbTab8Tree1.heading("LRWait", text="LRWAIT")
serverNbTab8Tree1.column("LRWait", minwidth=0,width=115,anchor="w")

#--#Logins Sysadmin Tab
#--Sysadmin members
serverNbTab10Tree1=ttk.Treeview(serverNbTab10,show='headings',height=12, )
serverNbTab10Tree1.grid(row=1,column=1,padx=5, pady=5, sticky='n')
serverNbTab10Tree1['columns'] = ('Name','Type','Status','Creation','Db',)
serverNbTab10Tree1['displaycolumns'] = ('Name','Type','Status','Creation','Db',)
serverNbTab10Tree1.heading("Name", text="NAME")
serverNbTab10Tree1.column("Name", minwidth=0,width=250, )
serverNbTab10Tree1.heading("Type", text="TYPE")
serverNbTab10Tree1.column("Type", minwidth=0,width=145, )
serverNbTab10Tree1.heading("Status", text="STATUS")
serverNbTab10Tree1.column("Status", minwidth=0,width=145, )
serverNbTab10Tree1.heading("Creation", text="CREATION")
serverNbTab10Tree1.column("Creation", minwidth=0,width=145, )
serverNbTab10Tree1.heading("Db", text="DB")
serverNbTab10Tree1.column("Db", minwidth=0,width=145, )

#--#DBA Tools Tab
#--DBAdmin Database
labelDBAdmin=ttk.Label(serverNbTab9,text="DBAdmin Database")
labelDBAdmin.grid(row=0,column=0,padx=5, pady=5, sticky='w')
serverNbTab9Tree1=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree1.grid(row=1,column=0,padx=5, pady=5,columnspan=2 )
serverNbTab9Tree1['columns'] = ('Id','Name','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab9Tree1['displaycolumns'] = ('Id','Name','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab9Tree1.heading("Id", text="ID")
serverNbTab9Tree1.column("Id", minwidth=0,width=50,anchor="w")
serverNbTab9Tree1.heading("Name", text="NAME")
serverNbTab9Tree1.column("Name", minwidth=0,width=200,anchor="w")
serverNbTab9Tree1.heading("Owner", text="OWNER")
serverNbTab9Tree1.column("Owner", minwidth=0,width=50,anchor="w")
serverNbTab9Tree1.heading("Creation", text="CREATION")
serverNbTab9Tree1.column("Creation", minwidth=0,width=75,anchor="w")
serverNbTab9Tree1.heading("Compat", text="COMPAT")
serverNbTab9Tree1.column("Compat", minwidth=0,width=70,anchor="w")
serverNbTab9Tree1.heading("Status", text="STATUS")
serverNbTab9Tree1.column("Status", minwidth=0,width=70,anchor="w")
serverNbTab9Tree1.heading("Recovery", text="RECOVERY")
serverNbTab9Tree1.column("Recovery", minwidth=0,width=70,anchor="w")
serverNbTab9Tree1.heading("Verification", text="VERIFICATION")
serverNbTab9Tree1.column("Verification", minwidth=0,width=85,anchor="w")
serverNbTab9Tree1.heading("LRWait", text="LRWAIT")
serverNbTab9Tree1.column("LRWait", minwidth=0,width=150,anchor="w")

#--Service Restart Notification Job
labelDBAdmin=ttk.Label(serverNbTab9,text="Service Restart Notification Job")
labelDBAdmin.grid(row=2,column=0,padx=5, pady=5, sticky='w')
serverNbTab9Tree2=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree2.grid(row=3,column=0,padx=5, pady=5, sticky='w',)
serverNbTab9Tree2['columns'] = ('Name','Owner','Status','Desc',)
serverNbTab9Tree2['displaycolumns'] = ('Name','Owner','Status','Desc',)
serverNbTab9Tree2.heading("Name", text="NAME")
serverNbTab9Tree2.column("Name", minwidth=0,width=200,anchor="w")
serverNbTab9Tree2.heading("Owner", text="OWNER")
serverNbTab9Tree2.column("Owner", minwidth=0,width=50,anchor="w")
serverNbTab9Tree2.heading("Status", text="STATUS")
serverNbTab9Tree2.column("Status", minwidth=0,width=75,anchor="w")
serverNbTab9Tree2.heading("Desc", text="DESC")
serverNbTab9Tree2.column("Desc", minwidth=0,width=100,anchor="w")

#--sp_whoisactive
labelDBAdmin=ttk.Label(serverNbTab9,text="sp_whoisactive")
labelDBAdmin.grid(row=2,column=1,padx=5, pady=5, sticky='w')
serverNbTab9Tree3=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree3.grid(row=3,column=1,padx=5, pady=5, sticky='w')
serverNbTab9Tree3['columns'] = ('Name','Info',)
serverNbTab9Tree3['displaycolumns'] = ('Name','Info',)
serverNbTab9Tree3.heading("Name", text="NAME")
serverNbTab9Tree3.column("Name", minwidth=0,width=200,anchor="w")
serverNbTab9Tree3.heading("Info", text="INFO")
serverNbTab9Tree3.column("Info", minwidth=0,width=50,anchor="w")

#Bottoms
#DBAdminButton = ttk.Button(serverNbTab7, text='Install', underline = 0, command= lambda: get_detail_command(ConnMode.get()))
#DBAdminButton.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#Adding all Tabs to the Notebook
serverNb.add(serverNbTab1, text='Services',)
serverNb.add(serverNbTab2, text='Disks',)
serverNb.add(serverNbTab3, text='Page File',)
serverNb.add(serverNbTab4, text='Default Paths',)
serverNb.add(serverNbTab6, text='DBMail',)
serverNb.add(serverNbTab5, text='Alerts',)
serverNb.add(serverNbTab8, text='Databases',)
serverNb.add(serverNbTab10, text='Sysadmins',)
serverNb.add(serverNbTab7, text='General Check',)
serverNb.add(serverNbTab9, text='DBA Tools',)

inventoryframe['borderwidth'] = 2
inventoryframe['relief'] = 'groove'
detailframe['borderwidth'] = 2
detailframe['relief'] = 'groove'

window.mainloop()