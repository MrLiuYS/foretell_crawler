'''
Author: MrLiuYS
Date: 2020-10-21 21:52:05
LastEditors: MrLiuYS
Description: 
'''

# from bs4 import BeautifulSoup
import bs4
import json
import re


#1966年1月1日01-03時  (刀砧日)
def get_top_header_time(soup):
    readme_system_solid = soup.find_all(class_='readme_system_solid')[0]
    bs = []
    for row in readme_system_solid.findAll("b"):
        bs.append(strFormat(row.text))
    return bs

#1月1 庚申日 丑時( 01-03時 )
def get_top_table_header(soup):
    table_header = soup.table.tr.td.table.tr

    bs = []
    for row in table_header:
        if row.name != None :
            bs.append(strFormat(row.text))
    return bs

# def get_top_table_left(soup):
#     bs = []
#     table_header = soup.table.contents[3]
#     table_header = table_header.table
#     for index, row in enumerate(table_header):
#         if (row.name != None) & (5 != index) :
#             subs=[]
#             for sub in row:
#                 if (sub.name != None):
#                     subs.append(strFormat(sub.text))
#             bs.append(subs)
#     return bs

def get_top_table(soup):
    bs = []
    table_header = soup.table.contents[3]
    for index, row in enumerate(table_header):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                if (sub.name != None):
                    sub1s=[]
                    for sub1 in sub:
                        if (sub1.name != None):
                            sub1s.append(strFormat(sub1.text))
                    subs.append(sub1s)

            bs.append(subs)

    return bs

def get_panel_head_nav(soup):
    bs = []
    panelHeadNav = soup.find_all(class_='panelHeadNav')[0]
    for row in panelHeadNav.findAll("li"):
        bs.append(strFormat(row.text))
    return bs
    
def get_panel1(soup):
    bs = []
    panel1 = soup.find_all(id='panel1')[0]
    for index, row in enumerate(panel1):
        if (row.name != None)  :
            for sub in row:
                if (sub.name != None):
                    sub1s=[]
                    for sub1 in sub:
                        if (sub1.name != None):
                            sub1s.append(strFormat(sub1.text))
                    bs.append(sub1s)
    return bs

def get_panel2(soup):
    bs = []
    panel2 = soup.find_all(id='panel2')[0]
    for index, row in enumerate(panel2):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                # if (sub.name != None):
                
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))

                # print(type(sub))
                # print(sub)
                # print('------------')

                # if type(sub) == str:
                #     sub1s.append(strFormat(sub))
                # else:    
                #     for sub1 in sub:
                #         print(sub1)
                #         print('------------')
                #         # if type(sub) == str:
                #         #     sub1s.append(strFormat(sub1))
                #         # else:
                #         #     sub1s.append(strFormat(sub1.text))

                # subs.append(sub1s)

            bs.append(subs)

    return bs

def strFormat(str):
    return re.sub(r'\s+','$_$',str)


def washData():

    soup = bs4.BeautifulSoup(open('files/1966_1_1_1_M_N.htm'), 'html.parser')    
    panel = soup.findAll('div',class_='ResultContent')[0]
    
    with open("data.json", "w") as fd:
        map = {}
        map["top_header_time"]=get_top_header_time( panel)
        
        map["top_table_header"]=get_top_table_header(panel)

        # map["get_top_table_left"]=get_top_table_left(panel)
        map["get_top_table"]=get_top_table(panel)

        map["get_panel_head_nav"]=get_panel_head_nav(panel)
        map["get_panel1"]=get_panel1(panel)
        map["get_panel2"]=get_panel2(panel)
        
        
        
        
        fd.write(json.dumps(map ,ensure_ascii=False))
        fd.close
    
    return panel


washData()