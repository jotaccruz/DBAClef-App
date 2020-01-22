# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:50:56 2020

@author: juan.cruz2
"""

def readFileFromOS(filename):
    with open(filename,'r') as file:
        data=file.read()
    return data
    

#data=readFileFromOS('VLF.sql')
#print (data)

