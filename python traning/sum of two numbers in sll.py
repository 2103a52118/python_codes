class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_and_format_linked_list(num1, num2):
    total = num1 + num2
    
    
    total_str = str(total)
    
    dummy = ListNode(0)
    current = dummy
    
    
    for digit in total_str:
        current.next = ListNode(int(digit))
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.value))
        current = current.next
    print('->'.join(values))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
output1_list = add_and_format_linked_list(num1, num2)


print_linked_list(output1_list)  
