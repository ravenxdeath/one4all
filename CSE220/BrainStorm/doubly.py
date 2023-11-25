
class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:
    
    def __init__(self, a):
        # Creates a Non Dummy Headed Circular Doubly Linked List using the values from the given array a.
        self.head = None
        self.tail = None
        for i in range(len(a)):
            new_node = Node(a[i], None, None)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.head.prev = self.tail
                self.tail.next = self.head
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                new_node.next = self.head
                self.head.prev = new_node
                self.tail = new_node

    # Counts the number of Nodes in the list and return the number
    def countNode(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # prints the elements in the list
    def forwardprint(self):
        current = self.head
        while current:
            print(current.element, end=",")
            current = current.next

    # prints the elements in the list backward
    def backwardprint(self):
        current = self.tail
        while current:
            print(current.element, end=",")
            current = current.prev

    # returns the reference of the at the given index. For invalid index return None.
    def nodeAt(self, idx):
        current = self.head
        count = 0
        while current and count != idx:
            current = current.next
            count += 1
        if current:
            return current
        else:
            print("index error")
            return None

    # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        current = self.head
        index = 0
        while current:
            if current.element == elem:
                return index
            current = current.next
            index += 1
        return -1

    # inserts containing the given element at the given index Check validity of index. 
    def insert(self, elem, idx):
        if idx < 0 or idx > self.countNode():
            print("index error")
        else:
            new_node = Node(elem, None, None)
            if idx == 0:
                new_node.prev = self.tail
                self.tail.next = new_node
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif idx == self.countNode():
                new_node.prev = self.tail
                self.tail.next = new_node
                new_node.next = self.head
                self.head.prev = new_node
                self.tail = new_node
            else:
                current = self.head
                count = 0
                while current and count != idx:
                    current = current.next
                    count += 1
                new_node.prev = current.prev
                current.prev.next = new_node
                new_node.next = current
                current.prev = new_node

    # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
    def remove(self, idx):
        if idx < 0 or idx >= self.countNode():
            print("index error")
            return None
        elif idx == 0:
            removed_elem = self.head.element
            self


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.