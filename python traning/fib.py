'''
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return(fib(num-1)+fib(num-2))
num=int(input("enter a number:"))
print("fibonacci series:",end="")
for num in range(0,num):
    print(fib(num),end=" ")
'''


fibval=[0,1]
def fib(n):
    if n<0:
        print("Incorrect input")
    elif n < len(fibval):
        return fibval[n]
    fibval.append(fib(n-1)+fib(n-2))
    return fibval[n]
print(fib(int(input())))
