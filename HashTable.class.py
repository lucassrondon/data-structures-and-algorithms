class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def allItems(self):
        if self.head == None:
            return '[]'
        
        pointer = self.head
        returnData = '[CHAVE: ' + str(pointer.key) + '][ITEM: ' + str(pointer.value) + ']'
        while pointer.next:
            returnData = returnData + '\n'
            pointer = pointer.next
            returnData = returnData + '[CHAVE: ' + str(pointer.key) + ']' + '[ITEM: ' + str(pointer.value) + ']'
        return returnData

    def listInsert(self, key, value):
        if self.head == None:
            newNode = Node(key, value)
            self.head = newNode
            self.len = self.len + 1
            return True
        
        pointer = self.head

        if pointer.key == key:
            self.head.value = value
            return True
        
        while pointer.next:
            pointer = pointer.next
            if pointer.key == key:
                pointer.value = value
                return True
        
        newNode = Node(key, value)
        newNode.next = self.head
        self.head = newNode
        self.len = self.len + 1
        return True
    
    def listRemove(self, key):
        if self.head == None:
            return False

        if self.head.key == key:
            newHead = self.head.next
            self.head = newHead
            self.len = self.len - 1
            return True

        pointer = self.head
        
        while pointer.next:
            behindPointer = pointer
            pointer = pointer.next

            if pointer.key == key:
                behindPointer.next = pointer.next
                self.len = self.len - 1
                return True
        return False

    def listItem(self, key):
        if self.head == None:
            return False
        
        pointer = self.head

        if pointer.key == key:
            return pointer.value
        while pointer.next:
            pointer = pointer.next
            if pointer.key == key:
                return pointer.value
        return False

    def isEmpty(self):
        if self.len == 0:
            return True
        return False

class HashTable:
    def __init__(self, numberOfItems):
        numberOfItems = numberOfItems + (numberOfItems // 2)
        prime = True
        while True:
            for i in range(2, numberOfItems):
                if numberOfItems % i == 0:
                    prime = False
                    break
            if prime == True:
                break
            else:
                numberOfItems = numberOfItems + 1
                prime = True

        self.numberOfItems = numberOfItems
        self.vector = [None] * numberOfItems

    def __repr__(self):
        returnData = ''
        for i in range(1, self.numberOfItems):
            if self.vector[i]:
                if returnData != '':
                    returnData = returnData + '\n'
                returnData = returnData + self.vector[i].allItems()
        if returnData != '':
            return returnData
        return '[]'

    def hash(self, key):
        return (key % self.numberOfItems) + 1

    def insert(self, key, value):
        index = self.hash(key)
        if index == self.numberOfItems:
            index = index -1
        if self.vector[index] == None:
            self.vector[index] = List()

        self.vector[index].listInsert(key, value)

        return True
    
    def getValue(self, key):
        index = self.hash(key)
        if index == self.numberOfItems:
            index = index -1

        if self.vector[index] == None:
            return False
        
        returnData = self.vector[index].listItem(key)

        return returnData

    def removeFromTable(self, key):
        index = self.hash(key)
        if index == self.numberOfItems:
            index = index -1

        if self.vector[index] == None:
            return False
        
        returnData = self.vector[index].listRemove(key)

        if self.vector[index].isEmpty():
            self.vector[index] = None

        return returnData
