'''
Author: MrLiuYS
Date: 2020-10-21 21:52:05
LastEditors: MrLiuYS
Description: 
'''

from bs4 import BeautifulSoup

import json


#1966年1月1日01-03時  (刀砧日)
def get_top_header_time(soup):
    readme_system_solid = soup.find_all(class_='readme_system_solid')[0]
    bs = []
    for row in readme_system_solid.findAll("b"):
        bs.append(row.text)
    return bs

#1月1 庚申日 丑時( 01-03時 )
def get_top_table_header(soup):
    table_header = soup.select('div#ResultContent table[0] tr td')
   
    print(table_header)

    return table_header


def washData():

    soup = BeautifulSoup(open('files/1966_1_1_1_M_N.htm'), 'html.parser')    
    panel = soup.findAll('div',class_='ResultContent')[0]

    
    
    with open("data.json", "w") as fd:
        map = {}
        map["header_times"]=get_top_header_time( panel)
        fd.write(json.dumps(map ,ensure_ascii=False))

        get_top_table_header(panel)
        
        fd.close
    
    return panel


washData()