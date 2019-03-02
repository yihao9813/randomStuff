#To determine whether a number is prime number
import math

def getPrime(a): #查找根号N以内的所有素数
    primList = []
    primList1 = []
    for i in range(a+1):
        primList.append(1)
    primList[0],primList[1]=0,0
    for i in xrange(2,int(math.sqrt(a)+1)): 
        for j in xrange(i*i,len(primList),i):  #以次筛去素数的倍数
            primList[j]=0  
    for i in range (len(primList)):
        if primList[i]==1:
            primList1.append(i)
    return primList1

def deterPrim(number,b): #判断N是否存在素数列表内
    for i in b:
        if number == i :
            return True
    else:
        return False

def main():
    number = input()
    primList=getPrime(10000)
    flag = deterPrim(number,primList)
    if flag==True:
        print number,'is Prime Number'
    else:
        print number,'is not Prime Number'
    
main()