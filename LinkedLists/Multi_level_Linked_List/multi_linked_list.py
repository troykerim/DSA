class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def createLinkedList():
    # Start with a single head node
    data = input("Enter data for the head node: ")
    head = Node(data)
    buildList(head)
    return head

def buildList(node):
    while True:
        choice = input(
            f"\nAt node '{node.data}', do you want to add:\n"
            "1. Next node\n"
            "2. Child node\n"
            "3. Go back (stop here)\n"
            "Enter choice: "
        )
        
        if choice == "1":
            data = input("Enter data for the next node: ")
            node.next = Node(data)
            node = node.next  # Move to the new node
        elif choice == "2":
            data = input("Enter data for the child node: ")
            node.child = Node(data)
            buildList(node.child)  # Recursively build child list
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

def printList(head):
    while head:
        if head.child:
            printList(head.child)
        print(head.data, end=" ")
        head = head.next

if __name__ == "__main__":
    print("Let's build a multilevel linked list!")
    head = createLinkedList()
    print("\nFinal list (DFS order):")
    printList(head)
    print()
