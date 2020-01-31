# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:20:35 2019

@author: juan.cruz2
"""
#important sites
#https://reqbin.com/
#https://htmlformatter.com/
#https://realpython.com
#https://support.microsoft.com/en-ie/help/321185/how-to-determine-the-version-edition-and-update-level-of-sql-server-an

#import json
import requests

def mssqlversion(version):
    URL = 'https://sqlcollaborative.github.io/assets/dbatools-buildref-index.json'
    page = requests.get(URL).json()
    animals = []
    
    for keys in page:
        a = page[keys]
        if (type(a) is list):
            for item in a:
                for key in item:
                    #if (version == item["Version"]):
                    if (item["Version"] > version and item["Version"][:item["Version"].index('.')] == version[:version.index('.')]):
                        animals.append(item["Version"])
    return(list(dict.fromkeys(animals)))

def mssqlversioncomplete(version):
    URL = 'https://sqlcollaborative.github.io/assets/dbatools-buildref-index.json'
    page = requests.get(URL).json()
    animals = []
    for element in page:
        a = page[element]
        if (type(a) is list):
            for dic in a:
                if 'Version' in dic:
                    if (dic["Version"] > version and dic["Version"][:dic["Version"].index('.')] == version[:version.index('.')]):
                        #animals.append(dic["Version"])
                        animals.append(dic)
    return(animals)

#list=mssqlversion('12.0.6259')
#print (list)
#dic = mssqlversioncomplete('12.0.6259')
