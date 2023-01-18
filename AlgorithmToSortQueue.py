# THE STACK CLASS IS AN IMPLEMENTATION OF THE STACK DATA STRUCTURE
# THE QUEUE CLASS IS AN IMPLEMENTATION OF THE QUEUE DATA STRUCTURE
# THE ALGORITHM TO SORT A QUEUE USING TWO STACKS IS USED IN A METHOD 
# CALLED sortQueue() OF THE QUEUE CLASS 

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.top = -1

    def __repr__(self):
        if self.head == None:
            return '[]'

        pointer = self.head
        if pointer.next == None:
            return '[' + str(pointer.item) + ']'

        list = '['
        while pointer.next:
            list = list + str(pointer.item) + ", "
            pointer = pointer.next
            if not pointer.next:
                list = list + str(pointer.item) + ']'
        return list

    def push(self, item):
        newNode = Node(item)

        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = newNode
            self.top = self.top + 1
            return True
        else:
            self.head = newNode
            self.top = self.top + 1
            return True
            
    def pop(self):
        if self.head:
            if self.top == 0:
                self.head = None
                self.top = self.top -1
                return True
            else:
                pointer = self.head
                while True:
                    if pointer.next.next == None:
                        pointer.next = None
                        self.top = self.top - 1
                        return True
                    pointer = pointer.next
        else:
            return False

    def checkTop(self):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            return pointer.item
        else:
            return False

    def destroy(self):
        self.head = None

class Queue:
    def __init__(self, maximumSize):
        self.maximumSize = maximumSize
        self.queue = [None] * maximumSize
        self.length = 0

    def __repr__(self):
        if self.length == 0:
            return '[]'
        else:
            items = '['
            for i in range(0, self.length):
                if i < self.length - 1:
                    items = items + "'" + str(self.queue[i]) + "'" + ", "
                else:
                    items = items + "'" + str(self.queue[i]) + "'"
            items = items + ']'
            return items
    
    def insert(self, item):
        if self.length == self.maximumSize:
            return False
        elif self.length == 0:
            self.queue[0] = item
            self.length = self.length + 1
            return True
        else:
            self.queue[self.length] = item
            self.length = self.length + 1
            return True

    def remove(self):
        if self.length > 0:
            for item in range(0, self.length-1):
                self.queue[item] = self.queue[item+1]
            self.length = self.length - 1
            return True

    def consult(self):
        if self.length > 0:
            return self.queue[0]
        else:
            return False

    def destroy(self):
        self.length = 0

    def sortQueue(self):
        sortedStack = Stack()
        secondaryStack = Stack()
        
        while self.length != 0:
                while self.consult() > sortedStack.checkTop() and sortedStack.top != -1:
                    secondaryStack.push(sortedStack.checkTop())
                    sortedStack.pop()
                sortedStack.push(self.consult())
                self.remove()

                while secondaryStack.top != -1:
                    sortedStack.push(secondaryStack.checkTop())
                    secondaryStack.pop()

        while sortedStack.top != -1:
            self.insert(sortedStack.checkTop())
            sortedStack.pop()

        return True
