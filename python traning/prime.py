'''n=int(input("enter number:"))
for i in range(2, n):
    if n % i == 0:
        print(f"not a prime number.")
        break
else:
    print(f" is a prime number.")
******************************************
n=int(input())
c=0
for d in range(1,n+1):
    if n%d==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")

***********************O(1),O(n)*************
'''
n=int(input("enter number:"))
for i in range(2,(n//2)+1):
    if n % i == 0:
        print(f"not a prime number.")
        break
else:
    print(f" is a prime number.")
