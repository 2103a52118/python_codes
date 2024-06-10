'''program to printsum of all odd numbers presnet in larger number
3446877846445566
n=int(input())
totSum=0
while n !=0:
  rem=n%10
  if rem%2!=0:
    totSum+=rem
  n//=10  
print(totSum)

program to sor firts half in ascending order and
second half in descending order in an array
input:1 21 5 2 50 16
output:
1 2 5 50 21 16
'''

i= input("Enter the elements of the array separated by spaces: ")
a = list(map(int, i.split()))
n = len(a)
mid = n // 2
first_half = a[:mid]
second_half = a[mid:]
first_half.sort()
second_half.sort(reverse=True)
output_arr = first_half + second_half
print("Output array:", output_arr)
