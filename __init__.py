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

def daterange(start, end):
    while start < end:
        print(start)
        currentDate = start - timedelta(seconds=1)

        if foretell_file.hasFile(currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N') == False:
            print('-------------')
            info = right_works.rightWord(currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N')
            foretell_file.write(info,currentDate.year,currentDate.month,currentDate.day,currentDate.hour,'M','N')


        start += timedelta(hours=1)
    
# start_date ='1965-12-31 22:00:00'
start_date ='1966-1-1 22:00:00'
end_date ='1967-01-01 23:59:59'

start_date_object = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
end_date_object = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

daterange(start_date_object, end_date_object)