#Input : Year Month     Ex. 2018 5

import sys    
def getyearmonth():
    for line in sys.stdin:
        b=line.split()
        break
    year=int(b[0])
    month=int(b[1])
    return year,month

def firstday(year):
    k=leapyear(year)
    a=(year-1900)*365+k
    return (a+1)%7

def leapyear(year):
    count=0
    for i in range(1900,year):
        if i%4==0 and i%100!=0 or i%400==0:
            count = count+1
    return count

def monthfirstday(year,month,w):
    days=0
    if year%4==0 and year!=100 or year%400==0:
        days = days+1
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(month-1):
        days=days+month_days[i]
    return (days+w)%7

def oneMonth(year,month,w):
    days=getdays(year,month)
    frame=layout(w,days)
    printMonth(frame)

def printMonth(frame):
    print("MON\tTUE\tWED\tTHU\tFRI\tSAT\tSUN")
    for i in range(42):
        print("%s%s"%(frame[i],"\t"),end="")2
        if (i+1)%7==0:
            print ("\n")
    
def layout(w,days):
    frame=42*[""]
    if w==0:
        w=7
    j=w-1
    for i in range(1,days+1):
        frame[j]=i
        j=j+1
    return frame

def getdays(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    days=month_days[month-1]
    if year%4==0 and year!=100 or year%400==0:
        days = days+1
    return days

def main():
    year,month=getyearmonth()
    w=firstday(year)
    if month!=1:
        w=monthfirstday(year,month,w)
    oneMonth(year,month,w)
    
    
main()
