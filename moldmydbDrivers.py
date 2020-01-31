# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:11:40 2019

@author: juan.cruz2
"""

import pyodbc

def mssqlodbc ():
    mysqlobdc17=''
    mysqlobdc131=''
    mysqlobdc13=''
    mysqlobdc11=''
    for item in pyodbc.drivers():
        if item.find("17") > 0:
            mysqlobdc17 = item
        if item.find("13.1") > 0:
            mysqlobdc131 = item
        if item.find("13") > 0:
            mysqlobdc13 = item
        if item.find("11") > 0:
            mysqlobdc11 = item
    
    if (mysqlobdc17 != ''):
        return mysqlobdc17
    elif (mysqlobdc131 != ''):
        return mysqlobdc131
    elif (mysqlobdc13 != ''):
        return mysqlobdc13
    elif (mysqlobdc11 != ''):
        return mysqlobdc11
    
#odbc=mssqlodbc()