import tkinter
from tkinter import *
from tkinter import ttk
import moldmydbInventoryBackend
from moldmydbInventoryBackend import *

mysqlserver='172.25.20.17'#ip.get()
mysqlusername='ISJCruz'#user.get()
mysqlpsw='T3lu52018!'#pas.get()

def get_selected_row():
    try:
        global selected_row
        selected_row=InventoryTree.set(InventoryTree.selection())
        #print (type(selected_row))
        #print (selected_row)
        srv_nameInput.delete(0,END)
        srv_nameInput.insert(END,selected_row['srv_name'])
        srv_instanceInput.delete(0,END)
        srv_instanceInput.insert(END,selected_row['srv_instance'])
        srv_ins_portInput.delete(0,END)
        srv_ins_portInput.insert(END,selected_row['srv_ins_port'])
        srv_ip1Input.delete(0,END)
        srv_ip1Input.insert(END,selected_row['srv_ip1'])
        srv_ip2Input.delete(0,END)
        srv_ip2Input.insert(END,selected_row['srv_ip2'])
        srv_userInput.delete(0,END)
        srv_userInput.insert(END,selected_row['srv_user'])
        srv_pwdInput.delete(0,END)
        srv_pwdInput.insert(END,'')
        srv_directoryInput.delete(0,END)
        srv_directoryInput.insert(END,selected_row['srv_directory'])
        srv_osInput.delete(0,END)
        srv_osInput.current(int(selected_row['srv_os']))
        srv_frecuencyInput.delete(0,END)
        srv_frecuencyInput.current(int(selected_row['srv_frecuency']))
        srv_bk_locationInput.delete(0,END)
        srv_bk_locationInput.insert(END,selected_row['srv_bk_location'])
        srv_typeInput.delete(0,END)
        srv_typeInput.current(int(selected_row['srv_type']))
        srv_domainInput.delete(0,END)
        srv_domainInput.insert(END,selected_row['srv_domain'])
        #srv_activeInput.delete(0,END)
        srv_activeInput.current(int(selected_row['srv_active']))
        srv_created_dtInput.delete(0,END)
        srv_created_dtInput.insert(END,selected_row['srv_created_dt'])
        srv_updated_dtInput.delete(0,END)
        srv_updated_dtInput.insert(END,selected_row['srv_updated_dt'])

    except IndexError:
        pass

def view_command():
    for i in InventoryTree.get_children():
        InventoryTree.delete(i)
    for row in view():
        InventoryTree.insert("", END, values=(row[0],row[1],row[2],row[3],\
        row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],\
        row[13],row[14],row[16],row[17],row[15],row[18]))

def search_command():
    InventoryTree.delete(0,END)
    for row in search(title_text.get(),author_text.get(),year_text.get() \
                      ,isbn_text.get()):
        InventoryTree.insert(END,row)

def add_command():
    sqlexec ="INSERT INTO lgm_servers (srv_name,srv_instance,srv_ins_port,\
    srv_ip1, srv_ip2,srv_user,srv_pwd,srv_directory,srv_os,srv_frecuency,\
    srv_bk_location,srv_type,srv_location,srv_domain,srv_active,srv_created_dt,\
    srv_updated_dt)\
    VALUES("+"'"+srv_nameInput.get()+"','"+srv_instanceInput.get()+"','"+srv_ins_portInput.get()+"','"+\
    srv_ip1Input.get()+"','"+srv_ip2Input.get()+"','"+srv_userInput.get()+"','"+srv_pwdInput.get()+"','"+\
    srv_directoryInput.get()+"','"+str(srv_osInput.current())+"','"+srv_frecuencyInput.get()+"','"+\
    srv_bk_locationInput.get()+"','"+str(srv_typeInput.current())+"','"+str(srv_locationInput.current())+"','"+\
    srv_domainInput.get()+"','"+str(srv_activeInput.current())+"','"+srv_created_dtInput.get()+"','"+\
    srv_updated_dtInput.get()+"')"
    #print (sqlexec)
    dbserversCreate(sqlexec,mysqlserver,mysqlusername,mysqlpsw)
    view_command()

#lambda function replace this code
#def delete_command():
#    delete(selected_row[0])
#    view_command()

def update_command():
    update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),\
           isbn_text.get())
    InventoryTree.delete(0,END)
    view_command()

def close_command():
    return

InventoryFeed=Tk()
InventoryFeed.wm_title("Server Inventory")


InventoryFrameInput = ttk.LabelFrame(InventoryFeed, width=250, height=200,text="Servers")
InventoryFrameInput.grid(row=0,column=0,padx=5, pady=5, rowspan=2)

#Labels controls
l1=Label(InventoryFrameInput,text="1. Server Name")
l1.grid(row=0,column=0,sticky='w',padx=5, pady=5,)

l2=Label(InventoryFrameInput,text="2. Server Instance Name")
l2.grid(row=0,column=2,sticky='w',padx=5, pady=5,)

l3=Label(InventoryFrameInput,text="3. Server Instance port")
l3.grid(row=0,column=4,sticky='w',padx=5, pady=5,)

l4=Label(InventoryFrameInput,text="4. Ip Address 1")
l4.grid(row=1,column=0,sticky='w',padx=5, pady=5,)

l1=Label(InventoryFrameInput,text="5. Ip Address 2")
l1.grid(row=1,column=2,sticky='w',padx=5, pady=5,)

l2=Label(InventoryFrameInput,text="6. User Name")
l2.grid(row=1,column=4,sticky='w',padx=5, pady=5,)

l3=Label(InventoryFrameInput,text="7. Password")
l3.grid(row=2,column=0,sticky='w',padx=5, pady=5,)

l4=Label(InventoryFrameInput,text="8. Server directory")
l4.grid(row=2,column=2,sticky='w',padx=5, pady=5,)

l1=Label(InventoryFrameInput,text="9. Server OS")
l1.grid(row=2,column=4,sticky='w',padx=5, pady=5,)

l2=Label(InventoryFrameInput,text="10. Frecuency")
l2.grid(row=3,column=0,sticky='w',padx=5, pady=5,)

l3=Label(InventoryFrameInput,text="11. Backup Location")
l3.grid(row=3,column=2,sticky='w',padx=5, pady=5,)

l4=Label(InventoryFrameInput,text="12. Server Type")
l4.grid(row=3,column=4,sticky='w',padx=5, pady=5,)

l1=Label(InventoryFrameInput,text="13. Server Location")
l1.grid(row=4,column=0,sticky='w',padx=5, pady=5,)

l2=Label(InventoryFrameInput,text="14. Server Domain")
l2.grid(row=4,column=2,sticky='w',padx=5, pady=5,)

l3=Label(InventoryFrameInput,text="15. Status")
l3.grid(row=4,column=4,sticky='w',padx=5, pady=5,)

l4=Label(InventoryFrameInput,text="16. Created")
l4.grid(row=5,column=0,sticky='w',padx=5, pady=5,)

l1=Label(InventoryFrameInput,text="17. Updated")
l1.grid(row=5,column=2,sticky='w',padx=5, pady=5,)

#Text Controls
srv_name=StringVar()
srv_nameInput=ttk.Entry(InventoryFrameInput,textvariable=srv_name)
srv_nameInput.grid(row=0,column=1,padx=5, pady=5,sticky='w')

srv_instance=StringVar()
srv_instanceInput=ttk.Entry(InventoryFrameInput,textvariable=srv_instance)
srv_instanceInput.grid(row=0,column=3,padx=5, pady=5,sticky='w')

srv_ins_port=StringVar()
srv_ins_portInput=ttk.Entry(InventoryFrameInput,textvariable=srv_ins_port)
srv_ins_portInput.grid(row=0,column=5,padx=5, pady=5,sticky='w')


srv_ip1=StringVar()
srv_ip1Input=ttk.Entry(InventoryFrameInput,textvariable=srv_ip1)
srv_ip1Input.grid(row=1,column=1,padx=5, pady=5,sticky='w')

srv_ip2=StringVar()
srv_ip2Input=ttk.Entry(InventoryFrameInput,textvariable=srv_ip2)
srv_ip2Input.grid(row=1,column=3,padx=5, pady=5,sticky='w')

srv_user=StringVar()
srv_userInput=ttk.Entry(InventoryFrameInput,textvariable=srv_user)
srv_userInput.grid(row=1,column=5,padx=5, pady=5,sticky='w')

srv_pwd=StringVar()
srv_pwdInput=ttk.Entry(InventoryFrameInput,textvariable=srv_pwd,show='*')
srv_pwdInput.grid(row=2,column=1,padx=5, pady=5,sticky='w')

srv_directory=StringVar()
srv_directoryInput=ttk.Entry(InventoryFrameInput,textvariable=srv_directory)
srv_directoryInput.grid(row=2,column=3,padx=5, pady=5,sticky='w')

srv_os=StringVar()
srv_osInput=ttk.Combobox(InventoryFrameInput,values=['Linux','Windows','N/A'],state='readonly')
srv_osInput.grid(row=2,column=5,padx=5, pady=5,sticky='w')
srv_osInput.current(0)

srv_frecuency=StringVar()
srv_frecuencyInput=ttk.Combobox(InventoryFrameInput,values=['Daily','Monday','Monthly','Saturday','Sunday'],state='readonly')
srv_frecuencyInput.grid(row=3,column=1,padx=5, pady=5,sticky='w')
srv_frecuencyInput.current(0)

srv_bk_location=StringVar()
srv_bk_locationInput=ttk.Entry(InventoryFrameInput,textvariable=srv_bk_location)
srv_bk_locationInput.grid(row=3,column=3,padx=5, pady=5,sticky='w')

srv_type=StringVar()
srv_typeInput=ttk.Combobox(InventoryFrameInput,values=['MSSQL','MySQL','Oracle','PostgreSQL','Sybase'],state='readonly')
srv_typeInput.grid(row=3,column=5,padx=5, pady=5,sticky='w')
srv_typeInput.current(0)

srv_location=StringVar()
srv_locationInput=ttk.Combobox(InventoryFrameInput,values=['GCP','OnPrem'],state='readonly')
srv_locationInput.grid(row=4,column=1,padx=5, pady=5,sticky='w')

srv_domain=StringVar()
srv_domainInput=ttk.Entry(InventoryFrameInput,textvariable=srv_domain)
srv_domainInput.grid(row=4,column=3,padx=5, pady=5,sticky='w')

srv_active=StringVar()
srv_activeInput=ttk.Combobox(InventoryFrameInput,values=['Inactive','Active'],state='readonly')
srv_activeInput.grid(row=4,column=5,padx=5, pady=5,sticky='w')
srv_activeInput.current(0)

srv_created_dt=StringVar()
srv_created_dtInput=ttk.Entry(InventoryFrameInput,textvariable=srv_created_dt)
srv_created_dtInput.grid(row=5,column=1,padx=5, pady=5,sticky='w')

srv_updated_dt=StringVar()
srv_updated_dtInput=ttk.Entry(InventoryFrameInput,textvariable=srv_updated_dt)
srv_updated_dtInput.grid(row=5,column=3,padx=5, pady=5,sticky='w')

srv_created_dtInput.config(state=DISABLED)
srv_updated_dtInput.config(state=DISABLED)

#Listbox Controls

InventoryTree=ttk.Treeview(InventoryFrameInput,show='headings',height=7)
InventoryTree.grid(row=8,column=0,columnspan=7,padx=5, pady=5,)
InventoryTree['columns'] = ('No','srv_name','srv_instance','srv_ins_port',\
'srv_ip1','srv_ip2','srv_user','srv_pwd','srv_directory','srv_os',\
'srv_frecuency','srv_bk_location','srv_type','srv_location','srv_domain',\
'srv_active_literal','srv_created_dt','srv_updated_dt','srv_active')
InventoryTree['displaycolumns'] = ('No','srv_name','srv_instance',\
'srv_ins_port','srv_ip1','srv_ip2','srv_user','srv_pwd','srv_directory',\
'srv_os','srv_frecuency','srv_bk_location','srv_type','srv_location',\
'srv_domain','srv_active_literal')
InventoryTree.column("No", minwidth=0,width=25)
InventoryTree.heading("No", text="No",)
InventoryTree.column("srv_name", minwidth=0,width=125)
InventoryTree.heading("srv_name", text="SERVER",)
InventoryTree.column("srv_instance", minwidth=0,width=140)
InventoryTree.heading("srv_instance", text="INSTANCE",)
InventoryTree.column("srv_ins_port", minwidth=0,width=80)
InventoryTree.heading("srv_ins_port", text="PORT",)
InventoryTree.column("srv_ip1", minwidth=0,width=85)
InventoryTree.heading("srv_ip1", text="IP1",)
InventoryTree.column("srv_ip2", minwidth=0,width=85)
InventoryTree.heading("srv_ip2", text="IP2",)
InventoryTree.column("srv_user", minwidth=0,width=65)
InventoryTree.heading("srv_user", text="USER",)
InventoryTree.column("srv_pwd", minwidth=0,width=65)
InventoryTree.heading("srv_pwd", text="PASS",)
InventoryTree.column("srv_directory", minwidth=0,width=65)
InventoryTree.heading("srv_directory", text="DIR",)
InventoryTree.column("srv_os", minwidth=0,width=65)
InventoryTree.heading("srv_os", text="OS",)
InventoryTree.column("srv_frecuency", minwidth=0,width=65)
InventoryTree.heading("srv_frecuency", text="FREQ",)
InventoryTree.column("srv_bk_location", minwidth=0,width=65)
InventoryTree.heading("srv_bk_location", text="BKPLOC",)
InventoryTree.column("srv_type", minwidth=0,width=65)
InventoryTree.heading("srv_type", text="TYPE",)
InventoryTree.column("srv_location", minwidth=0,width=65)
InventoryTree.heading("srv_location", text="SRVLOC",)
InventoryTree.column("srv_domain", minwidth=0,width=65)
InventoryTree.heading("srv_domain", text="SRVDOM",)
InventoryTree.column("srv_active_literal", minwidth=0,width=65)
InventoryTree.heading("srv_active_literal", text="STATUS",)
InventoryTree.column("srv_created_dt", minwidth=0,width=65)
InventoryTree.heading("srv_created_dt", text="CREATED",)
InventoryTree.column("srv_updated_dt", minwidth=0,width=65)
InventoryTree.heading("srv_updated_dt", text="UPDATED",)
InventoryTree.column("srv_active", minwidth=0,width=65)
InventoryTree.heading("srv_active", text="ACTIVE",)

InventoryTree.bind('<Double-Button-1>', lambda x: get_selected_row())

#Scrollbar Controls
scrollbar_vertical = ttk.Scrollbar(InventoryFrameInput, orient="vertical", \
                                   command=InventoryTree.yview)
scrollbar_vertical.grid(row=8, column=7, sticky="ens")
InventoryTree.configure(yscrollcommand=scrollbar_vertical.set)

#Button Controls
b1=Button(InventoryFrameInput,text="View All",width=12,command=view_command)
b1.grid(row=0,column=6,padx=5, pady=5,)

b2=Button(InventoryFrameInput,text="Search ttk.Entry",width=12,command=search_command)
b2.grid(row=1,column=6,padx=5, pady=5,)

b3=Button(InventoryFrameInput,text="Add ttk.Entry",width=12,command=add_command)
b3.grid(row=2,column=6,padx=5, pady=5,)

b4=Button(InventoryFrameInput,text="Update selected",width=12,command=update_command)
b4.grid(row=3,column=6,padx=5, pady=5,)

#b5=Button(InventoryFrameInput,text="Delete selected",width=12,command=delete_command)
b5=Button(InventoryFrameInput,text="Delete selected",width=12,command=lambda InventoryTree=InventoryTree: \
          InventoryTree.delete(ANCHOR))
b5.grid(row=4,column=6,padx=5, pady=5,)

b6=Button(InventoryFrameInput,text="Close",width=12,command=InventoryFrameInput.destroy)
b6.grid(row=5,column=6,padx=5, pady=5,)

InventoryFeed.mainloop()
