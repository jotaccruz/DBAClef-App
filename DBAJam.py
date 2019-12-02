#pyinstaller DBAJam.py --windowed --onefile

# -*- coding: utf-8 -*-
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
import tkinter
from tkinter import *
from tkinter import ttk
import DBAJamSource
from DBAJamSource import *
import DBAJamOS
from DBAJamOS import *
import wmi
from wmi import *

window=Tk()

#Funtions----------------------------------------------------------------------
#------------------------------------------------------------------------------
#---
def getRbselected(mode):
    if (mode == 0):
        view_command()
    else:
        cleanall(InventoryTree)
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

#---
def cleanall(widget):
    for i in widget.get_children():
        widget.delete(i)

#---           
def hello():
    # create a canvas
    m1 = PanedWindow(window)
    m1.pack(fill=BOTH, expand=1)

    left = Label(m1, text="left pane")
    m1.add(left)
    
    m2 = PanedWindow(m1, orient=VERTICAL)
    m1.add(m2)
    
    top = Label(m2, text="top pane")
    m2.add(top)
    
    bottom = Label(m2, text="bottom pane")
    m2.add(bottom)

#---
def basic_analyze_command():
    return

#---
def view_command():
    for i in InventoryTree.get_children():
        InventoryTree.delete(i)
    
    query="SELECT srv_name as SERVER, srv_user as USER, SRV_PWD as PWD,"\
            " srv_ip as IP, srv_os as OS FROM lgm_servers WHERE"+ \
            " srv_name in"+\
            " ('SCAEDYAK02','SUSWEYAK05');"
    #query="SELECT srv_name as SERVER, srv_ip as IP, srv_os as OS,"\
    #       "srv_type as ENGINE, srv_location as LOCATION, srv_domain "\
    #        "as DOMAIN FROM lgm_servers WHERE"+ \
    #        " srv_location = 'GCP' and srv_active=1 and srv_name in"+\
    #        " ('SUSWEYAK03','SUSWEYAK05');"
    for row in dbservers(query):
        InventoryTree.insert("", END, values=(row[0],row[1],row[2],row[3],row[4]))

#---
def get_selected_command(event):
    return

#---
def get_detail_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "User": "test",
                "Pwd": ""
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
        except IndexError:
            pass

#Tab Special Settings----------------------------------------------------------
#------------------------------------------------------------------------------

#Hostname
    sqlexec="SELECT CONVERT(nvarchar(250),@@servername) AS 'ServerName\InstanceName',CONVERT(nvarchar(250),SERVERPROPERTY('servername')) AS 'ServerName',CONVERT(nvarchar(250),SERVERPROPERTY('machinename')) AS 'Windows_Name',CONVERT(nvarchar(250),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')) AS 'NetBIOS_Name',CONVERT(nvarchar(250),ISNULL(SERVERPROPERTY('instanceName'),'DEFAULT')) AS 'InstanceName',CONVERT(nvarchar(250),SERVERPROPERTY('IsClustered')) AS 'IsClustered'"

    for i in serverNbTab1Tree1.get_children():
        serverNbTab1Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))
    
#Services
    for i in serverNbTab1Tree2.get_children():
        serverNbTab1Tree2.delete(i)
        
    for row in mssqlinfo(mode, selected_row['Server']):
        if (row['State'] == "Stopped"):
            serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('need',))
        else:
            serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('good',))

    #serverNbTab2Tree1.tag_configure('need', background='red')    
    
#Tab Disks---------------------------------------------------------------------
#------------------------------------------------------------------------------

    for i in serverNbTab2Tree1.get_children():
        serverNbTab2Tree1.delete(i)
        
    for row in diskinfo(mode, selected_row['Server']):
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

    #serverNbTab2Tree1.tag_configure('need', background='red')

#Tab Page File-----------------------------------------------------------------
#------------------------------------------------------------------------------
    
    for i in serverNbTab3Tree1.get_children():
        serverNbTab3Tree1.delete(i)
        
    for row in pageinfo(mode, selected_row['Server']):
        serverNbTab3Tree1.insert("", END, values=(row['SystemName'],\
                                                      row['Automatic'],\
                                                      row['Caption'],\
                                                      row['Status'],\
                                                      row['CurrentUsage'],\
                                                      row['PeakUsage'],\
                                                      row['InitialSize'],\
                                                      row['MaximumSize']),\
        tags = ('good',))

    #serverNbTab3Tree1.tag_configure('need', background='red')

#Tab Default Paths-------------------------------------------------------------
#------------------------------------------------------------------------------

    sqlexec1="CREATE TABLE #DPaths(Type nvarchar(50),Location sql_variant, \
    Restart integer);CREATE TABLE #RDPaths(Type nvarchar(50),\
        Location sql_variant);EXECUTE dbo.get_defaultpathdb;"
        
    sqlexec2="CREATE TABLE #DPath(Type nvarchar(50),Location nvarchar(250),\
    Restart integer);INSERT INTO #DPath(Type,Location,Restart) SELECT Type,\
        CONVERT(NVARCHAR(250),Location),Restart FROM #DPaths;INSERT INTO \
        #DPath(Type,Location) SELECT Type,CONVERT(NVARCHAR(250),Location) \
        FROM #RDPaths WHERE Type='BackupDirectory';"
        
    sqlexec3="SELECT Type, Location, Restart, CASE WHEN (ISNULL(Restart,0)=1)\
    THEN 'Required' ELSE 'No' END AS Restart FROM #DPath;"

    for i in serverNbTab4Tree1.get_children():
        serverNbTab4Tree1.delete(i)
        
    for row in mssqldetailsp(selected_row['Server'],"DBAdmin",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (row[2]==1):
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('need',))
        else:
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('good',))
    #serverNbTab4Tree1.tag_configure('need', background='red')

#Tab Alerts--------------------------------------------------------------------
#------------------------------------------------------------------------------

#Operator
    sqlexec="SELECT name,email_address,CASE WHEN enabled=0 THEN 'No' ELSE \
    'Yes' END AS Enabled,CASE WHEN pager_days=0 THEN 'All' ELSE 'Some days' \
    END AS Notifications FROM msdb.dbo.sysoperators WHERE enabled = 1"

    for i in serverNbTab5Tree1.get_children():
        serverNbTab5Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree1.insert("", END, values=(row[0],row[1],row[2],row[3]))
    
#Alerts
    sqlexec="SELECT id,name,severity,CASE WHEN enabled=0 THEN 'No' ELSE 'Yes'\
    END AS Enabled FROM msdb.dbo.sysalerts"
    
    for i in serverNbTab5Tree3.get_children():
        serverNbTab5Tree3.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree3.insert("", END, values=(row[1],row[2],row[3]))
    
#Failsafe Operator
    sqlexec1="CREATE TABLE #AlertInfo (FailSafeOperator NVARCHAR(255),\
    NotificationMethod INT,ForwardingServer NVARCHAR(255),ForwardingSeverity \
    INT,PagerToTemplate NVARCHAR(255),PagerCCTemplate NVARCHAR(255),\
    PagerSubjectTemplate NVARCHAR(255),PagerSendSubjectOnly NVARCHAR(255),\
    ForwardAlways INT);"
        
    sqlexec2="INSERT  INTO #AlertInfo EXEC [master].[dbo].[sp_MSgetalertinfo] \
    @includeaddresses = 0;"
        
    sqlexec3="SELECT ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),\
    'No Fail safe Operator.')) AS \
    FailSafeOperator, CASE WHEN ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),'No Fail safe Operator.'))='No Fail safe Operator.' \
    THEN '0' ELSE '1' END as Semaphore FROM #AlertInfo;"

    for rows in serverNbTab5Tree2.get_children():
        serverNbTab5Tree2.delete(rows)
        
    for rows in mssqldetailsp(selected_row['Server'],"DBAdmin",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (rows[1]=='1'):
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('need'))
        else:
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('good'))

#Tab DBMail--------------------------------------------------------------------
#------------------------------------------------------------------------------

#SQL Server Agent enabled  
    sqlexec="SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled;' ELSE 'Enabled' END AS SQLAgentEnabled FROM sys.configurations WHERE [name] ='Agent XPs';"

    for i in serverNbTab6Tree1.get_children():
        serverNbTab6Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree1.insert("", END, values=(row[0]))

#SQL Server Agent status
    sqlexec="IF (SELECT CAST(SERVERPROPERTY('Edition') AS VARCHAR(30))) NOT LIKE 'Express Edition%' BEGIN SELECT CASE WHEN status_desc = 'Running' THEN 'Running' ELSE 'Stopped' END AS SQLAgentStarted FROM sys.dm_server_services WHERE servicename LIKE 'SQL Server Agent%' END;"

    for i in serverNbTab6Tree2.get_children():
        serverNbTab6Tree2.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree2.insert("", END, values=(row[0]))
    
#SQL Database Mail is enabled
    sqlexec="SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled;' ELSE 'Enabled' END AS DBMailEnabled  FROM sys.configurations WHERE [name] ='Database Mail XPs';"

    for i in serverNbTab6Tree3.get_children():
        serverNbTab6Tree3.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree3.insert("", END, values=(row[0]))

#@SQL Agent Mail Enabled     
    sqlexec="SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled FROM msdb.dbo.sysmail_profile;"

    for i in serverNbTab6Tree4.get_children():
        serverNbTab6Tree4.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree4.insert("", END, values=(row[0]))

#Mail Account Enabled
    sqlexec="SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS MailAccountEnabled FROM msdb.dbo.sysmail_account;"

    for i in serverNbTab6Tree5.get_children():
        serverNbTab6Tree5.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree5.insert("", END, values=(row[0]))

#SQL Server Agent is enabled to use Database Mail
    sqlexec="DECLARE @SQLAgentMailEnabled INT = 0; EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent', N'UseDatabaseMail', @SQLAgentMailEnabled OUTPUT; SELECT CASE WHEN @SQLAgentMailEnabled=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled"

    for i in serverNbTab6Tree6.get_children():
        serverNbTab6Tree6.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree6.insert("", END, values=(row[0]))

#SQL Server Agent is enabled to use Database Mail and Mail Profile is assigned
    sqlexec="DECLARE @SQLAgentMailProfileEnabled SYSNAME; EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',N'DatabaseMailProfile', @SQLAgentMailProfileEnabled OUTPUT; SELECT CASE WHEN COUNT(@SQLAgentMailProfileEnabled)=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailProfileEnabled"

    for i in serverNbTab6Tree7.get_children():
        serverNbTab6Tree7.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree7.insert("", END, values=(row[0]))

#get email retry interval configuration value
    sqlexec="SELECT paramvalue as retry_sec FROM msdb.dbo.sysmail_configuration WHERE paramname = 'AccountRetryDelay';"

    for i in serverNbTab6Tree8.get_children():
        serverNbTab6Tree8.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree8.insert("", END, values=(row[0]))


    #serverNbTab5Tree2.tag_configure('need', background='red')
    
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
filemenu.add_command(label="8 DatabaseOwner", command=hello)
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
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
window.config(menu=menubar)
window.wm_title("DBAJam")

#Frame Controls
inventoryframe = ttk.LabelFrame(window, width=250, height=200,text="Server")
inventoryframe.grid(row=0,column=0,padx=5, pady=5)

Statusframe1 = ttk.LabelFrame(window, width=525, height=192,text="Status")
Statusframe1.grid(row=0,column=1,padx=5, pady=5)

ConnMode = IntVar()
ConnMode.set(1)

Radiobutton(inventoryframe, text="Inventory", variable=ConnMode, value=0, command= lambda : getRbselected(ConnMode.get())).grid(row=0,column=0,padx=5, pady=5, sticky="W")
Radiobutton(inventoryframe, text="Local", variable=ConnMode, value=1,command= lambda : getRbselected(ConnMode.get())).grid(row=0,column=1,padx=5, pady=5, sticky="W")

#Texts
server_text=StringVar()
e1=ttk.Entry(inventoryframe,textvariable=server_text,width=20)
e1.grid(row=1,column=0,padx=5, pady=5)

#Bottoms
DetailButton = Button(inventoryframe, text='Connect', underline = 0, command= lambda: get_detail_command(ConnMode.get()))
DetailButton.grid(row=1, column=1, sticky="e", padx=5, pady=5)

#ScanButton = Button(inventoryframe, text='Scan', underline = 0, \
#                      command=get_detail_command)
#ScanButton.grid(row=2, column=2, sticky="s", padx=5, pady=5)

#ExitButton = Button(inventoryframe, text='Exit', underline = 0, \
#                      command=window.destroy)
#ExitButton.grid(row=3, column=2, sticky="s", padx=5, pady=5)

#TreeViews
InventoryTree=ttk.Treeview(inventoryframe,show='headings',height=5)
InventoryTree.grid(row=2,column=0,padx=5, pady=5,rowspan=6,columnspan=2)
InventoryTree['columns'] = ('Server', 'User', 'Pwd','Ip','Os')
InventoryTree['displaycolumns'] = ('Server','Ip','Os')
InventoryTree.column("Server", minwidth=0,width=100)
InventoryTree.heading("Server", text="SERVER",)
InventoryTree.column("Ip", minwidth=0,width=100)
InventoryTree.heading("Ip", text="IP",)
InventoryTree.column("Os", minwidth=0,width=100)
InventoryTree.heading("Os", text="OS",)
InventoryTree.heading("User", text="USER")
InventoryTree.heading("Pwd", text="PWD")

#if (selected_mode == 1):
#    InventoryTree.state(('disabled',))
#else:
#    InventoryTree.state(('!disabled',))
    
InventoryTree.bind('<Double-Button-1>',lambda x: DetailButton.invoke())

detailframe = ttk.LabelFrame(window, width=600, height=600, text="Detail")
detailframe.grid(row=2,column=0,padx=5, pady=5, columnspan=2)

serverNb=ttk.Notebook(detailframe)
serverNb.grid(row=0,column=0, sticky="e",padx=5, pady=5)

serverNbTab1=Frame(serverNb)
serverNbTab2=Frame(serverNb)
serverNbTab3=Frame(serverNb)
serverNbTab4=Frame(serverNb)
serverNbTab5=Frame(serverNb)
serverNbTab6=Frame(serverNb)

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
serverNbTab1Tree2=ttk.Treeview(serverNbTab1,show='headings',height=7,)
serverNbTab1Tree2.grid(row=1,column=0,padx=5, pady=5)
serverNbTab1Tree2['columns'] = ('SystemName', 'DisplayName', 'Description', 'Started','StartMode','StartName','State','Status',)
serverNbTab1Tree2['displaycolumns'] = ('SystemName', 'DisplayName', 'Description','StartMode','StartName','State',)
serverNbTab1Tree2.heading("SystemName", text="SERVER")
serverNbTab1Tree2.column("SystemName", minwidth=0,width=125)
serverNbTab1Tree2.heading("DisplayName", text="SERVICE")
serverNbTab1Tree2.column("DisplayName", minwidth=0,width=175)
serverNbTab1Tree2.heading("Description", text="DESC")
serverNbTab1Tree2.column("Description", minwidth=0,width=250)
serverNbTab1Tree2.heading("Started", text="STARTED")
serverNbTab1Tree2.column("Started", minwidth=0,width=50)
serverNbTab1Tree2.heading("StartMode", text="START")
serverNbTab1Tree2.column("StartMode", minwidth=0,width=60)
serverNbTab1Tree2.heading("StartName", text="ACCOUNT")
serverNbTab1Tree2.column("StartName", minwidth=0,width=155)
serverNbTab1Tree2.heading("State", text="STATE")
serverNbTab1Tree2.column("State", minwidth=0,width=60)
#serverNbTab1Tree2.heading("PathName", text="PATH")
#serverNbTab1Tree2.column("PathName", minwidth=0,width=180)

#Disks Tab
serverNbTab2Tree1=ttk.Treeview(serverNbTab2,show='headings',height=10,)
serverNbTab2Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab2Tree1['columns'] = ('SName', 'Name', 'DLetter','FSystem',
                 'Label', 'Capacity', 'FSpace', 'BSize','SUBSize')
serverNbTab2Tree1['displaycolumns'] = ('SName', 'Name', 'DLetter','FSystem',
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
serverNbTab2Tree1.column("Label", minwidth=0,width=150)
serverNbTab2Tree1.heading("Capacity", text="CAPACITY GB")
serverNbTab2Tree1.column("Capacity", minwidth=0,width=100)
serverNbTab2Tree1.heading("FSpace", text="FSPACE GB")
serverNbTab2Tree1.column("FSpace", minwidth=0,width=75)
serverNbTab2Tree1.heading("BSize", text="BSIZE KB")
serverNbTab2Tree1.column("BSize", minwidth=0,width=75)
serverNbTab2Tree1.heading("SUBSize", text="SUBSIZE KB")
serverNbTab2Tree1.column("SUBSize", minwidth=0,width=75)

#Page File Tab
serverNbTab3Tree1=ttk.Treeview(serverNbTab3,show='headings')
serverNbTab3Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab3Tree1['columns'] = ('SName', 'Automatic', 'Caption','Status',
                 'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximumSize')
serverNbTab3Tree1['displaycolumns'] = ('SName', 'Automatic', 'Caption','Status'
                 ,'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximumSize')
serverNbTab3Tree1.heading("SName", text="SERVER")
serverNbTab3Tree1.column("SName", minwidth=0,width=150)
serverNbTab3Tree1.heading("Automatic", text="AUTO")
serverNbTab3Tree1.column("Automatic", minwidth=0,width=50)
serverNbTab3Tree1.heading("Caption", text="FNAME")
serverNbTab3Tree1.column("Caption", minwidth=0,width=150)
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
serverNbTab4Tree1=ttk.Treeview(serverNbTab4,show='headings')
serverNbTab4Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab4Tree1['columns'] = ('Type', 'Location','Restart')
serverNbTab4Tree1['displaycolumns'] = ('Type', 'Location','Restart')
serverNbTab4Tree1.heading("Type", text="TYPE")
serverNbTab4Tree1.column("Type", minwidth=0,width=100)
serverNbTab4Tree1.heading("Location", text="LOCATION")
serverNbTab4Tree1.column("Location", minwidth=0,width=500)
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
serverNbTab5Tree3=ttk.Treeview(serverNbTab5,show='headings',height=7, )
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
serverNbTab6Tree7.column("SQLAgentMailProfileEnabled", minwidth=0,width=175,anchor="center")

serverNbTab6Tree8=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree8.grid(row=1,column=3,padx=5, pady=5, )
serverNbTab6Tree8['columns'] = ('retry_sec')
serverNbTab6Tree8['displaycolumns'] = ('retry_sec')
serverNbTab6Tree8.heading("retry_sec", text="Retry Sec")
serverNbTab6Tree8.column("retry_sec", minwidth=0,width=145,anchor="center")


#Adding all Tabs to the Notebook
serverNb.add(serverNbTab1, text='Special Settings',)
serverNb.add(serverNbTab2, text='Disks',)
serverNb.add(serverNbTab3, text='Page File',)
serverNb.add(serverNbTab4, text='Default Paths',)
serverNb.add(serverNbTab6, text='DBMail',)
serverNb.add(serverNbTab5, text='Alerts',)

inventoryframe['borderwidth'] = 2
inventoryframe['relief'] = 'groove'
detailframe['borderwidth'] = 2
detailframe['relief'] = 'groove'

window.mainloop()