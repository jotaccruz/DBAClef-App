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
from bs4 import BeautifulSoup

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
    print("getting")
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

def mssqlversioneverywhere(version):
    URL = 'https://sqlcollaborative.github.io/assets/dbatools-buildref-index.json'
    page = requests.get(URL).json()
    print("getting")
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

# savehtml(r.content,'google_com')

def savehtml(html, path):
    with open(path,'wb') as f:
        f.write(html)

def openhtml(path):
    with open(path,'rb') as f:
        return f.read()

def BeatifulSoup_Parser(version):
    URL = 'https://sqlserverbuilds.blogspot.com/index.html'
    r = requests.get(URL)
    HtmlPage = r.content

    page_html_text = BeautifulSoup(HtmlPage, "html5lib")
    div_areas_with_important_tables = page_html_text.find_all(lambda tag: tag.name=='div' and tag.get('class') == ['oxa'])

    rows_important_tables = div_areas_with_important_tables[0].find_all("th")
    # columns_title_important_tables = rows_important_tables[0]
    # for title in columns_title_important_tables:
    #     print (title.get_text())

    all_data = []

    for item in div_areas_with_important_tables:
        rows_important_tables = item.find_all("tr")
        for rows in rows_important_tables:
            columns_data_important_tables = rows.find_all("td")
            data_values = []
            data_values
            for data in columns_data_important_tables:
                data_values.append(data.get_text())
            all_data.append(data_values)

    all_versions = []
    for items in all_data:
        if len(items) != 0:
            all_versions.append(items[0])


    animals = []
    for element in all_versions:
        if (element > version and element[:element.index('.')] == version[:version.index('.')]):
            #animals.append(dic["Version"])
            animals.append(element)


    return animals

    # rows_important_tables = div_areas_with_important_tables[6].find_all("tr")
    # columns_title_important_tables = rows_important_tables[0].find_all("th")

    # for items in columns_title_important_tables:
        # print (items.contents[0])

    # for columns in rows_important_tables:
    #     columns_data_important_tables = columns.find_all("td")
    #     for tags in columns_data_important_tables:
    #         print (tags.get_text())

# version = BeatifulSoup_Parser(htmldoc)

# [[row[i] for row in version] for i in range(7)]
#
# printing = BeatifulSoup_Parser('15.0.2000.5')
# printing.sort()
# print(printing)
