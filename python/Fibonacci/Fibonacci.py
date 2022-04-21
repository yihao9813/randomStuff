#Input a Number(Level of Fibo)

def f(n):
    if n <2:
        return n
    b = f(n-1)+f(n-2)
    return b

def main():
    print ('Enter level of Fibo')
    a=eval(input())
    print (f(a))
    

main()
