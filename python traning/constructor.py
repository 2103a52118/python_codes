
'''#Objects and classes
class stu:
    roll=2167
    name='Harshini'
    phn=7729021537
    add='Warangal'

    def display(self):
        print('Name:',self.name,'Roll no:',self.roll)
s1=stu()
s1.display()

#init constructor

class stu:
    def __init__(self,roll,name,phn,add):
        self.roll=roll
        self.name=name
        self.phn=phn
        self.add=add

    def display(self):
        print('Name:',self.name,'Roll no:',self.roll)
s1=stu(2167,'Ash',9381298674,'WGL')
s1.display()'''

def last(t):
    return t[-1]

n = int(input("Enter the no of tuples: "))

t= []
for _ in range(n):
    e = tuple(map(int, input("Enter the elements: ")))
    t.append(e)

t_sort= sorted(t, key=last)

print("Sorted list of tuples:",t_sort)
