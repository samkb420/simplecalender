#!/usr/bin/python
#Author :samkb
#Email:kagosamuel07@yahoo.com


import time
import calendar
print("............Welcome To My Calender...........")
time.sleep(0.5)
fo=open("sam.txt","w+")
print("Enter year and month you want to view calendar")
time.sleep(0.5)
y=int(input("Enter year: "))
m=int(input("Enter month:"))

cal = calendar.month(y, m)
print( "Here is the calendar:")
time.sleep(0.5)
fo.write( cal);

fo.write("Welcome!! Enjoy!!");



fo.close()
