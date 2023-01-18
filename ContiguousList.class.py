class ContiguousList:
    def __init__(self, maximum):
        self.__beginning = -1
        self.__ending = -1
        self.__maximum = maximum

    def __repr__(self):
        if self.isEmpty(): 
            return '[]'
        else: 
            items = '['
            for i in range(self.__beginning, self.__ending):
                items = items + "'" + str(self.vector[i]) + "'" + ", "
            items = items + "'" + str(self.vector[self.__ending]) + "'" + ']'
            return items

    def isEmpty(self):
        if self.__beginning == -1 or self.__ending == -1:
            return True
        else:
            return False
    
    def length(self):
        return self.__ending + 1 

    def getIndex(self, item):
        for i in range(0, self.length()):
            if self.vector[i] == item:
                return i
        return False

    def getItem(self, index):
        if index >= 0 and index < self.length():
            return self.vector[index]
        return False

    def isIndexValid(self, index):
        if index >= self.__beginning and index <= self.__ending + 1:
            return True
        else:
            return False

    def insert(self, item, index=int):
        if self.length() < self.__maximum:
            if self.isEmpty(): 
                if index == 0:
                    self.vector = [None]
                    self.vector[0] = item
                    self.__beginning = 0
                    self.__ending = 0
                    return True
                else:
                    return False
            elif self.isIndexValid(index):
                if [None] not in self.vector:
                    self.vector = self.vector + [None]
                for i in range(self.__ending, index -1, -1):
                    self.vector[i+1] = self.vector[i]
                self.vector[index] = item
                self.__ending = self.__ending + 1
                return True
            else:
                return False
        else:
            return False

    def remove(self, delete_this_index):
        if delete_this_index >= 0 and delete_this_index <= self.__ending:
            for i in range(delete_this_index, self.__ending):
                self.vector[i] = self.vector[i + 1] 
            self.vector[self.__ending] = [None]
            self.__ending = self.__ending - 1
            return True
        else:
            return False

    def emptyList(self):
        self.vector = None
        self.__beginning = -1
        self.__ending = -1
