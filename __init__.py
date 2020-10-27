'''
Author: MrLiuYS
Date: 2020-10-21 21:23:46
LastEditors: MrLiuYS
Description: 
'''

from datetime import datetime
from datetime import timedelta


import right_works
import foretell_file 

# global line
# global f

f = open("西拉.txt")
line = f.readline()

def daterange(start, end):
    global line
    global f
    while start < end:
        print(start)
        currentDate = start - timedelta(seconds=1)
        if foretell_file.hasFile(currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N') == False:
            print('-------------' + line)
            info = right_works.rightWord(line,currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N')
            infoString = str(info)
            if (
                infoString.find("请求报错---------------") == -1 &
                infoString.find("親愛的用戶您好，您已達當日免費算命查詢次數限制上限！") == -1 &
                infoString.find("5歲以上之命盤分析，限付費會員才能讀取") == -1):
                print('-------------' + line)
            else:
                line = f.readline()
                if not line:
                    f.close()
                    f = open("西拉.txt")
                    line = f.readline()

            foretell_file.write(info,currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N')


        start += timedelta(hours=1)
    
# start_date ='1965-12-31 22:00:00'
start_date ='1966-1-1 22:00:00'
end_date ='1967-01-01 23:59:59'

start_date_object = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
end_date_object = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

daterange(start_date_object, end_date_object)


# while line:
#     print (line)
#     line = f.readline()
# f.close()
