"""
version:0.1
Author:wanglinag
"""
import math
year = int(input("输入年份:"))
if(year % 400==0) :
    print("%d 是闰年" % year)
elif year %4 == 0 and year % 100 !=0:
    print("%d 是闰年" % year)
else:
    print("%d 不不不不不不是闰年" % year)
################################################3

r = float(input("请输入半径:"))
print("该○的周长是=%f,半径是=%f" % (2*math.pi*r,math.pi*r*r))