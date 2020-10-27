'''
Author: MrLiuYS
Date: 2020-10-21 21:29:33
LastEditors: MrLiuYS
Description: 文件操作
'''

from pathlib import Path
import os

path = os.getcwd()+""

def hasFile(year=0,month=0,day=0,hour=0,sex='M',earth='N'):
    my_file = Path(path + "/files/%s_%s_%s_%s_%s_%s.htm" % (year,month,day,hour,sex,earth))
    
    if my_file.is_file():
        print("已经存在文件:",my_file)
        return True
    print("不存在文件:",my_file)
    return False


def write(info,year=0,month=0,day=0,hour=0,sex='M',earth='N'):
    # mkdir("/files/%s_%s_%s_%s_%s_%s.htm" % (year,month,day,hour,sex,earth))
    infoString = str(info)
    print("infoString----------")
    print(infoString)

    if (
        infoString.find("请求报错---------------") == -1 &
        infoString.find("親愛的用戶您好，您已達當日免費算命查詢次數限制上限！") == -1 &
        infoString.find("5歲以上之命盤分析，限付費會員才能讀取") == -1):
        fileObject = open(path + "/files/%s_%s_%s_%s_%s_%s.htm" % (year,month,day,hour,sex,earth), 'w')  
        fileObject.write(infoString)  
        fileObject.close
