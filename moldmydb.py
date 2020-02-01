#https://www.colorhexa.com/

#pyinstaller --windowed --onefile --add-binary "./files/moldmydb.png;files"
# --add-data "./scripts/StatusTree1_0.sql;scripts"
# --add-data "./scripts/StatusTree2_0.sql;scripts"
# --add-data "./scripts/StatusTree2_1.sql;scripts"
# --add-data "./scripts/StatusTree3_0.sql;scripts"
# --add-data "./scripts/StatusTree4_0.sql;scripts"
# --add-data "./scripts/serverNbTab1Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab4Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab4Tree1_1.sql;scripts"
# --add-data "./scripts/serverNbTab4Tree1_2.sql;scripts"
# --add-data "./scripts/serverNbTab4Tree1_3.sql;scripts"
# --add-data "./scripts/serverNbTab5Tree1_0.sql;scripts"  
# --add-data "./scripts/serverNbTab5Tree2_0.sql;scripts"
# --add-data "./scripts/serverNbTab5Tree2_1.sql;scripts"
# --add-data "./scripts/serverNbTab5Tree3_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree2_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree3_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree4_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree5_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree6_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree6_1.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree7_0.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree7_1.sql;scripts"
# --add-data "./scripts/serverNbTab6Tree8_0.sql;scripts"
# --add-data "./scripts/serverNbTab7Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab7Tree2_0.sql;scripts"
# --add-data "./scripts/serverNbTab7Tree3_0.sql;scripts"
# --add-data "./scripts/serverNbTab7Tree3_1.sql;scripts"
# --add-data "./scripts/serverNbTab8Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab9Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab9Tree2_0.sql;scripts"
# --add-data "./scripts/serverNbTab9Tree3_0.sql;scripts"
# --add-data "./scripts/serverNbTab9Tree4_0.sql;scripts"
# --add-data "./scripts/serverNbTab9Tree4_1.sql;scripts"
# --add-data "./scripts/serverNbTab10Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree1_0.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree1_1.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree2_0.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree2_1.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree2_2.sql;scripts"
# --add-data "./scripts/serverNbTab12Tree2_3.sql;scripts"
# --add-data "./scripts/ServiceButton_0.sql;scripts"
# --add-data "./scripts/ServiceButton_1.sql;scripts"
# --add-data "./scripts/spButton_0.sql;scripts"
# --add-data "./scripts/spButton_1.sql;scripts"
# --add-data "./scripts/StandardLoginsButton_0.sql;scripts"
# --add-data "./scripts/saButton_0.sql;scripts"
# --add-data "./scripts/AlertsButton_0.sql;scripts"
# --add-data "./scripts/mailButton_0.sql;scripts"
# --add-data "./scripts/genchkButton_0.sql;scripts"
# --add-data "./scripts/ifiButton_0.sql;scripts"
# --add-data "./scripts/ifiButton_1.sql;scripts"
# --add-data "./scripts/ifiButton_2.sql;scripts"
# --add-data "./scripts/ifiButton_3.sql;scripts"
# --add-data "./scripts/ifiButton_4.sql;scripts"

# --i ./files/moldmydb.ico moldmydb.py
 
#pyinstaller --windowed --onefile --icon=moldmydb.ico moldmydb.py
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
import moldmydbSource
from moldmydbSource import *
import moldmydbOS
from moldmydbOS import *
import wmi
from wmi import *
import moldmydbWeb
from moldmydbWeb import *
#import PIL
#from PIL import Image,ImageTk
import webbrowser
import moldmydbSQLFiles
from moldmydbSQLFiles import *
#import moldmydbReport
#from moldmydbReport import *

window=Tk()

#Funtions----------------------------------------------------------------------
#------------------------------------------------------------------------------
#---
def cleanallone():
    cleanall(VersionTree1)
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
    cleanall(serverNbTab9Tree4)
    cleanall(serverNbTab10Tree1)
    cleanall(serverNbTab12Tree1)
    cleanall(serverNbTab12Tree2)

def getRbselected(mode):
    if (mode == 0):
        InventoryButton.config(state=NORMAL)
        #view_command()
    #else:
        cleanallone()
    else:
        InventoryButton.config(state=DISABLED)
#---
def cleanall(widget):
    for i in widget.get_children():
        widget.delete(i)

#---

def getFileUrl(filename,directory):
    if getattr(sys, 'frozen', False): # Running as compiled
        running_dir = sys._MEIPASS + "/" + directory + "/" #"/files/" # Same path name than pyinstaller option
    else:
        running_dir = "./" + directory + "/" # Path name when run with Python interpreter
    FileName = running_dir + filename #"moldmydb.png"
    return FileName 

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def About():
    tkinter.messagebox.showinfo(title="moldmydb", message="Telus International - moldmydb v 1.0",)
    for i in serverNbTab1Tree1.get_children():
        server=(serverNbTab1Tree1.item(i)["values"][2])
    #ReportAssessment(server,StatusTree4)

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
    tkinter.messagebox.askquestion(title="moldmydb", message="Telus International - moldmydb v 1.0",)

#---
def basic_analyze_command():
    return

#---
def view_command():
    for i in InventoryTree.get_children():
        InventoryTree.delete(i)
    
    query="SELECT srv_name as SERVER, srv_instance as INSTANCE, srv_ip as IP,"+\
            "srv_ins_port as PORT, '' as USER, '' as PWD, srv_os as OS"+\
            " FROM lgm_servers"# WHERE"+\
            #" srv_name in"+\
            #" ('SCAEDYAK02','SUSWEYAK05');"
    #print (query)
    #query="SELECT srv_name as SERVER, srv_ip as IP, srv_os as OS,"\
    #       "srv_type as ENGINE, srv_location as LOCATION, srv_domain "\
    #        "as DOMAIN FROM lgm_servers WHERE"+ \
    #        " srv_location = 'GCP' and srv_active=1 and srv_name in"+\
    #        " ('SUSWEYAK03','SUSWEYAK05');"
    mysqlserver=ip.get()
    mysqlusername=user.get()
    mysqlpsw=pas.get()
    
    #try:
    for row in dbservers(query,mysqlserver,mysqlusername,mysqlpsw):
        InventoryTree.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]),tags = ('color'))
    InventoryTree.tag_configure('color', background='#aba9f8')
    #except:
        #tkinter.messagebox.showerror("moldmydb", "Error connecting to the Inventory Database")

#---
def get_selected_command(event):
    return


#Install buttons

#DBAdmin database Install
def get_dbadmin_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec="IF  NOT EXISTS (\
    	SELECT name \
		FROM sys.databases \
		WHERE name = N'DBAdmin'\
        )\
        BEGIN\
        CREATE DATABASE DBAdmin;\
        ALTER DATABASE DBAdmin SET RECOVERY SIMPLE;\
        END;"
    sqlexec1="use DBAdmin; exec sp_changedbowner 'sa';"
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1)
        DBAdminButton.config(state=DISABLED)
        success_handler("DBAdmin","Database was created")
    except:
        DBAdminButton.config(state=NORMAL)
        error_handler("Error","DBAdmin")

#Service Restart Notification Job
def get_servicerestart_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("ServiceButton_0.sql","scripts"))
    
    dba_profile='dba_profile'
    for i in serverNbTab1Tree1.get_children():
        server=(serverNbTab1Tree1.item(i)["values"][2])
    
    sqlexec0 = readFileFromOS(getFileUrl("ServiceButton_1.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"msdb",
                               selected_row['User'],selected_row['Pwd'],sqlexec)
        mssqlexec(selected_row['Ip'],selected_row['Port'],"msdb",
                               selected_row['User'],selected_row['Pwd'],sqlexec0)
    
        sqlexec1="EXECUTE dbo.get_servicenotification '" + dba_profile + "', '" + server + "';"
    
        mssqlexec(selected_row['Ip'],selected_row['Port'],"msdb",
                               selected_row['User'],selected_row['Pwd'],sqlexec1)
        
        ServiceButton.config(state=DISABLED)
        success_handler("Service Restart","Job was created")
    except:
        ServiceButton.config(state=NORMAL)
        error_handler("Error","Service Restart")        

    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)

#Sp Who is active
def get_spwhoisactive_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("spButton_0.sql","scripts"))
    sqlexec1 = readFileFromOS(getFileUrl("spButton_1.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"DBAdmin",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        mssqlexec(selected_row['Ip'],selected_row['Port'],"DBAdmin",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1)
        spButton.config(state=DISABLED)
        success_handler("sp_whoisactive","Store Procedure was created")
    except:
        spButton.config(state=NORMAL)
        error_handler("Error","sp_whoisactive")


#Standard Processes Logins
def get_logins_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("StandardLoginsButton_0.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        StandardLoginsButton.config(state=DISABLED)
        success_handler("Logins","Logins were created")
    except:
        StandardLoginsButton.config(state=NORMAL)
        error_handler("Error","Logins")


#DBMail
def get_mail_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("mailButton_0.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        mailButton.config(state=DISABLED)
        success_handler("DB Mail","DB Mail successfuly configured")
    except:
        mailButton.config(state=NORMAL)
        error_handler("Error","DB Mail config error")

#Alerts
def get_alerts_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("AlertsButton_0.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        AlertsButton.config(state=DISABLED)
        success_handler("Alerts","Alerts successfuly configured")
    except:
        AlertsButton.config(state=NORMAL)
        error_handler("Error","Alerts config error")

#--sa owner
def get_sa_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("saButton_0.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        saButton.config(state=DISABLED)
        success_handler("DB Owner","sa was set sucessfuly")
    except:
        saButton.config(state=NORMAL)
        error_handler("Error","DB Owner sa config error")


#Remote Admin
#Backup
def get_genchk_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass
        
    sqlexec = readFileFromOS(getFileUrl("genchkButton_0.sql","scripts"))
    
    try:
        mssqlexec(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec)
        genchkButton.config(state=DISABLED)
        success_handler("Configurations","Configs set sucessfuly")
    except:
        genchkButton.config(state=NORMAL)
        error_handler("Error","Configurations error")

#IFI Testing
def get_ifitest_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
        except IndexError:
            pass

    #try:
    sqlexec = readFileFromOS(getFileUrl("ifiButton_0.sql","scripts"))
    sqlexec0 = readFileFromOS(getFileUrl("ifiButton_1.sql","scripts"))

    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec0)

    sqlexec1 = readFileFromOS(getFileUrl("ifiButton_2.sql","scripts"))
        
    sqlexec2 = readFileFromOS(getFileUrl("ifiButton_3.sql","scripts"))
    
    sqlexec3 = readFileFromOS(getFileUrl("ifiButton_4.sql","scripts"))
    
        
    for row in mssqldetailsp(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2,sqlexec3):
        if (row[1]==0):
            serverNbTab7Tree3.insert("", END, values=(row[0], ),tags = ('need'))
        else:
            serverNbTab7Tree3.insert("", END, values=(row[0], ),tags = ('good'))
    
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    
    serverNbTab7Tree3.tag_configure('need', background='#f86d7e')
    #except:
    #    ifiButton.config(state=NORMAL)
    #    error_handler("Error","IFI testing failed")
    
#---Main
def get_detail_command(mode):
    if (mode == 1):
        selected_row = {
                "Server": "127.0.0.1",
                "Ip": "127.0.0.1",
                "Port": e2.get(),
                "User": SQLUser.get(),
                "Pwd": SQLPass.get()
                }
        wmiuser=''
        wmipass=''
    else:
        try:
            selected_row=InventoryTree.set(InventoryTree.selection())
            selected_row.update({"User": SQLUser.get(),"Pwd": SQLPass.get()})
            
            #WMI Authentication
            wmiuser = simpledialog.askstring("WMI Credential", "Username (ti\\username)", parent=window)
            if (wmiuser!=None):
                wmipass = simpledialog.askstring("WMI Credential", "Password:", show='*', parent=window)
        except IndexError:
            pass

#Tab Status
#Last startup
    sqlexec1 = readFileFromOS(getFileUrl("StatusTree1_0.sql","scripts"))
    for i in StatusTree1.get_children():
        StatusTree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1):
        StatusTree1.insert("", END, values=(row[0],row[1]))
        
#CPUs
    sqlexec1 = readFileFromOS(getFileUrl("StatusTree2_0.sql","scripts"))

    sqlexec3 = readFileFromOS(getFileUrl("StatusTree2_1.sql","scripts"))
    
    for i in StatusTree2.get_children():
        StatusTree2.delete(i)
        
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec3):
        StatusTree2.insert("", END, values=(row[0],row[1],row[2]))

#Version
    sqlexec1 = readFileFromOS(getFileUrl("StatusTree3_0.sql","scripts"))
    for i in StatusTree3.get_children():
        StatusTree3.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1):
        StatusTree3.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))

#Is Supported?
        
    for i in StatusTree3.get_children():
        if (float(StatusTree3.item(i)["values"][0][0:2])<11):
            VersionTree1.insert("", END, values=("So\\ Sorry!!!\\ Version\\ is\\ not\\ supported.\\ Some\\ functionalities\\ may\\ don't\\ work"), tags = ('need',))
        else:
            VersionTree1.insert("", END, values=("Version\\ is\\ supported."), tags = ('good',))
    
    VersionTree1.tag_configure('need', background='#f86d7e')
                               
#Missing updates
    
    sqlexec1=readFileFromOS(getFileUrl("StatusTree4_0.sql","scripts"))
    
    for i in StatusTree4.get_children():
        StatusTree4.delete(i)
        
    try:
        for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
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
    except:
        StatusTree4.insert("", END, values=('',),tags = ('need',))
        pass
    
    StatusTree4.tag_configure('need', background='#f86d7e')
                              
#Tab Services----------------------------------------------------------
#------------------------------------------------------------------------------

#Hostname
    sqlexec= readFileFromOS(getFileUrl("serverNbTab1Tree1_0.sql","scripts"))

    for i in serverNbTab1Tree1.get_children():
        serverNbTab1Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[1]!=row[2]):
            serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],),tags = ('need'))
        else:
            serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],),tags = ('good'))
    serverNbTab1Tree1.tag_configure('need', background='#f86d7e')

#Services
    for i in serverNbTab1Tree2.get_children():
        serverNbTab1Tree2.delete(i)
        
    try:
        for row in mssqlinfo(mode, selected_row['Ip'], wmiuser, wmipass):
            if (row['State'] == "Stopped"):
                serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('need',))
            else:
                serverNbTab1Tree2.insert("", END, values=(row['SystemName'],row['DisplayName'],row['Description'],row['Started'],row['StartMode'],row['StartName'],row['State'],row['Status'],),tags = ('good',))
    except:
        serverNbTab1Tree2.insert("", END, values=("",'Missing','','','','','','',),tags = ('need',))
        pass        
    
    serverNbTab1Tree2.tag_configure('need', background='#f86d7e')
    
#Tab Disks---------------------------------------------------------------------
#------------------------------------------------------------------------------

    for i in serverNbTab2Tree1.get_children():
        serverNbTab2Tree1.delete(i)
        
    try:
        for row in diskinfo(mode, selected_row['Ip'], wmiuser, wmipass):
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
    
    except:
        serverNbTab2Tree1.insert("", END, values=('',\
                                                  'Missing',\
                                                  '',\
                                                  '',\
                                                  '',\
                                                  '',\
                                                  '',\
                                                  '',\
                                                  ''),\
        tags = ('need',))
        serverNbTab2Tree1.tag_configure('need', background='#f86d7e')
        pass
    

#Tab Page File-----------------------------------------------------------------
#------------------------------------------------------------------------------
    
    for i in serverNbTab3Tree1.get_children():
        serverNbTab3Tree1.delete(i)
        
    try:
        for row in pageinfo(mode, selected_row['Ip'], wmiuser, wmipass):
            serverNbTab3Tree1.insert("", END, values=(row['SystemName'],\
                                                          row['Automatic'],\
                                                          row['Caption'],\
                                                          row['Status'],\
                                                          row['CurrentUsage'],\
                                                          row['PeakUsage'],\
                                                          row['InitialSize'],\
                                                          row['MaximumSize']),\
            tags = ('good',))
    except:
        serverNbTab3Tree1.insert("", END, values=('',
                                                  '',
                                                  'Missing',
                                                  '',
                                                  '',
                                                  '',
                                                  '',
                                                  ''),
        tags = ('need',))
        pass
    serverNbTab3Tree1.tag_configure('need', background='#f86d7e')

#Tab Default Paths-------------------------------------------------------------
#------------------------------------------------------------------------------
    sqlexec = readFileFromOS(getFileUrl("serverNbTab4Tree1_0.sql","scripts"))
    sqlexec0 = readFileFromOS(getFileUrl("serverNbTab4Tree1_1.sql","scripts"))
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec0)

    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab4Tree1_2.sql","scripts"))
        
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab4Tree1_3.sql","scripts"))
        
    for i in serverNbTab4Tree1.get_children():
        serverNbTab4Tree1.delete(i)
        
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2):
        if (row[2]==1):
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('need',))
        else:
            serverNbTab4Tree1.insert("", END, values=(row[0],row[1],row[3]),\
                                     tags = ('good',))
    
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    serverNbTab4Tree1.tag_configure('need', background='#f86d7e')

#Alerts Tab--------------------------------------------------------------------
#------------------------------------------------------------------------------

#Operator
    sqlexec = readFileFromOS(getFileUrl("serverNbTab5Tree1_0.sql","scripts"))

    for i in serverNbTab5Tree1.get_children():
        serverNbTab5Tree1.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree1.insert("", END, values=(row[0],row[1],row[2],row[3]),tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab5Tree1.insert("", END, values=("Missing","","","",),tags = ('need'))
        AlertsButton.config(state=NORMAL)
    
    serverNbTab5Tree1.tag_configure('need', background='#f86d7e')
    #serverNbTab5Tree1.tag_configure('good', background='#aef38c')
                   
#Alerts
    sqlexec = readFileFromOS(getFileUrl("serverNbTab5Tree3_0.sql","scripts"))
    
    for i in serverNbTab5Tree3.get_children():
        serverNbTab5Tree3.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab5Tree3.insert("", END, values=(row[1],row[2],row[3]),tags = ('good'))
        rows=rows+1
    if rows==0 or rows<13 :
        serverNbTab5Tree3.insert("", END, values=("Missing","","",),tags = ('need'))
        AlertsButton.config(state=NORMAL)
    
    serverNbTab5Tree3.tag_configure('need', background='#f86d7e')
    #serverNbTab5Tree3.tag_configure('good', background='#aef38c')
                   
#Failsafe Operator
    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab5Tree2_0.sql","scripts"))
        
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab5Tree2_1.sql","scripts"))
        
    for rows in serverNbTab5Tree2.get_children():
        serverNbTab5Tree2.delete(rows)
        
    for rows in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2):
        if (rows[1]=='1'):
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('need'))
            AlertsButton.config(state=NORMAL)
        else:
            serverNbTab5Tree2.insert("", END, values=(rows[0], ),tags = ('good'))
    
    serverNbTab5Tree2.tag_configure('need', background='#f86d7e')
    #serverNbTab5Tree2.tag_configure('good', background='#aef38c')
               
#DBMail Tab--------------------------------------------------------------------
#------------------------------------------------------------------------------

#SQL Server Agent enabled  
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree1_0.sql","scripts"))

    for i in serverNbTab6Tree1.get_children():
        serverNbTab6Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree1.insert("", END, values=(row[0]), tags = ('need'))
        else:
            serverNbTab6Tree1.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree1.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree1.tag_configure('good', background='#aef38c')
                                    
#SQL Server Agent status
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree2_0.sql","scripts"))

    for i in serverNbTab6Tree2.get_children():
        serverNbTab6Tree2.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Running.'):
            serverNbTab6Tree2.insert("", END, values=(row[0]), tags = ('good'))
        else:
            serverNbTab6Tree2.insert("", END, values=(row[0]), tags = ('need'))
    
    serverNbTab6Tree2.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree2.tag_configure('good', background='#aef38c')
                                    
#SQL Database Mail is enabled
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree3_0.sql","scripts"))

    for i in serverNbTab6Tree3.get_children():
        serverNbTab6Tree3.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='Disabled'):
            serverNbTab6Tree3.insert("", END, values=(row[0]), tags = ('need'))
            mailButton.config(state=NORMAL)
        else:
            serverNbTab6Tree3.insert("", END, values=(row[0]), tags = ('good'))
    
    serverNbTab6Tree3.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree3.tag_configure('good', background='#aef38c')
               
#@Mail Profile
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree4_0.sql","scripts"))

    for i in serverNbTab6Tree4.get_children():
        serverNbTab6Tree4.delete(i)
    
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree4.insert("", END, values=(row[0]), tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab6Tree4.insert("", END, values=("Missing"), tags = ('need'))
        mailButton.config(state=NORMAL)
            
    serverNbTab6Tree4.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree4.tag_configure('good', background='#aef38c')
               
#Mail Account
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree5_0.sql","scripts"))

    for i in serverNbTab6Tree5.get_children():
        serverNbTab6Tree5.delete(i)
    
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree5.insert("", END, values=(row[0]), tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab6Tree5.insert("", END, values=("Missing"), tags = ('need'))
        mailButton.config(state=NORMAL)
        
    serverNbTab6Tree5.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree5.tag_configure('good', background='#aef38c')
               
#SQL Server Agent is enabled to use Database Mail
    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab6Tree6_0.sql","scripts"))
    
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab6Tree6_1.sql","scripts"))
    
    for i in serverNbTab6Tree6.get_children():
        serverNbTab6Tree6.delete(i)
        
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2):
        if (row[0]=='Enabled'):
            serverNbTab6Tree6.insert("", END, values=(row[0]), tags = ('good'))
        else:
            serverNbTab6Tree6.insert("", END, values=(row[0]), tags = ('need'))
            mailButton.config(state=NORMAL)
    
    serverNbTab6Tree6.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree6.tag_configure('good', background='#aef38c')
               
#SQL Server Agent is enabled to use Database Mail and Mail Profile is assigned
    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab6Tree7_0.sql","scripts"))
    
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab6Tree7_1.sql","scripts"))

    for i in serverNbTab6Tree7.get_children():
        serverNbTab6Tree7.delete(i)
        
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2):
        #print (row[0])
        if (row[0]=='Missing' or row[0]=='Express Edition'):
            serverNbTab6Tree7.insert("", END, values=(row[0]), tags = ('need'))
            mailButton.config(state=NORMAL)
        else:
            serverNbTab6Tree7.insert("", END, values=(row[0]), tags = ('good'))
            
    serverNbTab6Tree7.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree7.tag_configure('good', background='#aef38c')
               
#get email retry interval configuration value
    sqlexec = readFileFromOS(getFileUrl("serverNbTab6Tree8_0.sql","scripts"))

    for i in serverNbTab6Tree8.get_children():
        serverNbTab6Tree8.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab6Tree8.insert("", END, values=(row[0],),tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab6Tree8.insert("", END, values=("","Missing",),tags = ('need'))
    
    serverNbTab6Tree8.tag_configure('need', background='#f86d7e')
    #serverNbTab6Tree8.tag_configure('good', background='#aef38c')
               
#General Check
#--PENDING CONFIGURATIONS.
    sqlexec = readFileFromOS(getFileUrl("serverNbTab7Tree1_0.sql","scripts"))

    for i in serverNbTab7Tree1.get_children():
        serverNbTab7Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab7Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],),tags = ('need'))
    serverNbTab7Tree1.tag_configure('need', background='#f86d7e')

#--REMOTE ADMIN
#--BACKUP COMPRESSION
#--AD HOC
#--MAXDOP

    sqlexec = readFileFromOS(getFileUrl("serverNbTab7Tree2_0.sql","scripts"))

    for i in serverNbTab7Tree2.get_children():
        serverNbTab7Tree2.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[2]=='OFF'):
            serverNbTab7Tree2.insert("", END, values=(row[0],row[1],row[2],),tags = ('need'))
            genchkButton.config(state=NORMAL)
        else:
            serverNbTab7Tree2.insert("", END, values=(row[0],row[1],row[2],),tags = ('good'))
    serverNbTab7Tree2.tag_configure('need', background='#f5e45e')

#--IFI STATUS
    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab7Tree3_0.sql","scripts"))
        
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab7Tree3_1.sql","scripts"))

    for i in serverNbTab7Tree3.get_children():
        serverNbTab7Tree3.delete(i)
        
    for rows in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec2):
        if (rows[0]=='disabled'):
            serverNbTab7Tree3.insert("", END, values=(rows[0], ),tags = ('need'))
        else:
            serverNbTab7Tree3.insert("", END, values=(rows[0], ),tags = ('good'))
            ifiButton.config(state=NORMAL)
   
    serverNbTab7Tree3.tag_configure('need', background='#f86d7e')
    #serverNbTab7Tree3.tag_configure('good', background='#aef38c')
    
    
#Databases
#--DATABASES
    sqlexec = readFileFromOS(getFileUrl("serverNbTab8Tree1_0.sql","scripts"))

    for i in serverNbTab8Tree1.get_children():
        serverNbTab8Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[3]!='sa' or row[2]=='Take Care'):
            serverNbTab8Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],),tags = ('need'))
            saButton.config(state=NORMAL)
        else:
            serverNbTab8Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],),tags = ('good'))
            
    serverNbTab8Tree1.tag_configure('need', background='#f86d7e')

#Transaction Log
#--Transaction Log Usage
    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab12Tree1_0.sql","scripts"))
        
    sqlexec2 = readFileFromOS(getFileUrl("serverNbTab12Tree1_1.sql","scripts"))

    for i in serverNbTab12Tree1.get_children():
        serverNbTab12Tree1.delete(i)
        
    for rows in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec1,
                           sqlexec2):
        if (rows[2]>90):
            serverNbTab12Tree1.insert("", END, values=(rows[0],rows[1],rows[2],rows[3], ),tags = ('need'))
        else:
            serverNbTab12Tree1.insert("", END, values=(rows[0],rows[1],rows[2],rows[3], ),tags = ('good'))
   
    serverNbTab12Tree1.tag_configure('need', background='#f86d7e')
    #serverNbTab12Tree1.tag_configure('good', background='#aef38c')

    sqlexec = readFileFromOS(getFileUrl("serverNbTab12Tree2_0.sql","scripts"))
    sqlexec0 = readFileFromOS(getFileUrl("serverNbTab12Tree2_1.sql","scripts"))
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec0)

    sqlexec1 = readFileFromOS(getFileUrl("serverNbTab12Tree2_2.sql","scripts"))

    sqlexec3 = readFileFromOS(getFileUrl("serverNbTab12Tree2_3.sql","scripts"))
    
    for i in serverNbTab12Tree2.get_children():
        serverNbTab12Tree2.delete(i)
        
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec1,\
                           sqlexec3):
        if (row[1]>200):
            serverNbTab12Tree2.insert("", END, values=(row[0],row[1],),tag='need')
        else:
            serverNbTab12Tree2.insert("", END, values=(row[0],row[1],),tag='good')
    
    mssqlexec(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec)

    serverNbTab12Tree2.tag_configure('need', background='#f86d7e')
    #serverNbTab12Tree2.tag_configure('good', background='#aef38c')

#Logins
#--Sysadmin Logins
    sqlexec = readFileFromOS(getFileUrl("serverNbTab10Tree1_0.sql","scripts"))

    for i in serverNbTab10Tree1.get_children():
        serverNbTab10Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]=='BUILTIN\\Users' or row[0]=='NT AUTHORITY\\SYSTEM'):
            serverNbTab10Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('need'))
        else:
            serverNbTab10Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('good'))
            
    serverNbTab10Tree1.tag_configure('need', background='#f86d7e')

#DBA Tools
#--DBAdmin
    sqlexec = readFileFromOS(getFileUrl("serverNbTab9Tree1_0.sql","scripts"))

    for i in serverNbTab9Tree1.get_children():
        serverNbTab9Tree1.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[3]!='sa' or row[2]=='Take Care' ):
            serverNbTab9Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],),tags = ('need'))
        else:
            serverNbTab9Tree1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],),tags = ('good'))
        rows=1

    if rows==0:
        serverNbTab9Tree1.insert("", END, values=("","Missing","","","","","","","",),tags = ('need'))
        DBAdminButton.config(state=NORMAL)
    
    serverNbTab9Tree1.tag_configure('need', background='#f86d7e')
    #serverNbTab9Tree1.tag_configure('good', background='#aef38c')
               
#--Service Restart Notification
    sqlexec = readFileFromOS(getFileUrl("serverNbTab9Tree2_0.sql","scripts"))

    for i in serverNbTab9Tree2.get_children():
        serverNbTab9Tree2.delete(i)
        
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab9Tree2.insert("", END, values=(row[0],row[1],row[2],row[3],),tags = ('good'))
        rows=1

    if rows==0:
        serverNbTab9Tree2.insert("", END, values=("Missing","","","",),tags = ('need'))
        ServiceButton.config(state=NORMAL)
    
    serverNbTab9Tree2.tag_configure('need', background='#f86d7e')
    #serverNbTab9Tree2.tag_configure('good', background='#aef38c')
                                    
#--sp_whoisactive
    sqlexec = readFileFromOS(getFileUrl("serverNbTab9Tree3_0.sql","scripts"))

    for i in serverNbTab9Tree3.get_children():
        serverNbTab9Tree3.delete(i)
    
    rows=0
    for row in mssqldetail(selected_row['Ip'],selected_row['Port'],"master",
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        if (row[0]!='Missing'):
            serverNbTab9Tree3.insert("", END, values=(row[0],row[1],),tags = ('good'))
        else:
            serverNbTab9Tree3.insert("", END, values=(row[0],row[1],),tags = ('need'))
            spButton.config(state=NORMAL)
        rows=1
        
    if rows==0:
        serverNbTab9Tree3.insert("", END, values=("Missing","",),tags = ('need'))
        spButton.config(state=NORMAL)
    
    serverNbTab9Tree3.tag_configure('need', background='#f86d7e')
    #serverNbTab9Tree3.tag_configure('good', background='#aef38c')

#--Standard Processes Logins
    sqlexec0 = readFileFromOS(getFileUrl("serverNbTab9Tree4_0.sql","scripts"))
    
    sqlexec = readFileFromOS(getFileUrl("serverNbTab9Tree4_1.sql","scripts"))
    
    for i in serverNbTab9Tree4.get_children():
        serverNbTab9Tree4.delete(i)
    rows=0    
    for row in mssqldetail2sql(selected_row['Ip'],selected_row['Port'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec0,\
                           sqlexec):
        if (row[1]=='Missing'):
            serverNbTab9Tree4.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('need'))
            StandardLoginsButton.config(state=NORMAL)
        else:
            serverNbTab9Tree4.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],),tags = ('good'))
        rows=1
    
    if rows==0:
        serverNbTab9Tree4.insert("", END, values=("Missing","",),tags = ('need'))
        StandardLoginsButton.config(state=NORMAL)
        
    serverNbTab9Tree4.tag_configure('need', background='#f86d7e')


####### main ------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    
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
window.wm_title("moldmydb")

iconFileName=getFileUrl("moldmydb.png","files")

if os.path.isfile(iconFileName):
    photo = PhotoImage(file = iconFileName)
    window.iconphoto(False,photo)

#Frame Controls
inventoryframe = ttk.LabelFrame(window, width=250, height=200,text="Server")
inventoryframe.grid(row=0,column=0,padx=5, pady=5, rowspan=2)

inventory2frame = ttk.LabelFrame(inventoryframe, width=250, height=200,text="")
inventory2frame.grid(row=0,column=0,padx=5, pady=5, rowspan=4,sticky='n',)

inventory3frame = ttk.LabelFrame(inventoryframe, width=250, height=200,text="")
inventory3frame.grid(row=0,column=1,padx=5, pady=5, sticky='n',columnspan=2)

versionframe = ttk.LabelFrame(window, width=525, height=50,)
versionframe.grid(row=0,column=1,padx=5, pady=5, sticky='n')

statusframe = ttk.LabelFrame(window, width=525, height=192,text="Status")
statusframe.grid(row=1,column=1,padx=5, pady=5, sticky='n')

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

labelPort=ttk.Label(inventory3frame,text="Port", wraplength=50)
labelPort.grid(row=1,column=0,padx=5, pady=5, sticky='w')
Port=StringVar()
e2=ttk.Entry(inventory3frame,textvariable=Port,width=20)
e2.grid(row=1,column=1,padx=5, pady=5,sticky="w")

labelSQLUser=ttk.Label(inventoryframe,text="SQL Login", wraplength=50)
labelSQLUser.grid(row=2,column=1,padx=5, pady=5, sticky='w')
SQLUser=StringVar()
SQLUserEntry=ttk.Entry(inventoryframe,textvariable=SQLUser,width=20)
SQLUserEntry.grid(row=2,column=2,padx=5, pady=5,sticky="w")

labelSQLPass=ttk.Label(inventoryframe,text="Password", wraplength=50)
labelSQLPass.grid(row=3,column=1,padx=5, pady=5, sticky='w')
SQLPass=StringVar()
SQLPassEntry=ttk.Entry(inventoryframe,textvariable=SQLPass,show='*',width=20)
SQLPassEntry.grid(row=3,column=2,padx=5, pady=5,sticky="w")

#Bottoms
DetailButton = ttk.Button(inventoryframe, text='Connect', underline = 0, command= lambda: get_detail_command(ConnMode.get()))
DetailButton.grid(row=10, column=2, sticky="e", padx=5, pady=5,)

InventoryButton = ttk.Button(inventory2frame, state=DISABLED, text='Load', underline = 0, command= lambda: view_command())
InventoryButton.grid(row=0, column=1, sticky="e", padx=5, pady=5,)

#ScanButton = Button(inventoryframe, text='Scan', underline = 0, \
#                      command=get_detail_command)
#ScanButton.grid(row=2, column=2, sticky="s", padx=5, pady=5)

#ExitButton = Button(inventoryframe, text='Exit', underline = 0, \
#                      command=window.destroy)
#ExitButton.grid(row=3, column=2, sticky="s", padx=5, pady=5)

#TreeViews
InventoryTree=ttk.Treeview(inventoryframe,show='headings',height=3)
InventoryTree.grid(row=4,column=0,padx=5, pady=5,rowspan=6,columnspan=3)
InventoryTree['columns'] = ('Server', 'Instance', 'Ip', 'Port', 'User', 'Pwd','Os')
InventoryTree['displaycolumns'] = ('Server', 'Instance', 'Ip', 'Port', 'Os')
InventoryTree.column("Server", minwidth=0,width=125)
InventoryTree.heading("Server", text="SERVER",)
InventoryTree.column("Instance", minwidth=0,width=140)
InventoryTree.heading("Instance", text="INSTANCE",)
InventoryTree.column("Ip", minwidth=0,width=80)
InventoryTree.heading("Ip", text="IP",)
InventoryTree.column("Port", minwidth=0,width=40)
InventoryTree.heading("Port", text="PORT",)
InventoryTree.column("Os", minwidth=0,width=65)
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

VersionTree1=ttk.Treeview(versionframe,show='headings',height=1,)
VersionTree1.grid(row=0,column=0,padx=5, pady=5,sticky="w",) #rowspan=2,columnspan=2,
VersionTree1['columns'] = ('Result',)
VersionTree1['displaycolumns'] = ('Result')
VersionTree1.column("Result", minwidth=0,width=515,anchor='w')
VersionTree1.heading("Result", text="VERSION SUPPORTED", )

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
serverNbTab11=Frame(serverNb)
serverNbTab12=Frame(serverNb)

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

AlertsButton = ttk.Button(serverNbTab5, text='Install', underline = 0, command= lambda: get_alerts_command(ConnMode.get()))
AlertsButton.grid(row=0, column=3, sticky="w", padx=5, pady=5,)
AlertsButton.config(state=DISABLED)

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
#--AgentXps
serverNbTab6Tree1=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree1.grid(row=0,column=0,padx=5, pady=5, sticky='n')
serverNbTab6Tree1['columns'] = ('AgentXPs')
serverNbTab6Tree1['displaycolumns'] = ('AgentXPs')
serverNbTab6Tree1.heading("AgentXPs", text="Agent XPs")
serverNbTab6Tree1.column("AgentXPs", minwidth=0,width=145,anchor="center")

#--Agent Status
serverNbTab6Tree2=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree2.grid(row=0,column=1,padx=5, pady=5, sticky='n')
serverNbTab6Tree2['columns'] = ('SQLAgentStatus')
serverNbTab6Tree2['displaycolumns'] = ('SQLAgentStatus')
serverNbTab6Tree2.heading("SQLAgentStatus", text="SQL Agent Status")
serverNbTab6Tree2.column("SQLAgentStatus", minwidth=0,width=145,anchor="center")

#--Mail Xps
serverNbTab6Tree3=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree3.grid(row=0,column=2,padx=5, pady=5, sticky='n')
serverNbTab6Tree3['columns'] = ('DatabaseMailXPs')
serverNbTab6Tree3['displaycolumns'] = ('DatabaseMailXPs')
serverNbTab6Tree3.heading("DatabaseMailXPs", text="Database Mail XPs")
serverNbTab6Tree3.column("DatabaseMailXPs", minwidth=0,width=145,anchor="center")

#--Mail Profile
serverNbTab6Tree4=ttk.Treeview(serverNbTab6,show='headings',height=2, )
serverNbTab6Tree4.grid(row=0,column=3,padx=5, pady=5, )
serverNbTab6Tree4['columns'] = ('MailProfile')
serverNbTab6Tree4['displaycolumns'] = ('MailProfile')
serverNbTab6Tree4.heading("MailProfile", text="Mail Profile")
serverNbTab6Tree4.column("MailProfile", minwidth=0,width=145,anchor="center")

mailButton = ttk.Button(serverNbTab6, text='Install', underline = 0, command= lambda: get_mail_command(ConnMode.get()))
mailButton.grid(row=0, column=4, sticky="w", padx=5, pady=5,)
mailButton.config(state=DISABLED)

#--Mail Account
serverNbTab6Tree5=ttk.Treeview(serverNbTab6,show='headings',height=2, )
serverNbTab6Tree5.grid(row=1,column=0,padx=5, pady=5, )
serverNbTab6Tree5['columns'] = ('MailAccount')
serverNbTab6Tree5['displaycolumns'] = ('MailAccount')
serverNbTab6Tree5.heading("MailAccount", text="Mail Account")
serverNbTab6Tree5.column("MailAccount", minwidth=0,width=145,anchor="center")

#--Agent Mail
serverNbTab6Tree6=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree6.grid(row=1,column=1,padx=5, pady=5, sticky='n')
serverNbTab6Tree6['columns'] = ('SQLAgentMailEnabled')
serverNbTab6Tree6['displaycolumns'] = ('SQLAgentMailEnabled')
serverNbTab6Tree6.heading("SQLAgentMailEnabled", text="SQL Agent Mail")
serverNbTab6Tree6.column("SQLAgentMailEnabled", minwidth=0,width=145,anchor="center")

#--Agent Mail Profile
serverNbTab6Tree7=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree7.grid(row=1,column=2,padx=5, pady=5, sticky='n')
serverNbTab6Tree7['columns'] = ('SQLAgentMailProfileEnabled')
serverNbTab6Tree7['displaycolumns'] = ('SQLAgentMailProfileEnabled')
serverNbTab6Tree7.heading("SQLAgentMailProfileEnabled", \
                          text="SQL Agent Mail Profile")
serverNbTab6Tree7.column("SQLAgentMailProfileEnabled", minwidth=0,width=145,anchor="center")

#--Retry
serverNbTab6Tree8=ttk.Treeview(serverNbTab6,show='headings',height=1, )
serverNbTab6Tree8.grid(row=1,column=3,padx=5, pady=5, sticky='n')
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
serverNbTab7Tree2.grid(row=1,column=0,padx=5, pady=5, sticky='w', rowspan=2)
serverNbTab7Tree2['columns'] = ('Name','Desc','Status',)
serverNbTab7Tree2['displaycolumns'] = ('Name','Desc','Status',)
serverNbTab7Tree2.heading("Name", text="NAME")
serverNbTab7Tree2.column("Name", minwidth=0,width=245)
serverNbTab7Tree2.heading("Desc", text="DESC")
serverNbTab7Tree2.column("Desc", minwidth=0,width=350)
serverNbTab7Tree2.heading("Status", text="STATUS")
serverNbTab7Tree2.column("Status", minwidth=0,width=55)

#--IFI Status
serverNbTab7Tree3=ttk.Treeview(serverNbTab7,show='headings',height=2, )
serverNbTab7Tree3.grid(row=1,column=1,padx=5, pady=5, sticky='n')
serverNbTab7Tree3['columns'] = ('IFIStatus',)
serverNbTab7Tree3['displaycolumns'] = ('IFIStatus',)
serverNbTab7Tree3.heading("IFIStatus", text="IFI Status")
serverNbTab7Tree3.column("IFIStatus", minwidth=0,width=145, anchor="center")

genchkButton = ttk.Button(serverNbTab7, text='Set Configurations', underline = 0, command= lambda: get_genchk_command(ConnMode.get()))
genchkButton.grid(row=4, column=1, sticky="n,e", padx=5, pady=5,)
genchkButton.config(state=DISABLED)

ifiButton = ttk.Button(serverNbTab7, text='Test IFI', underline = 0, command= lambda: get_ifitest_command(ConnMode.get()))
ifiButton.grid(row=2, column=1, sticky="e", padx=5, pady=5,)
ifiButton.config(state=DISABLED)

#--PENDING CONFIGURATIONS.
GenCheckLabel=ttk.Label(serverNbTab7,text="Pending Configurations")
GenCheckLabel.grid(row=3,column=0,padx=5, pady=5, sticky='w')

serverNbTab7Tree1=ttk.Treeview(serverNbTab7,show='headings',height=4, )
serverNbTab7Tree1.grid(row=4,column=0,padx=5, pady=5, columnspan=2, sticky='w')
serverNbTab7Tree1['columns'] = ('Name','Desc','Value','ValueInUse',)
serverNbTab7Tree1['displaycolumns'] = ('Name','Desc','Value','ValueInUse',)
serverNbTab7Tree1.heading("Name", text="NAME")
serverNbTab7Tree1.column("Name", minwidth=0,width=245)
serverNbTab7Tree1.heading("Desc", text="DESC")
serverNbTab7Tree1.column("Desc", minwidth=0,width=255)
serverNbTab7Tree1.heading("Value", text="VALUE")
serverNbTab7Tree1.column("Value", minwidth=0,width=75)
serverNbTab7Tree1.heading("ValueInUse", text="VINUSE")
serverNbTab7Tree1.column("ValueInUse", minwidth=0,width=75)

#--#Databases Tab
#--Databases
serverNbTab8Tree1=ttk.Treeview(serverNbTab8,show='headings',height=12, )
serverNbTab8Tree1.grid(row=0,column=0,padx=5, pady=5, )
serverNbTab8Tree1['columns'] = ('Id','Name','LastBackup','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab8Tree1['displaycolumns'] = ('Id','Name','LastBackup','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab8Tree1.heading("Id", text="ID")
serverNbTab8Tree1.column("Id", minwidth=0,width=25,anchor="w")
serverNbTab8Tree1.heading("Name", text="NAME")
serverNbTab8Tree1.column("Name", minwidth=0,width=160,anchor="w")
serverNbTab8Tree1.heading("LastBackup", text="LAST BKP")
serverNbTab8Tree1.column("LastBackup", minwidth=0,width=80,anchor="w")
serverNbTab8Tree1.heading("Owner", text="OWNER")
serverNbTab8Tree1.column("Owner", minwidth=0,width=50,anchor="w")
serverNbTab8Tree1.heading("Creation", text="CREATION")
serverNbTab8Tree1.column("Creation", minwidth=0,width=75,anchor="w")
serverNbTab8Tree1.heading("Compat", text="COM")
serverNbTab8Tree1.column("Compat", minwidth=0,width=35,anchor="w")
serverNbTab8Tree1.heading("Status", text="STATUS")
serverNbTab8Tree1.column("Status", minwidth=0,width=60,anchor="w")
serverNbTab8Tree1.heading("Recovery", text="RECOVER")
serverNbTab8Tree1.column("Recovery", minwidth=0,width=60,anchor="w")
serverNbTab8Tree1.heading("Verification", text="VERIFICATION")
serverNbTab8Tree1.column("Verification", minwidth=0,width=85,anchor="w")
serverNbTab8Tree1.heading("LRWait", text="LRWAIT")
serverNbTab8Tree1.column("LRWait", minwidth=0,width=80,anchor="w")

saButton = ttk.Button(serverNbTab8, text='sa owner', underline = 0, command= lambda: get_sa_command(ConnMode.get()))
saButton.grid(row=0, column=1, sticky="n", padx=5, pady=5,)
saButton.config(state=DISABLED)

#--#Transaction Log Tab
#--Transaction Log Usage
serverNbTab12Tree1=ttk.Treeview(serverNbTab12,show='headings',height=12, )
serverNbTab12Tree1.grid(row=0,column=0,padx=5, pady=5, )
serverNbTab12Tree1['columns'] = ('Database','LogSizeMB','LogSpaceUsed','Status',)
serverNbTab12Tree1['displaycolumns'] = ('Database','LogSizeMB','LogSpaceUsed','Status')
serverNbTab12Tree1.heading("Database", text="DATABASE")
serverNbTab12Tree1.column("Database", minwidth=0,width=160,anchor="w")
serverNbTab12Tree1.heading("LogSizeMB", text="LOG SIZE MB")
serverNbTab12Tree1.column("LogSizeMB", minwidth=0,width=100,anchor="w")
serverNbTab12Tree1.heading("LogSpaceUsed", text="LOG SPACE USED %")
serverNbTab12Tree1.column("LogSpaceUsed", minwidth=0,width=125,anchor="w")
serverNbTab12Tree1.heading("Status", text="STATUS")
serverNbTab12Tree1.column("Status", minwidth=0,width=75,anchor="w")

#--VLF
serverNbTab12Tree2=ttk.Treeview(serverNbTab12,show='headings',height=12, )
serverNbTab12Tree2.grid(row=0,column=2,padx=5, pady=5, )
serverNbTab12Tree2['columns'] = ('Database','Vlfs',)
serverNbTab12Tree2['displaycolumns'] = ('Database','Vlfs',)
serverNbTab12Tree2.heading("Database", text="DATABASE")
serverNbTab12Tree2.column("Database", minwidth=0,width=160,anchor="w")
serverNbTab12Tree2.heading("Vlfs", text="VLFs")
serverNbTab12Tree2.column("Vlfs", minwidth=0,width=100,anchor="w")

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

DBAdminButton = ttk.Button(serverNbTab9, text='Install', underline = 0, command= lambda: get_dbadmin_command(ConnMode.get()))
DBAdminButton.grid(row=0, column=1, sticky="w", padx=5, pady=5,)
DBAdminButton.config(state=DISABLED)

serverNbTab9Tree1=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree1.grid(row=1,column=0,padx=5, pady=5,columnspan=4 )
serverNbTab9Tree1['columns'] = ('Id','Name','LastBackup','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab9Tree1['displaycolumns'] = ('Id','Name','LastBackup','Owner','Creation','Compat','Status','Recovery','Verification','LRWait',)
serverNbTab9Tree1.heading("Id", text="ID")
serverNbTab9Tree1.column("Id", minwidth=0,width=25,anchor="w")
serverNbTab9Tree1.heading("Name", text="NAME")
serverNbTab9Tree1.column("Name", minwidth=0,width=160,anchor="w")
serverNbTab9Tree1.heading("LastBackup", text="LAST BKP")
serverNbTab9Tree1.column("LastBackup", minwidth=0,width=100,anchor="w")
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
serverNbTab9Tree1.column("LRWait", minwidth=0,width=115,anchor="w")

#--Service Restart Notification Job
labelService=ttk.Label(serverNbTab9,text="Service Restart Notification Job")
labelService.grid(row=2,column=0,padx=5, pady=5, sticky='w')

ServiceButton = ttk.Button(serverNbTab9, text='Install', underline = 0, command= lambda: get_servicerestart_command(ConnMode.get()))
ServiceButton.grid(row=2, column=1, sticky="w", padx=5, pady=5,)
ServiceButton.config(state=DISABLED)

serverNbTab9Tree2=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree2.grid(row=3,column=0,padx=5, pady=5, sticky='w',columnspan=2)
serverNbTab9Tree2['columns'] = ('Name','Owner','Status','Desc',)
serverNbTab9Tree2['displaycolumns'] = ('Name','Owner','Status','Desc',)
serverNbTab9Tree2.heading("Name", text="NAME")
serverNbTab9Tree2.column("Name", minwidth=0,width=150,anchor="w")
serverNbTab9Tree2.heading("Owner", text="OWNER")
serverNbTab9Tree2.column("Owner", minwidth=0,width=50,anchor="w")
serverNbTab9Tree2.heading("Status", text="STATUS")
serverNbTab9Tree2.column("Status", minwidth=0,width=55,anchor="center")
serverNbTab9Tree2.heading("Desc", text="DESC")
serverNbTab9Tree2.column("Desc", minwidth=0,width=175,anchor="w")

#--sp_whoisactive
labelsp=ttk.Label(serverNbTab9,text="sp_whoisactive")
labelsp.grid(row=2,column=2,padx=5, pady=5, sticky='w')

spButton = ttk.Button(serverNbTab9, text='Install', underline = 0, command= lambda: get_spwhoisactive_command(ConnMode.get()))
spButton.grid(row=2, column=2, sticky="e,n", padx=5, pady=5,)
spButton.config(state=DISABLED)

serverNbTab9Tree3=ttk.Treeview(serverNbTab9,show='headings',height=1, )
serverNbTab9Tree3.grid(row=3,column=2,padx=5, pady=5, sticky='w',columnspan=2)
serverNbTab9Tree3['columns'] = ('Name','Info',)
serverNbTab9Tree3['displaycolumns'] = ('Name','Info',)
serverNbTab9Tree3.heading("Name", text="NAME")
serverNbTab9Tree3.column("Name", minwidth=0,width=200,anchor="w")
serverNbTab9Tree3.heading("Info", text="INFO")
serverNbTab9Tree3.column("Info", minwidth=0,width=50,anchor="w")

#--Standard Processes Logins
labelStandardLogins=ttk.Label(serverNbTab9,text="Standard Processes Logins")
labelStandardLogins.grid(row=4,column=0,padx=5, pady=5, sticky='w')

StandardLoginsButton = ttk.Button(serverNbTab9, text='Install', underline = 0, command= lambda: get_logins_command(ConnMode.get()))
StandardLoginsButton.grid(row=4, column=1, sticky="w", padx=5, pady=5,)
StandardLoginsButton.config(state=DISABLED)

serverNbTab9Tree4=ttk.Treeview(serverNbTab9,show='headings',height=3, )
serverNbTab9Tree4.grid(row=5,column=0,padx=5, pady=5,columnspan=4,sticky='w' )
serverNbTab9Tree4['columns'] = ('Name','Type','Status','Creation','Db',)
serverNbTab9Tree4['displaycolumns'] = ('Name','Type','Status','Creation','Db',)
serverNbTab9Tree4.heading("Name", text="NAME")
serverNbTab9Tree4.column("Name", minwidth=0,width=250, )
serverNbTab9Tree4.heading("Type", text="TYPE")
serverNbTab9Tree4.column("Type", minwidth=0,width=145, )
serverNbTab9Tree4.heading("Status", text="STATUS")
serverNbTab9Tree4.column("Status", minwidth=0,width=145, )
serverNbTab9Tree4.heading("Creation", text="CREATION")
serverNbTab9Tree4.column("Creation", minwidth=0,width=145, )
serverNbTab9Tree4.heading("Db", text="DB")
serverNbTab9Tree4.column("Db", minwidth=0,width=145, )

#Bottoms
#LoginsButton = ttk.Button(serverNbTab9, text='Install', underline = 0, command= lambda: get_logins_command(ConnMode.get()))
#LoginsButton.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#Adding all Tabs to the Notebook
serverNb.add(serverNbTab1, text='Services',)
serverNb.add(serverNbTab2, text='Disks',)
serverNb.add(serverNbTab3, text='Page File',)
serverNb.add(serverNbTab4, text='Default Paths',)
serverNb.add(serverNbTab6, text='DBMail',)
serverNb.add(serverNbTab5, text='Alerts',)
serverNb.add(serverNbTab8, text='Databases',)
serverNb.add(serverNbTab12, text='Transaction Log',)
serverNb.add(serverNbTab10, text='Sysadmins',)
serverNb.add(serverNbTab7, text='General Check',)
serverNb.add(serverNbTab9, text='DBA Tools',)
serverNb.add(serverNbTab11, text='Other Options',)

inventoryframe['borderwidth'] = 2
inventoryframe['relief'] = 'groove'
detailframe['borderwidth'] = 2
detailframe['relief'] = 'groove'

window.mainloop()