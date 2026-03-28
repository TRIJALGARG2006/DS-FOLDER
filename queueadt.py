queue = []

def insert(item):
    queue.append(item)

def delete():
    if not isEmpty():
        return queue.pop(0)
    else:
        raise IndexError("Queue is empty")
    
def isEmpty():
    return len(queue) == 0

def traverse():
    for item in queue:
        print(item)

while True : 
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to insert: ")
        insert(item)
    elif choice == 2:
        try:
            deleted_item = delete()
            print(f"Deleted item: {deleted_item}")
        except IndexError as e:
            print(e)
    elif choice == 3:
        traverse()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")