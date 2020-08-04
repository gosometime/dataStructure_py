

class linkNode():
    def __init__(self,initData):
        self.data = initData
        self.next = None

    def setData(self,newData):
        self.data = newData
    def setNext(self,newNext):
        self.next = newNext

    def getData(self):
        return self.data
    def getNext(self):
        return self.next



class linkList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    #在当前节点的后面插入节点
    #1. 找到curData所在的节点
    #2. 插入newData
    def insert(self,curData,newData):
        pass

    # 在头部插入数据
    def addAtHead(self,item):
        tmp = linkNode(item)
        tmp.setNext(self.head)
        self.head = tmp

    def length(self):
        current = self.head
        count = 0
        while current != None:  # ?
            count += 1
            current = current.getNext()
        return count
    def search(self):
        pass


if __name__ == '__main__':
    lklst = linkList()



