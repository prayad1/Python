
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.counter = 0

    def create(self):
        while(True):
            choice = input("Want to add node in linked list (y/n) : ")
            if choice == "y" or choice == "Y":
                myData = int(input("Enter data : "))
                newnode = Node(myData)
                if self.head == None:
                    self.head = newnode
                    current = newnode
                else:
                    current.next = newnode
                    current = current.next
                self.counter += 1

            if choice == "n" or choice == "N":
                break

    def display(self):
        if self.head == None:
            print("Empty Linked list")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next

    def Countfun(self):
        print(f"Total count of nodes is : {self.counter}")

    def insertAtHead(self):
        myData = int(input("Enter data to insert : "))
        newnode = Node(myData)
        if self.head == None:
            self.head = newnode
            self.counter += 1
        else:
            newnode.next = self.head
            self.head = newnode
            self.counter += 1


    def insertAtTail(self):
        if self.head == None:
            self.insertAtHead()
        else:
            current = self.head
            while current.next != None:
                current = current.next
            myData = int(input("Enter data to insert : "))
            newnode = Node(myData)
            current.next = newnode
            self.counter += 1

    def insertBefore(self):
        position = int(input("Enter position before which you want to insert a node : "))
        if position == 1:
            self.insertAtHead()
        elif position < 1 or position > self.counter+1:
            print("This is Invalid position")
        elif position == self.counter + 1:
            self.insertAtTail()
        else:
            current = self.head
            i = 1
            while i < (position-1):
                current = current.next
                i += 1
            myData = int(input("Enter data to insert before given position : "))
            newnode = Node(myData)
            newnode.next = current.next
            current.next = newnode
            self.counter += 1


    def insertAfter(self):
        position = int(input("Enter position after which you want to insert node : "))
        if position > self.counter or position < 0:
            print("This is Invalid position")
        elif position == self.counter:
            self.insertAtTail()
        elif position == 0:
            self.insertAtHead()
        else:
            i = 1
            current = self.head
            while i < position :
                current = current.next
                i += 1
            myData = int(input("Enter data to insert after given position : "))
            newnode = Node(myData)
            newnode.next = current.next
            current.next = newnode
            self.counter += 1


   

    def deleteFirst(self):
        if self.head == None:
            print("Can't delete node as List is empty")
        else:
            current = self.head
            self.head = current.next
            self.counter -= 1



    def deleteLast(self):
        if self.head == None:
            print("Can't delete node as List is empty")
        elif self.counter == 1:
            self.head = None
            self.counter -= 1
        else:
            current = self.head
            prev = None
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            self.counter -= 1


    def deletePosition(self):
        if self.head == None:
            print("List is empty")
        else:
            position = int(input("Enter position to delete : "))
            if position < 1 or position > self.counter:
                print("Invalid position")
            elif position == 1:
                self.deleteFirst()
            else:
                current = self.head
                i = 1
                prev = None
                while i < position:
                    prev = current
                    current = current.next
                    i += 1
                prev.next = current.next
                self.counter -= 1



    def reverse(self):
        if self.head == None:
            print("List is empty")
        elif self.counter == 1:
            pass
        else:
            nextnode = self.head
            current = self.head
            prev = None
            while nextnode != None:
                nextnode = nextnode.next
                current.next = prev
                prev = current
                current = nextnode
            self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    while(True):
        print("\n")
        print("Select your choice : \n")
        print("1: Create Linked List")
        print("2: Count nodes")
        print("3: Display")
        print("4: Insert at head")
        print("5: Insert at tail")
        print("6: Insert after given position")
        print("7: Insert before given position")
        print("8: Delete first")
        print("9: Delete last")
        print("10: Delete given position")
        print("11: Reverse")
        print("0: STOP\n")
        choice = int(input("Enter your choice : "))
        print("\n")
        if choice == 1 :
            ll.create()
        elif choice == 2:
            ll.Countfun()
        elif choice == 3:
            ll.display()
        elif choice == 4:
            ll.insertAtHead()
        elif choice == 5:
            ll.insertAtTail()
        elif choice == 6:
            ll.insertAfter()
        elif choice == 7:
            ll.insertBefore()
        elif choice == 8:
            ll.deleteFirst()
        elif choice == 9:
            ll.deleteLast()
        elif choice == 10:
            ll.deletePosition()
        elif choice == 11:
            ll.reverse()
        elif choice == 0:
            print("\nQUIT!!!\n")
            break
