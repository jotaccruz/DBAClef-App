# -*- coding: utf-8 -*-
"""
Python 3.7.4
Created on Fri Nov  8 10:57:06 2019
Code behind the App that helps DBA to apply best practice to SQL Server:
    
@author: juan.cruz2

"""

import pyodbc
import mysql.connector
import tkinter
from tkinter import messagebox
import dbaClefDrivers
from dbaClefDrivers import *

#from mysql.connector.constants import ClientFlag
#from mysql.connector import errorcode

def error_handler(err, title):
    tkinter.messagebox.showerror("dbaClef - Conn error: "+ title , err)

def success_handler(title,message):
    tkinter.messagebox.showinfo("dbaClef - " + title,message)

def mysqlconnect(mysqlserver,mysqlusername,mysqlpsw):
    #mysqlserver = '172.25.20.17'
    mysqldatabase = 'db_legacy_maintenance'
    #mysqlusername = 'ISJCruz'
    #mysqlpsw = 'T3lu52018!'
    #mysqlinstancename = 'SUSWEYAK03'
    #sslpath="./ssl-certs/"
                            
    config = {
    'user': mysqlusername,
    'database': mysqldatabase,
    'password': mysqlpsw,
    'host': mysqlserver,
    #'client_flags': [ClientFlag.SSL],
    #'ssl_ca': sslpath + '/server-ca.pem' ,
    #'ssl_cert': sslpath + '/client-cert.pem',
    #        'ssl_key': sslpath + '/client-key.pem',
            }
    try:
        mysqlconn = mysql.connector.connect(**config)
        return mysqlconn
    except mysql.connector.Error as err:
        error_handler(err,"Inventory Database")
        #messagebox.showinfo ("Connection Error", err)
        #return err
        
def mssqlconnect(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw):
    #CONNECTION ZONE
    mssqldriver = mssqlodbc()
    #print (mssqldriver)
    #mssqlserver = 'tcp:35.247.3.208,1433'
    #mssqlserver = 'SCAEDYAK02'
    #mssqlinstance = 'GLOBALSOLARWINDS'
    #mssqldatabase = 'DBAdmin'
    #mssqlusername = 'test'
    #mssqlpsw = ''
    #mssqlinstancename = 'localhost'
    #mssqlconnection_string = "DRIVER={"+mssqldriver+"};SERVER="\
    #                          +mssqlserver+";DATABASE="+mssqldatabase+";UID=" \
    #                          +mssqlusername+";PWD="+mssqlpsw+";Encrypt=Yes;"+\
    #                          "TrustServerCertificate=yes;Application Name=dbaClef;"
    if (mssqlusername==''):
        mssqlconnection_string = "DRIVER={"+mssqldriver+"};SERVER="\
                              +mssqlserver+"\\"+mssqlinstance+";DATABASE="+mssqldatabase+";trusted_connection=Yes;Encrypt=Yes;"+\
                              "TrustServerCertificate=yes;Application Name=dbaClef;"
    else:
        mssqlconnection_string = "DRIVER={"+mssqldriver+"};SERVER="\
                              +mssqlserver+";DATABASE="+mssqldatabase+";UID=" \
                              +mssqlusername+";PWD="+mssqlpsw+";Encrypt=Yes;"+\
                              "TrustServerCertificate=yes;Application Name=dbaClef;"
                              
    #mssqlconnection_string = "DRIVER={"+mssqldriver+"};SERVER="\
    #                          +mssqlserver+"\\"+mssqlinstance+";DATABASE="+mssqldatabase+";trusted_connection=Yes;Encrypt=Yes;"+\
    #                          "TrustServerCertificate=yes;Application Name=dbaClef;"
    #print (mssqlconnection_string)
    try:
        mssqlconn = pyodbc.connect(mssqlconnection_string)
        return mssqlconn
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        messagebox.showinfo ("Connection Error", sqlstate)
        
def mssqlexec(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw,sqlexec):
    conn=mssqlconnect(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw)
    cur=conn.cursor()
    conn.autocommit = True
    cur.execute(sqlexec)
    conn.close()

def mssqldetail(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw,sqlexec):
    conn=mssqlconnect(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw)
    cur=conn.cursor()
    cur.execute(sqlexec)
    rows=cur.fetchall()
    conn.close()
    return rows

def mssqldetailsp(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw,sqlexec1,\
                  sqlexec2,sqlexec3):
    conn=mssqlconnect(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw)
    cur=conn.cursor()
    cur.execute(sqlexec1)
    cur.execute(sqlexec2)
    cur.execute(sqlexec3)
    rows=cur.fetchall()
    conn.close()
    return rows

def mssqldetail2sql(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw,sqlexec1,\
                  sqlexec3):
    conn=mssqlconnect(mssqlserver,mssqlinstance,mssqldatabase,mssqlusername,mssqlpsw)
    cur=conn.cursor()
    cur.execute(sqlexec1)
    cur.execute(sqlexec3)
    rows=cur.fetchall()
    conn.close()
    return rows
    
def insert(title,author,year,isbn):
    conn=mssqlconnect()
    cur=conn.cursor()
    cur.execute("INSERT INTO book(title,author,year,isbn) VALUES (?,?,?,?)",\
                (title,author,year,isbn))
    conn.commit()
    conn.close()

def dbservers(queryexec,mysqlserver,mysqlusername,mysqlpsw):
    conn=mysqlconnect(mysqlserver,mysqlusername,mysqlpsw)
    cur=conn.cursor()
    cur.execute(queryexec)
    rows=cur.fetchall()
    conn.close()
    return rows

#dbservers()