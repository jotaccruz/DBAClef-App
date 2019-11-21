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

window=Tk()

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


def basic_analyze_command():
    return


def view_command():
    for i in InventoryTree.get_children():
        InventoryTree.delete(i)
    
    query="SELECT srv_name as SERVER, srv_user as USER, SRV_PWD as PWD"\
            " FROM lgm_servers WHERE"+ \
            " srv_name in"+\
            " ('SCAEDYAK02','SUSWEYAK05');"
    #query="SELECT srv_name as SERVER, srv_ip as IP, srv_os as OS,"\
    #       "srv_type as ENGINE, srv_location as LOCATION, srv_domain "\
    #        "as DOMAIN FROM lgm_servers WHERE"+ \
    #        " srv_location = 'GCP' and srv_active=1 and srv_name in"+\
    #        " ('SUSWEYAK03','SUSWEYAK05');"
    for row in dbservers(query):
        InventoryTree.insert("", END, values=(row[0],row[1],row[2]))

def get_selected_command(event):
    return

def get_detail_command():
    try:
        global selected_row
        selected_row=InventoryTree.set(InventoryTree.selection())
    except IndexError:
        pass

#### Tab Detail
    sqlexec="SELECT @@SERVERNAME as SERVER,'192.168.0.1' as IP,'Windows'"+\
    " as OS FROM sys.dm_exec_requests"

    for i in serverNbTab1Tree1.get_children():
        serverNbTab1Tree1.delete(i)
        
    for row in mssqldetail(selected_row['Server'],"master",\
                           selected_row['User'],selected_row['Pwd'],sqlexec):
        serverNbTab1Tree1.insert("", END, values=(row[0],row[1],row[2]))
    
#### Tab Disks
    for i in serverNbTab2Tree1.get_children():
        serverNbTab2Tree1.delete(i)
        
    for row in diskinfo(selected_row['Server']):
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

    serverNbTab2Tree1.tag_configure('need', background='red')

#### Tab Page File
    for i in serverNbTab3Tree1.get_children():
        serverNbTab3Tree1.delete(i)
        
    for row in pageinfo(selected_row['Server']):
        serverNbTab3Tree1.insert("", END, values=(row['SystemName'],\
                                                      row['Automatic'],\
                                                      row['Caption'],\
                                                      row['Status'],\
                                                      row['CurrentUsage'],\
                                                      row['PeakUsage'],\
                                                      row['InitialSize'],\
                                                      row['MaximunSize']),\
        tags = ('good',))

    serverNbTab3Tree1.tag_configure('need', background='red')

#### Tab Default Paths
    sqlexec1="CREATE TABLE #DPaths(Type nvarchar(50),Location sql_variant, \
    Restart integer);CREATE TABLE #RDPaths(Type nvarchar(50),\
        Location sql_variant);EXECUTE dbo.get_defaultpathdb;"
        
    sqlexec2="CREATE TABLE #DPath(Type nvarchar(50),Location nvarchar(250),\
    Restart integer);INSERT INTO #DPath(Type,Location,Restart) SELECT Type,\
        CONVERT(NVARCHAR,Location),Restart FROM #DPaths;INSERT INTO \
        #DPath(Type,Location) SELECT Type,CONVERT(NVARCHAR,Location) \
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
    serverNbTab4Tree1.tag_configure('need', background='red')
    
####### main------------------------------------------------------------------
    
menubar = Menu(window)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="0 Server List", command=view_command)
filemenu.add_command(label="1 Default path", command=hello)
filemenu.add_command(label="2 DBAdmin", command=hello)
filemenu.add_command(label="3 DBMail", command=hello)
filemenu.add_command(label="4 Alerts", command=hello)
filemenu.add_command(label="5 sp_whoisactive", command=hello)
filemenu.add_command(label="6 ServerName", command=hello)
filemenu.add_command(label="7 DatabaseOwner", command=hello)
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
inventoryframe = ttk.Frame(window, width=600, height=512)
inventoryframe.grid(row=0,column=0,padx=5, pady=5)

#Labels controls
l1=ttk.Label(inventoryframe,text="Server",width=35)
l1.grid(row=0,column=0)

#Text Controls
server_text=StringVar()
e1=ttk.Entry(inventoryframe,textvariable=server_text,width=39)
e1.grid(row=0,column=1)

#Bottom Controls
DetailButton = Button(inventoryframe, text='Details', underline = 0, \
                      command=get_detail_command)
DetailButton.grid(column=2, row=0, sticky="e", padx=5, pady=5)

ScanButton = Button(inventoryframe, text='Scan', underline = 0, \
                      command=get_detail_command)
ScanButton.grid(column=2, row=2, sticky="s", padx=5, pady=5)

ExitButton = Button(inventoryframe, text='Exit', underline = 0, \
                      command=window.destroy)
ExitButton.grid(column=2, row=3, sticky="s", padx=5, pady=5)

#TreeView Controls
InventoryTree=ttk.Treeview(inventoryframe,show='headings')
InventoryTree.grid(row=2,column=0,padx=5, pady=5,rowspan=6,columnspan=2)
InventoryTree['columns'] = ('Server', 'User', 'Pwd')
InventoryTree['displaycolumns'] = ('Server')
InventoryTree.heading("Server", text="SERVER")
InventoryTree.heading("User", text="USER")
InventoryTree.heading("Pwd", text="PWD")

InventoryTree.bind('<Double-Button-1>',lambda x: DetailButton.invoke())

detailframe = Frame(window, width=600, height=600)
detailframe.grid(row=2,column=0,padx=5, pady=5)

serverNb=ttk.Notebook(detailframe)
serverNb.grid(row=0,column=0, sticky="e")

serverNbTab1=Frame(serverNb)
serverNbTab2=Frame(serverNb)
serverNbTab3=Frame(serverNb)
serverNbTab4=Frame(serverNb)
serverNbTab5=Frame(serverNb)
serverNbTab6=Frame(serverNb)

#General Status Tab
serverNbTab1Tree1=ttk.Treeview(serverNbTab1,show='headings')
serverNbTab1Tree1.grid(row=0,column=0,padx=5, pady=5)
serverNbTab1Tree1['columns'] = ('Server', 'Ip', 'Os')
serverNbTab1Tree1.heading("Server", text="SERVER")
serverNbTab1Tree1.column("Server", minwidth=0,width=100)
serverNbTab1Tree1.heading("Ip", text="IP")
serverNbTab1Tree1.column("Ip", minwidth=0,width=100)
serverNbTab1Tree1.heading("Os", text="OS")
serverNbTab1Tree1.column("Os", minwidth=0,width=100)

#Disks Tab
serverNbTab2Tree1=ttk.Treeview(serverNbTab2,show='headings')
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
                 'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximunSize')
serverNbTab3Tree1['displaycolumns'] = ('SName', 'Automatic', 'Caption','Status'
                 ,'CurrentUsage', 'PeakUsage', 'InitialSize', 'MaximunSize')
serverNbTab3Tree1.heading("SName", text="SERVER")
serverNbTab3Tree1.column("SName", minwidth=0,width=150)
serverNbTab3Tree1.heading("Automatic", text="AUTO")
serverNbTab3Tree1.column("Automatic", minwidth=0,width=50)
serverNbTab3Tree1.heading("Caption", text="FNAME")
serverNbTab3Tree1.column("Caption", minwidth=0,width=75)
serverNbTab3Tree1.heading("Status", text="STATUS")
serverNbTab3Tree1.column("Status", minwidth=0,width=75)
serverNbTab3Tree1.heading("CurrentUsage", text="CUSAGE GB")
serverNbTab3Tree1.column("CurrentUsage", minwidth=0,width=150)
serverNbTab3Tree1.heading("PeakUsage", text="PUSAGE GB")
serverNbTab3Tree1.column("PeakUsage", minwidth=0,width=100)
serverNbTab3Tree1.heading("InitialSize", text="ISIZE GB")
serverNbTab3Tree1.column("InitialSize", minwidth=0,width=75)
serverNbTab3Tree1.heading("MaximunSize", text="MSIZE GB")
serverNbTab3Tree1.column("MaximunSize", minwidth=0,width=75)

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

serverNb.add(serverNbTab1, text='Status',)
serverNb.add(serverNbTab2, text='Disks',)
serverNb.add(serverNbTab3, text='Page File',)
serverNb.add(serverNbTab4, text='Default Paths',)
serverNb.add(serverNbTab5, text='Alerts',)
serverNb.add(serverNbTab6, text='DBMail',)


inventoryframe['borderwidth'] = 2
inventoryframe['relief'] = 'groove'
detailframe['borderwidth'] = 2
detailframe['relief'] = 'groove'

window.mainloop()