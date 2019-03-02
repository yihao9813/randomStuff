#平凡除法求素数
import math
 
def prime(n):
    if n <= 1:
        return 0

    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

def main():
    n = input()
    for i in range(2,n+1):
        if prime(i):
            print i
main()