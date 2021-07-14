from pythonProject.structure.structure import LinkList


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DoubleLinkList(LinkList.SingleLinkList):
    '''
    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            count = 0
            while current != None:
                current = current.next
                count += 1
            return count

    def travel(self):
        pass
'''
    def __init__(self, node=None):
        super(DoubleLinkList, self).__init__(node)

    def get_head(self):
        return self.head.data

    def add(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node

    def append(self, item):
        node = DoubleNode(item)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        node.pre = current

    def insert(self, index, item):
        node =  DoubleNode(item)
        current = self.head
        if index <= 0:
            self.add(item)
        elif index > (self.length()-1):
            self.append(item)
        else:
            count = 0
            while count < (index-1):
                current = current.next
                count += 1
            node.next = current.next
            current.next.pre = node
            current.next = node
            node.pre = current

    def pop(self):
        current = self.head
        if self.is_empty():
            print("DoubleLinkList is empty!")
        elif self.length() == 1:
            self.head = None
        else:
            while current.next != None:
                current =  current.next
            current.pre.next = None

    def remove(self, item):
        pass

    def search(self):
        pass


if __name__ == '__main__':
    l3 = DoubleLinkList()
    l3.add(2)
    l3.add(3)
    l3.add(4)
    l3.append(8)
    l3.insert(3,1)
    l3.pop()

    print()
    l3.travel()


