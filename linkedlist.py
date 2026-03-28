# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # For correct tail management

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.traverse()

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.traverse()

    # Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Delete head node
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.traverse()
            return

        # Delete middle or tail node
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                self.traverse()
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    # Traverse list
    def traverse(self):
        if self.head is None:
            print("List: EMPTY")
            return

        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

sll = SinglyLinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete by Value")
    print("4. Traverse")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        sll.insert_beginning(val)

    elif choice == 2:
        val = int(input("Enter value: "))
        sll.insert_end(val)

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        sll.delete_by_value(val)

    elif choice == 4:
        sll.traverse()

    elif choice == 5:
        break

    else:
        print("Invalid choice")