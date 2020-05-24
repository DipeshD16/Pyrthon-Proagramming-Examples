"""n =int(input("Enter the number")"""
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print (c)
n=eval(input("enter value = "))
fib(n)
        

"""print("The value of the fibonacci series for the number", n, "is:", (c))"""
