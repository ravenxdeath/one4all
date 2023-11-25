def __init__(self, a):
    self.head = None
    self.tail = None
    for i in range(len(a)):
        newNode = Node(a[i], None, None)
        if self.head == None:
            self.head = self.tail = newNode
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.tail = newNode

def countNode(self):
    curr = self.head
    count = 0
    if self.head == None:
        return 0
    else:
        while True:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
    return count

def forwardprint(self):
    if self.head == None:
        return
    else:
        curr = self.head
        while True:
            print(curr.element, end=",")
            curr = curr.next
            if curr == self.head:
                break

def backwardprint(self):
    if self.head == None:
        return
    else:
        curr = self.tail
        while True:
            print(curr.element, end=",")
            curr = curr.prev
            if curr == self.tail:
                break
                
def nodeAt(self, idx):
    curr = self.head
    i = 0
    if idx < 0 or idx > self.countNode()-1:
        return None
    else:
        while i != idx:
            curr = curr.next
            i += 1
        return curr
    
def indexOf(self, elem):
    curr = self.head
    i = 0
    if self.head == None:
        return -1
    else:
        while True:
            if curr.element == elem:
                return i
            curr = curr.next
            i += 1
            if curr == self.head:
                break
        return -1
    
def insert(self, elem, idx):
    if idx < 0 or idx > self.countNode():
        return
    else:
        newNode = Node(elem, None, None)
        if idx == 0:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = newNode
        elif idx == self.countNode():
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.head.prev = newNode
        else:
            curr = self.head
            i = 0
            while i != idx:
                curr = curr.next
                i += 1
            newNode.next = curr
            newNode.prev = curr.prev
            curr.prev.next = newNode
            curr.prev = newNode
            
# def remove(self, idx):
#     if idx < 0 or idx > self.countNode()-1:
#         return None
#     else:
#         if idx == 0:
#             e = self.head.element
#             self.head = self.head.next
#             self.head.prev = self.tail
#             self.tail.next = self.head
#             return e
#         elif idx == self.countNode()-1:
#             e = self.tail.element
#             self.tail = self.tail.prev
#             self.tail.next = self.head
#             self.head.prev = self.tail
#             return e
#         else:
#             curr = self.head
            

def remove(self, idx):
    if idx < 0 or idx >= self.countNode():
        return None
    if idx == 0:
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
    elif idx == self.countNode()-1:
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
    else:
        curr = self.head
        for i in range(idx):
            curr = curr.next
        temp = curr
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    return temp.element

