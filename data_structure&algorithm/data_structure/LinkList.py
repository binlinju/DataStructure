class Node():
    def __init__(self, item):
        self.data = item
        self.next = None

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

class SingleLinkList():
    def __init__(self, node=None):
        self.head = node

    def get_head(self):
        return self.head.get_data()

    def is_empty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count += 1
        return count

    def travel(self):
        current = self.head
        while current != None:
            print(current.data, end = ' ')
            current = current.next
        print("")

    def add(self, item):
        '''
        头部添加元素
        :param item:
        :return:
        '''
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        '''
        尾部添加元素
        :param item:
        :return:
        '''
        node =  Node(item)
        current = self.head
        if self.is_empty():
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def insert(self, index, item):
        node = Node(item)
        current = self.head
        count = 0
        if self.length() > index:
            while current != None:
                current = current.next
                count += 1
                while count == (index - 1):
                    previous = current
                    node.next = previous.next
                    previous.next = node
                    break
        else:
            raise IndexError("Index is invalid", index)


    def pop(self, index = None):
        '''
        按索引弹出,默认弹出尾端
        :param index:
        :return:
        '''
        if index == None:
            index = self.length()-1
        current = self.head
        count = 0
        if index == 0:
            self.head = None
        elif index == 1:
            current.next =None
        else:
            while current != None:
                current = current.next
                count += 1
                while count == (index - 1):
                    previous = current.next
                    current.next = previous.next
                    break

    def remove(self, item):
        '''
        删除指定元素
        :param item:
        :return:
        '''
        current = self.head
        while current != None:
            current = current.next
            if current.next.get_data() == item:
                current.next = current.next.next
                break

    def search(self, item):

        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.next
        return False

class SingleCycleLinkList():
    def __init__(self, node = None):
        self.head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 1
        if self.head == None:
            return 0
        else:
            while current.next != self.head:
                current = current.next
                count += 1
        return count

    def travel(self):
        if self.is_empty():
            print(None)
        else:
            current = self.head
            while current.next != self.head:
                print(current.get_data(), end=" ")
                current = current.next
            print(current.get_data())


    def add(self, item):
        '''
        头部添加元素
        :param item:
        :return:
        '''
        node = Node(item)
        current = self.head
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            while current.next != self.head:
                current = current.next
            node.next = self.head
            self.head = node
            current.next = self.head

    def append(self, item):
        '''
        尾部添加元素
        :param item:
        :return:
        '''
        current = self.head
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def insert(self, index, item):
        '''
        指定位置添加元素
        :param index:
        :param item:
        :return:
        '''
        current = self.head
        node = Node(item)
        count = 0
        if index == 0:
            self.add(item)
        elif index == 1:
            pre = self.head
            node.next = pre.next
            pre.next = node
        elif self.length() > index:
            while current.next != self.head:
                current = current.next
                count += 1
                while count == (index-1):
                    previous = current
                    node.next = previous.next
                    previous.next = node
                    break
        else:
            raise IndexError("Index is invalid", index)

    def remove(self, item):
        current = self.head
        while current.next != self.head:
            current = current.next
            if current.next.get_data() == item:
                current.next = current.next.next
                break

    def pop(self):
        '''
        弹出尾部元素
        :return:
        '''
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head

if __name__ == "__main__":
    # l1 = SingleLinkList()
    # l1.add(99)
    # l1.append(6)
    # l1.append(7)
    # l1.append(8)
    # l1.append(9)
    # l1.append(10)
    # l1.insert(3, 0)
    # print(l1.length())
    # l1.pop()
    # l1.remove(7)
    # l1.travel()
    # print(l1.search(9))
    # print(l1.get_head())

    l2 = SingleCycleLinkList()
    l2.add(3)
    l2.add(4)
    l2.add(5)
    l2.add(55)
    l2.append(6)
    l2.append(7)
    l2.insert(1,666)
    l2.remove(7)
    l2.pop()
    l2.travel()



