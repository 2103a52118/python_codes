'''
class A:
    def _str_(self):
        return '1'
class B(A):
    def _init_(self):
        super()._init_()
class C(B):
    def _init_(self):
        super()._init_()
def main():
    obj1=B()
    obj2=A()
    obj3=C()
    print(obj1,obj2,obj3)
main()
'''

def isprime(num):
    if num==0 or num==1:
        return False
    for deno in range(2,int(num**0.5)+1):
        if num%deno==0:
            return False
    return True
num=int(input())
primeList=[i for i in range(2,num+1) if isprime(i)]
count,pSum=0,primeList[0]
for p in primeList[1:]:
    pSum+=p
    if pSum>num:
        break
    if isprime(pSum):
        count+=1
print(count)



