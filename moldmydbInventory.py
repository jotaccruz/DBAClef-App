import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import moldmydbSource
from moldmydbSource import *
import moldmydbRSA
from moldmydbRSA import *
from datetime import datetime

class InventoryFeeds():
    selected_row=[]
    mysqlserver=''
    mysqlusername=''
    mysqlpsw=''

    def __init__(self,window,mysqlserver,mysqlusername,mysqlpsw):
        self.window = window
        InventoryFeeds.mysqlserver = mysqlserver
        InventoryFeeds.mysqlusername = mysqlusername
        InventoryFeeds.mysqlpsw = mysqlpsw

        self.InventoryFeed = tk.Toplevel(window)
        self.InventoryFeed.wm_title("Server Inventory")
        self.InventoryFrameInput = ttk.LabelFrame(self.InventoryFeed, width=250, height=200,text="Servers")
        self.InventoryFrameInput.grid(row=0,column=0,padx=5, pady=5, rowspan=2)

        #Labels controls
        self.l1=Label(self.InventoryFrameInput,text="1. Server Name")
        self.l1.grid(row=0,column=0,sticky='w',padx=5, pady=5,)

        self.l2=Label(self.InventoryFrameInput,text="2. Server Instance Name")
        self.l2.grid(row=0,column=2,sticky='w',padx=5, pady=5,)

        self.l3=Label(self.InventoryFrameInput,text="3. Server Instance port")
        self.l3.grid(row=0,column=4,sticky='w',padx=5, pady=5,)

        self.l4=Label(self.InventoryFrameInput,text="4. Ip Address 1")
        self.l4.grid(row=1,column=0,sticky='w',padx=5, pady=5,)

        self.l1=Label(self.InventoryFrameInput,text="5. Ip Address 2")
        self.l1.grid(row=1,column=2,sticky='w',padx=5, pady=5,)

        self.l2=Label(self.InventoryFrameInput,text="6. User Name")
        self.l2.grid(row=1,column=4,sticky='w',padx=5, pady=5,)

        self.l3=Label(self.InventoryFrameInput,text="7. Password")
        self.l3.grid(row=2,column=0,sticky='w',padx=5, pady=5,)

        self.l4=Label(self.InventoryFrameInput,text="8. Server directory")
        self.l4.grid(row=2,column=2,sticky='w',padx=5, pady=5,)

        self.l1=Label(self.InventoryFrameInput,text="9. Server OS")
        self.l1.grid(row=2,column=4,sticky='w',padx=5, pady=5,)

        self.l2=Label(self.InventoryFrameInput,text="10. Frecuency")
        self.l2.grid(row=3,column=0,sticky='w',padx=5, pady=5,)

        self.l3=Label(self.InventoryFrameInput,text="11. Backup Location")
        self.l3.grid(row=3,column=2,sticky='w',padx=5, pady=5,)

        self.l4=Label(self.InventoryFrameInput,text="12. Server Type")
        self.l4.grid(row=3,column=4,sticky='w',padx=5, pady=5,)

        self.l1=Label(self.InventoryFrameInput,text="13. Server Location")
        self.l1.grid(row=4,column=0,sticky='w',padx=5, pady=5,)

        self.l2=Label(self.InventoryFrameInput,text="14. Server Domain")
        self.l2.grid(row=4,column=2,sticky='w',padx=5, pady=5,)

        self.l3=Label(self.InventoryFrameInput,text="15. Status")
        self.l3.grid(row=4,column=4,sticky='w',padx=5, pady=5,)

        self.l4=Label(self.InventoryFrameInput,text="16. Created")
        self.l4.grid(row=5,column=0,sticky='w',padx=5, pady=5,)

        self.l1=Label(self.InventoryFrameInput,text="17. Updated")
        self.l1.grid(row=5,column=2,sticky='w',padx=5, pady=5,)

        self.l1=Label(self.InventoryFrameInput,text="Id")
        self.l1.grid(row=5,column=4,sticky='w',padx=5, pady=5,)

        #Text Controls
        self.srv_name=StringVar()
        self.srv_nameInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_name)
        self.srv_nameInput.grid(row=0,column=1,padx=5, pady=5,sticky='w')

        self.srv_instance=StringVar()
        self.srv_instanceInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_instance)
        self.srv_instanceInput.grid(row=0,column=3,padx=5, pady=5,sticky='w')

        self.srv_ins_port=StringVar()
        self.srv_ins_portInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_ins_port)
        self.srv_ins_portInput.grid(row=0,column=5,padx=5, pady=5,sticky='w')

        self.srv_ip1=StringVar()
        self.srv_ip1Input=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_ip1)
        self.srv_ip1Input.grid(row=1,column=1,padx=5, pady=5,sticky='w')

        self.srv_ip2=StringVar()
        self.srv_ip2Input=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_ip2)
        self.srv_ip2Input.grid(row=1,column=3,padx=5, pady=5,sticky='w')

        self.srv_user=StringVar()
        self.srv_userInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_user)
        self.srv_userInput.grid(row=1,column=5,padx=5, pady=5,sticky='w')

        self.srv_pwd=StringVar()
        self.srv_pwdInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_pwd,show='*')
        self.srv_pwdInput.grid(row=2,column=1,padx=5, pady=5,sticky='w')

        self.srv_directory=StringVar()
        self.srv_directoryInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_directory)
        self.srv_directoryInput.grid(row=2,column=3,padx=5, pady=5,sticky='w')

        self.srv_os=StringVar()
        self.srv_osInput=ttk.Combobox(self.InventoryFrameInput,values=['Linux','Windows','N/A'],state='readonly')
        self.srv_osInput.grid(row=2,column=5,padx=5, pady=5,sticky='w')
        self.srv_osInput.current(0)

        self.srv_frecuency=StringVar()
        self.srv_frecuencyInput=ttk.Combobox(self.InventoryFrameInput,values=['Daily','Monday','Monthly','Saturday','Sunday'],state='readonly')
        self.srv_frecuencyInput.grid(row=3,column=1,padx=5, pady=5,sticky='w')
        self.srv_frecuencyInput.current(0)

        self.srv_bk_location=StringVar()
        self.srv_bk_locationInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_bk_location)
        self.srv_bk_locationInput.grid(row=3,column=3,padx=5, pady=5,sticky='w')

        self.srv_type=StringVar()
        self.srv_typeInput=ttk.Combobox(self.InventoryFrameInput,values=['MSSQL','MySQL','Oracle','PostgreSQL','Sybase'],state='readonly')
        self.srv_typeInput.grid(row=3,column=5,padx=5, pady=5,sticky='w')
        self.srv_typeInput.current(0)

        self.srv_location=StringVar()
        self.srv_locationInput=ttk.Combobox(self.InventoryFrameInput,values=['GCP','OnPrem'],state='readonly')
        self.srv_locationInput.grid(row=4,column=1,padx=5, pady=5,sticky='w')
        self.srv_locationInput.current(0)

        self.srv_domain=StringVar()
        self.srv_domainInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_domain)
        self.srv_domainInput.grid(row=4,column=3,padx=5, pady=5,sticky='w')

        self.srv_active=StringVar()
        self.srv_activeInput=ttk.Combobox(self.InventoryFrameInput,values=['Inactive','Active'],state='readonly')
        self.srv_activeInput.grid(row=4,column=5,padx=5, pady=5,sticky='w')
        self.srv_activeInput.current(0)

        self.srv_created_dt=StringVar()
        self.srv_created_dtInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_created_dt)
        self.srv_created_dtInput.grid(row=5,column=1,padx=5, pady=5,sticky='w')

        self.srv_updated_dt=StringVar()
        self.srv_updated_dtInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_updated_dt)
        self.srv_updated_dtInput.grid(row=5,column=3,padx=5, pady=5,sticky='w')

        self.srv_created_dtInput.config(state=DISABLED)
        self.srv_updated_dtInput.config(state=DISABLED)

        self.srv_id=StringVar()
        self.srv_idInput=ttk.Entry(self.InventoryFrameInput,textvariable=self.srv_updated_dt)
        self.srv_idInput.grid(row=5,column=5,padx=5, pady=5,sticky='w')

        #Listbox Controls

        self.InventoryTree=ttk.Treeview(self.InventoryFrameInput,show='headings',height=7)
        self.InventoryTree.grid(row=8,column=0,columnspan=7,padx=5, pady=5,)
        self.InventoryTree['columns'] = ('No','srv_name','srv_instance','srv_ins_port',\
        'srv_ip1','srv_ip2','srv_user','srv_pwd','srv_directory','srv_os',\
        'srv_frecuency','srv_bk_location','srv_type','srv_location','srv_domain',\
        'srv_active_literal','srv_created_dt','srv_updated_dt','srv_active')
        self.InventoryTree['displaycolumns'] = ('No','srv_name','srv_instance',\
        'srv_ins_port','srv_ip1','srv_ip2','srv_user','srv_directory',\
        'srv_os','srv_frecuency','srv_bk_location','srv_type','srv_location',\
        'srv_domain','srv_active_literal')
        self.InventoryTree.column("No", minwidth=0,width=25)
        self.InventoryTree.heading("No", text="No",)
        self.InventoryTree.column("srv_name", minwidth=0,width=125)
        self.InventoryTree.heading("srv_name", text="SERVER",)
        self.InventoryTree.column("srv_instance", minwidth=0,width=140)
        self.InventoryTree.heading("srv_instance", text="INSTANCE",)
        self.InventoryTree.column("srv_ins_port", minwidth=0,width=50)
        self.InventoryTree.heading("srv_ins_port", text="PORT",)
        self.InventoryTree.column("srv_ip1", minwidth=0,width=85)
        self.InventoryTree.heading("srv_ip1", text="IP1",)
        self.InventoryTree.column("srv_ip2", minwidth=0,width=85)
        self.InventoryTree.heading("srv_ip2", text="IP2",)
        self.InventoryTree.column("srv_user", minwidth=0,width=80)
        self.InventoryTree.heading("srv_user", text="USER",)
        self.InventoryTree.column("srv_pwd", minwidth=0,width=65)
        self.InventoryTree.heading("srv_pwd", text="PASS",)
        self.InventoryTree.column("srv_directory", minwidth=0,width=65)
        self.InventoryTree.heading("srv_directory", text="DIR",)
        self.InventoryTree.column("srv_os", minwidth=0,width=30)
        self.InventoryTree.heading("srv_os", text="OS",)
        self.InventoryTree.column("srv_frecuency", minwidth=0,width=50)
        self.InventoryTree.heading("srv_frecuency", text="FREQ",)
        self.InventoryTree.column("srv_bk_location", minwidth=0,width=65)
        self.InventoryTree.heading("srv_bk_location", text="BKPLOC",)
        self.InventoryTree.column("srv_type", minwidth=0,width=30)
        self.InventoryTree.heading("srv_type", text="TYPE",)
        self.InventoryTree.column("srv_location", minwidth=0,width=50)
        self.InventoryTree.heading("srv_location", text="SRVLOC",)
        self.InventoryTree.column("srv_domain", minwidth=0,width=65)
        self.InventoryTree.heading("srv_domain", text="SRVDOM",)
        self.InventoryTree.column("srv_active_literal", minwidth=0,width=65)
        self.InventoryTree.heading("srv_active_literal", text="STATUS",)
        self.InventoryTree.column("srv_created_dt", minwidth=0,width=65)
        self.InventoryTree.heading("srv_created_dt", text="CREATED",)
        self.InventoryTree.column("srv_updated_dt", minwidth=0,width=65)
        self.InventoryTree.heading("srv_updated_dt", text="UPDATED",)
        self.InventoryTree.column("srv_active", minwidth=0,width=65)
        self.InventoryTree.heading("srv_active", text="ACTIVE",)

        self.InventoryTree.bind('<Double-Button-1>', lambda x: self.get_selected_row())

        #Scrollbar Controls
        self.scrollbar_vertical = ttk.Scrollbar(self.InventoryFrameInput, orient="vertical", \
                                           command=self.InventoryTree.yview)
        self.scrollbar_vertical.grid(row=8, column=7, sticky="ens")
        self.InventoryTree.configure(yscrollcommand=self.scrollbar_vertical.set)

        #Button Controls
        self.b1=Button(self.InventoryFrameInput,text="View All",width=12,command= lambda: self.view_command())
        self.b1.grid(row=0,column=6,padx=5, pady=5,)

        self.b2=Button(self.InventoryFrameInput,text="Search",width=12,command= lambda: self.search_command())
        self.b2.grid(row=1,column=6,padx=5, pady=5,)

        self.b3=Button(self.InventoryFrameInput,text="Add",width=12,command= lambda: self.add_command())
        self.b3.grid(row=2,column=6,padx=5, pady=5,)

        self.b4=Button(self.InventoryFrameInput,text="Update selected",width=12,command= lambda: self.update_command())
        self.b4.grid(row=3,column=6,padx=5, pady=5,)

        #self.b5=Button(self.InventoryFrameInput,text="Close",width=12,command=self.InventoryFrameInput.destroy)
        self.b5=Button(self.InventoryFrameInput,text="Close",width=12,command= lambda: self.close_command())
        self.b5.grid(row=4,column=6,padx=5, pady=5,)

        self.b5=Button(self.InventoryFrameInput,text="New keys",width=12,command= lambda: self.newkeys_command())
        self.b5.grid(row=5,column=6,padx=5, pady=5,)


    def view(self):
        self.sqlexec="SELECT \
        srv_id as No,\
        srv_name,\
        srv_instance,\
        srv_ins_port,\
        srv_ip1,\
        srv_ip2,\
        srv_user,\
        srv_pwd,\
        srv_directory,\
        ifnull(srv_os,0),\
        ifnull(srv_frecuency,0),\
        srv_bk_location,\
        ifnull(srv_type,0),\
        ifnull(srv_location,0),\
        srv_domain,\
        CASE WHEN srv_active = 0 THEN 'OFF'\
        ELSE 'ON' END AS srv_active_letter,\
        srv_created_dt,\
        srv_updated_dt,\
        ifnull(srv_active,0) srv_active\
        FROM lgm_servers,\
        (SELECT @row_number:=0) AS t\
        ORDER BY srv_name;"
        self.rows=dbservers(self.sqlexec,InventoryFeeds.mysqlserver,InventoryFeeds.mysqlusername,InventoryFeeds.mysqlpsw)
        #print (rows)
        return self.rows

    def get_selected_row(self):
        try:

            InventoryFeeds.selected_row=self.InventoryTree.set(self.InventoryTree.selection())
            #print(InventoryFeeds.selected_row)
            self.srv_idInput.delete(0,END)
            self.srv_idInput.insert(END,InventoryFeeds.selected_row['No'])
            self.srv_nameInput.delete(0,END)
            self.srv_nameInput.insert(END,InventoryFeeds.selected_row['srv_name'])
            self.srv_instanceInput.delete(0,END)
            self.srv_instanceInput.insert(END,InventoryFeeds.selected_row['srv_instance'])
            self.srv_ins_portInput.delete(0,END)
            self.srv_ins_portInput.insert(END,InventoryFeeds.selected_row['srv_ins_port'])
            self.srv_ip1Input.delete(0,END)
            self.srv_ip1Input.insert(END,InventoryFeeds.selected_row['srv_ip1'])
            self.srv_ip2Input.delete(0,END)
            self.srv_ip2Input.insert(END,InventoryFeeds.selected_row['srv_ip2'])
            self.srv_userInput.delete(0,END)
            self.srv_userInput.insert(END,InventoryFeeds.selected_row['srv_user'])
            self.srv_pwdInput.delete(0,END)
            #self.srv_pwdInput.insert(END,InventoryFeeds.selected_row[''])
            self.secret = HidePass('',InventoryFeeds.selected_row['srv_pwd'])
            self.secret.readingprivkey()
            self.secret.unhidepwd()
            self.srv_directoryInput.delete(0,END)
            self.srv_directoryInput.insert(END,InventoryFeeds.selected_row['srv_directory'])
            self.srv_osInput.delete(0,END)
            self.srv_osInput.current(int(InventoryFeeds.selected_row['srv_os']))
            self.srv_frecuencyInput.delete(0,END)
            self.srv_frecuencyInput.current(int(InventoryFeeds.selected_row['srv_frecuency']))
            self.srv_bk_locationInput.delete(0,END)
            self.srv_bk_locationInput.insert(END,InventoryFeeds.selected_row['srv_bk_location'])
            self.srv_typeInput.delete(0,END)
            self.srv_typeInput.current(int(InventoryFeeds.selected_row['srv_type']))
            self.srv_locationInput.delete(0,END)
            self.srv_locationInput.current(int(InventoryFeeds.selected_row['srv_location']))
            self.srv_domainInput.delete(0,END)
            self.srv_domainInput.insert(END,InventoryFeeds.selected_row['srv_domain'])
            self.srv_activeInput.delete(0,END)
            self.srv_activeInput.current(int(InventoryFeeds.selected_row['srv_active']))
            self.srv_created_dtInput.delete(0,END)
            self.srv_created_dtInput.insert(END,InventoryFeeds.selected_row['srv_created_dt'])
            self.srv_updated_dtInput.delete(0,END)
            self.srv_updated_dtInput.insert(END,InventoryFeeds.selected_row['srv_updated_dt'])
        except IndexError:
            pass

    def view_command(self):
        for self.i in self.InventoryTree.get_children():
            self.InventoryTree.delete(self.i)
        for self.row in self.view():
            self.InventoryTree.insert("", END, values=(self.row[0],self.row[1],self.row[2],self.row[3],\
            self.row[4],self.row[5],self.row[6],self.row[7].decode('utf8'),self.row[8],self.row[9],self.row[10],self.row[11],self.row[12],\
            self.row[13],self.row[14],self.row[15],self.row[16],self.row[17],self.row[18]))

    def search_command(self):
        for i in self.InventoryTree.get_children():
            self.InventoryTree.delete(i)
        self.sqlexec="""SELECT \
        srv_id No,\
        srv_name,\
        srv_instance,\
        srv_ins_port,\
        srv_ip1,\
        srv_ip2,\
        srv_user,\
        srv_pwd,\
        srv_directory,\
        srv_os,\
        srv_frecuency,\
        srv_bk_location,\
        srv_type,\
        srv_location,\
        srv_domain,\
        CASE WHEN srv_active = 0 THEN 'OFF'\
        ELSE 'ON' END AS srv_active_letter,\
        srv_created_dt,\
        srv_updated_dt,\
        srv_active\
        FROM lgm_servers,\
        (SELECT @row_number:=0) AS t\
        WHERE\
        srv_name=%s\
        OR srv_instance=%s\
        ORDER BY srv_name;"""
        self.parameters = (self.srv_nameInput.get(),self.srv_instanceInput.get())
        for self.row in dbserversQuery(self.sqlexec,self.parameters,InventoryFeeds.mysqlserver,InventoryFeeds.mysqlusername,InventoryFeeds.mysqlpsw):
            self.InventoryTree.insert("", END, values=(self.row[0],self.row[1],self.row[2],self.row[3],\
            self.row[4],self.row[5],self.row[6],self.row[7].decode('utf8'),self.row[8],self.row[9],self.row[10],self.row[11],self.row[12],\
            self.row[13],self.row[14],self.row[15],self.row[16],self.row[17],self.row[18]))

    def newkeys_command(self):
        self.secret = HidePass('','')
        self.secret.generatekeys()
        success_handler("Keys","New keys were generated")

    def add_command(self):
        self.secret = HidePass(self.srv_pwdInput.get(),'')
        self.secret.readingpubkey()
        self.secret.hidepwd()

        self.sqlexec =""" INSERT INTO lgm_servers (srv_name,srv_instance,srv_ins_port,\
        srv_ip1, srv_ip2,srv_user,srv_pwd,srv_directory,srv_os,srv_frecuency,\
        srv_bk_location,srv_type,srv_location,srv_domain,srv_active,srv_created_dt,\
        srv_updated_dt)\
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        self.parameters=(self.srv_nameInput.get(),self.srv_instanceInput.get(),self.srv_ins_portInput.get(),\
        self.srv_ip1Input.get(),self.srv_ip2Input.get(),self.srv_userInput.get(),self.secret.encrypted,\
        self.srv_directoryInput.get(),str(self.srv_osInput.current()),str(self.srv_frecuencyInput.current()),\
        self.srv_bk_locationInput.get(),str(self.srv_typeInput.current()),str(self.srv_locationInput.current()),\
        self.srv_domainInput.get(),self.srv_activeInput.current(),self.srv_created_dtInput.get(),\
        self.srv_updated_dtInput.get())
        #print (sqlexec)
        dbserversCreate(self.sqlexec,self.parameters,InventoryFeeds.mysqlserver,InventoryFeeds.mysqlusername,InventoryFeeds.mysqlpsw)
        self.view_command()

    def update_command(self):
        self.secret = HidePass(self.srv_pwdInput.get(),'')
        self.secret.readingpubkey()
        self.secret.hidepwd()

        self.now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

        self.sqlexec ="""UPDATE lgm_servers \
        SET srv_name=%(srv_name)s\
        ,srv_instance=%(srv_instance)s\
        ,srv_ins_port=%(srv_ins_port)s\
        ,srv_ip1=%(srv_ip1)s\
        ,srv_ip2=%(srv_ip2)s\
        ,srv_user=%(srv_user)s\
        ,srv_pwd=%(srv_pwd)s\
        ,srv_directory=%(srv_directory)s\
        ,srv_os=%(srv_os)s\
        ,srv_frecuency=%(srv_frecuency)s\
        ,srv_bk_location=%(srv_bk_location)s\
        ,srv_type=%(srv_type)s\
        ,srv_location=%(srv_location)s\
        ,srv_domain=%(srv_domain)s\
        ,srv_active=%(srv_active)s\
        ,srv_created_dt=%(srv_created_dt)s\
        ,srv_updated_dt=%(srv_updated_dt)s\
        WHERE\
        srv_id=%(srv_id)s"""
        self.parameters = {
        "srv_name": self.srv_nameInput.get(),\
        "srv_instance": self.srv_instanceInput.get(),\
        "srv_ins_port": self.srv_ins_portInput.get(),\
        "srv_ip1": self.srv_ip1Input.get(),\
        "srv_ip2": self.srv_ip2Input.get(),\
        "srv_user": self.srv_userInput.get(),\
        'srv_pwd':self.secret.encrypted,\
        "srv_directory": self.srv_directoryInput.get(),\
        "srv_os": str(self.srv_osInput.current()),\
        "srv_frecuency": str(self.srv_frecuencyInput.current()),\
        "srv_bk_location": self.srv_bk_locationInput.get(),\
        "srv_type": str(self.srv_typeInput.current()),\
        "srv_location": str(self.srv_locationInput.current()),\
        "srv_domain": self.srv_domainInput.get(),\
        "srv_active": self.srv_activeInput.current(),\
        "srv_created_dt": self.srv_created_dtInput.get(),\
        "srv_updated_dt": self.now,\
        "srv_id": self.srv_idInput.get()
        }

        for i in self.InventoryTree.get_children():
            self.InventoryTree.delete(i)
        dbserversCreate(self.sqlexec,self.parameters,InventoryFeeds.mysqlserver,InventoryFeeds.mysqlusername,InventoryFeeds.mysqlpsw)
        self.view_command()

    def close_command(self):
        self.InventoryFeed.destroy()
        #return

#window=Tk()
#mysqlserver='172.25.20.17'
#mysqlusername='ISJCruz'
#mysqlpsw='T3lu52018!'
#Interfaz = InventoryFeeds(window,mysqlserver,mysqlusername,mysqlpsw)
#window.mainloop()
