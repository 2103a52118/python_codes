class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_in_middle(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_node = Node(new_data)
        new_node.next = slow.next
        slow.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.append(5)

    print("Original linked list:")
    llist.print_list()

    llist.insert_in_middle(3)

    print("Linked list after inserting in the middle:")
    llist.print_list()
