#To determine whether a number is prime number
import math

def getPrime(a): #查找根号N以内的所有素数
    primList = []
    primList1 = []
    for i in range(int(math.sqrt(a))+1):
        primList.append(1)
    primList[0],primList[1]=0,0
    for i in xrange(2,len(primList)):
        for j in xrange(i*i,len(primList),i):
            primList[j]=0
    for i in range (len(primList)):
        if primList[i]==1:
            primList1.append(i)
    return primList1

def deterPrim(number,b): #使用欧几里得除法判断素数能不能整除number
    for i in b:
        if number % i !=0:
            continue
        else:
            return False
    return True

def main():
    number = input()
    primList=getPrime(number)
    flag = deterPrim(number,primList)
    if flag==True:
        print number,'is Prime Number'
    else:
        print number,'is not Prime Number'
    

main()