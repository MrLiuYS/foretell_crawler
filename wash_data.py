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

import os

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

def traverse(tree,treeArray):

    for node in tree:
        if type(node) == bs4.element.Tag:

            pTree= traverse(node,[])
            if(len(pTree)):
                treeArray.append(pTree)
            
        elif type(node) == bs4.element.NavigableString:
            print('-----------------222')
            if len(node):
                treeArray.append(node)
            
            print('-----------------222')
        else :
            print('-----------------333')
            if len(node):
                treeArray.append(node)
            print('-----------------333')
            # subs.append(strFormat(sub.text))
    return treeArray

def get_top_table(soup):
    bs = []
    table_header = soup.table
    return traverse(table_header,bs)
    # for index, row in enumerate(table_header):
    #     if (row.name != None)  :
    #         subs=[]
    #         for sub in row:
    #             print(type(sub))
    #             print('-----------------')
    #             if (sub.name != None):
    #                 sub1s=[]
    #                 for sub1 in sub:
    #                     if (sub1.name != None):
    #                         sub1s.append(strFormat(sub1.text))
    #                 subs.append(sub1s)
    #         bs.append(subs)
    # return bs

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
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))
            bs.append(subs)

    return bs

def get_panel3(soup):
    bs = []
    panel2 = soup.find_all(id='panel3')[0]

    return traverse(panel2,bs)
    # for index, row in enumerate(panel2):
    #     if (row.name != None)  :
    #         subs=[]
    #         for sub in row:
    #             if type(sub) == bs4.element.NavigableString:
    #                 subs.append(strFormat(sub))
    #             else :
    #                 subs.append(strFormat(sub.text))
    #         bs.append(subs)

    # return bs
# 柱状图
def get_panel3_columnar(soup):
    bs = []
    panel = soup.find_all("table", width="420")[0]
    
    for index, row in enumerate(panel.find_all('img')):
        map={}
        map["src"]=row.attrs["src"]
        map["style"]=row.attrs["style"]
        bs.append(map)

    return bs

#流年運勢
def get_panel4(soup):
    bs = []
    panel2 = soup.find_all(id='panel4')[0]
    for index, row in enumerate(panel2):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))
            bs.append(subs)

    return bs

#趨吉避凶
def get_panel5(soup):
    bs = []
    panel2 = soup.find_all(id='panel5')[0]
    for index, row in enumerate(panel2):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))
            bs.append(subs)

    return bs

#秤骨論命
def get_panel6(soup):
    bs = []
    panel2 = soup.find_all(id='panel6')[0]
    for index, row in enumerate(panel2):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))
            bs.append(subs)

    return bs

#生肖論命
def get_panel7(soup):
    bs = []
    panel2 = soup.find_all(id='panel7')[0]
    for index, row in enumerate(panel2):
        if (row.name != None)  :
            subs=[]
            for sub in row:
                if type(sub) == bs4.element.NavigableString:
                    subs.append(strFormat(sub))
                else :
                    subs.append(strFormat(sub.text))
            bs.append(subs)

    return bs

#生肖
def get_panel7_zodiac(soup):
    # bs = []
    panel = soup.find_all("img", width="120")[0]
    
    return panel.attrs["src"]

def strFormat(str):
    return re.sub(r'\s+','$_$',str)


def washData(file):

    soup = bs4.BeautifulSoup(open(('files/%s' % file)), 'html.parser')    
    # soup = bs4.BeautifulSoup(open('files/1966_1_1_1_M_N.htm'), 'html.parser')    
    panel = soup.findAll('div',class_='ResultContent')[0]
    
    with open(('datas/%s' % file.replace(".htm", ".json")), "w") as fd:
        map = {}
        map["top_header_time"]=get_top_header_time( panel)
        
        map["top_table_header"]=get_top_table_header(panel)

        # map["get_top_table_left"]=get_top_table_left(panel)
        map["get_top_table"]=get_top_table(panel)

        map["get_panel_head_nav"]=get_panel_head_nav(panel)
        map["get_panel1"]=get_panel1(panel)
        map["get_panel2"]=get_panel2(panel)
        map["get_panel3"]=get_panel3(panel)
        map["get_panel3_columnar"]=get_panel3_columnar(panel)

        map["get_panel4"]=get_panel4(panel)
        map["get_panel5"]=get_panel5(panel)
        map["get_panel6"]=get_panel6(panel)
        map["get_panel7"]=get_panel7(panel)

        map["zodiac"]=get_panel7_zodiac(panel)

        
        
        fd.write(json.dumps(map ,ensure_ascii=False))
        fd.close
    
    return panel


# washData()



list = os.listdir("./files/")

for path in list:
    washData(path)

