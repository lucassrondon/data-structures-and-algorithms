class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

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

    def insert(self, item, index=int):
        if index >= 0 and index <= self.size: 
            newNode = Node(item)
            if self.head:
                if index == 0: 
                    newNode.next = self.head 
                    self.head = newNode 
                elif index == self.size: 
                    pointer = self.head
                    while pointer.next: 
                        pointer = pointer.next
                    pointer.next = newNode
                elif index > 0 and index < self.size: 
                    counter = 0
                    pointer = self.head
                    while pointer.next:
                        if counter + 1 == index:
                            newNode.next = pointer.next
                            pointer.next = newNode
                            break
                        counter = counter + 1
                        pointer = pointer.next
            else:
                self.head = newNode
            self.size = self.size + 1
        else:
            return False

    def remove(self, index):
        if index >= 0 and index < self.size: 
            if index == 0:
                self.head = self.head.next
                self.size = self.size - 1
                return True
            elif index == self.size-1:
                counter = 0
                pointer = self.head
                while pointer.next:
                    if counter + 1 == index:
                        pointer.next = None
                        self.size = self.size - 1
                        break
                    counter = counter + 1
                    pointer = pointer.next
                return True
            else:
                counter = 0
                pointer = self.head
                while pointer.next:
                    if counter + 1 == index:
                        previousIndex = pointer
                    elif counter == index:
                        previousIndex.next = pointer.next
                        self.size = self.size - 1
                        break
                    pointer = pointer.next
                    counter = counter + 1

                return True
        else:
            return False

    def getItem(self, index):
        if index >= 0 and index < self.size and self.size > 0: 
            counter = 0
            pointer = self.head
            while pointer.next: 
                if counter == index:
                    return pointer.item
                counter = counter + 1
                pointer = pointer.next
            if counter == index: 
                return pointer.item
        else:
            return False

    def getIndex(self, item):
        if self.size == 0:
            return False
        else:
            counter = 0
            pointer = self.head
            while pointer.next: 
                if item == pointer.item:
                    return counter
                counter = counter + 1
                pointer = pointer.next
            if item == pointer.item:
                return counter
            else:
                return False

    def empty(self):
        self.head = None
        self.size = 0
    
    def checkIfListsAreEqual(self, list2):
        if self.getListSize() != list2.getListSize(): 
            return False
        elif self.getListSize() == 0: 
            return True
        else: 
            pointerOfList1 = self.head 
            pointerOfList2 = list2.head
            while pointerOfList1.next:
                if pointerOfList1.item != pointerOfList2.item:
                    return False
                pointerOfList1 = pointerOfList1.next
                pointerOfList2 = pointerOfList2.next
            if pointerOfList1.item != pointerOfList2.item:
                return False
            else:
                return True

    def reverseList(self):
        counter = 1 
        whereToBegin = 1 
        reversedList = LinkedList()
        for i in range(0, self.getListSize()):
            pointer = self.head
            while counter < self.getListSize():
                pointer = pointer.next
                counter = counter + 1
            reversedList.insert(pointer.item, reversedList.getListSize()) 
            whereToBegin = whereToBegin + 1
            counter = whereToBegin
        return reversedList

    def getListSize(self): 
        return self.size
