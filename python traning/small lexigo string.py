'''
T = int(input("Enter :"))
for _ in range(T):
    P = input()
    S = input()
    small_lex = ""
    for char in P:  
        if char in S:
            small_lex += char
    print(small_lex)



'''
'''Logics for binary tree'''

def totalsum(self,root):
    if root is None:
        return 0
    else:
        leftsum=totalsum(root.left)
        rightsum=totalsum(root.right)
        return root.data+leftsum+rightsum
def treemax(self,root):
    if root is None:
        return 0
    else:
        leftmax=totalsum(root.left)
        rightmax=totalsum(root.right)
    return max(root.data,leftmax,rightmax)
def treeheight(self,root):
    if root is None:
        return 0
    else:
        leftheight=treeheight(root.left)
        rightheight=treeheight(root.right)
        return 1+max(leftheight,rightheight)
def existintree(self,root,value):
    if root is None:
        return False
    else:
        inleft=existintree(root.left,value)
        inright=existintree(root.right,value)
        return root.data == value or inleft or inright
def reversetree(self,root):
    if root is None:
        return 0
    else:
        reversetree(root.left)
        reversetree(root.left)
        root.left,root.right=root.right,root.left
