class Sorting:
    def __init__(self, a_list):
        self.a_list = a_list

    def bubble_sort(self):
        '''
        冒泡排序
        :return:
        '''
        for i in range(len(self.a_list) - 1):
            stop = False
            while not stop:
                for j in range(len(self.a_list) - 1 - i):
                    stop = True
                    if self.a_list[j + 1] < self.a_list[j]:
                        self.a_list[j], self.a_list[j + 1] = self.a_list[j+ 1], self.a_list[j]  # trick:利用下标对元素进行交换
                        stop = False

    def select_sort(self):
        '''
        选择排序
        :return:
        '''
        for i in range(len(self.a_list)-1):
            min_index = i
            for j in range(i+1, len(self.a_list)):
                if self.a_list[min_index] > self.a_list[j]:
                    min_index = j                          # 找到最小值对应的index
            self.a_list[min_index], self.a_list[i] = self.a_list[i], self.a_list[min_index]

    def insertion_sort(self):
        '''
        插入排序
        :return:
        '''
        for i in range(1, len(self.a_list)):
            for j in range(i, 0, -1):
                if self.a_list[j] < self.a_list[j-1]:
                    self.a_list[j], self.a_list[j-1] = self.a_list[j-1], self.a_list[j]

    def shell_sort(self):
        '''
        希尔排序
        :return:
        '''
        gap = len(self.a_list) // 2
        while gap > 0:
            for i in range(gap, len(self.a_list)):
                # i = [gap, gap+1, ... n-1]
                for j in range(i, 0, -gap):
                    # j = [i, i-gap]
                    if self.a_list[j] < self.a_list[j-gap]:
                        self.a_list[j], self.a_list[j-gap] = self.a_list[j-gap], self.a_list[j]
            gap = gap // 2

    def quick_sort(self, left=0, right=None):
        '''
        快速排序
        :return:
        '''
        if right == None:
            right = len(self.a_list)-1
        low = left
        high = right
        if left >= right:       # 递归的退出条件
            return
        temp = self.a_list[left]
        while low != high:
            while self.a_list[high] >= temp and low < high:
                high -= 1
            while self.a_list[low] <= temp and low < high:
                low += 1
            self.a_list[high], self.a_list[low] = self.a_list[low], self.a_list[high]

        self.a_list[left], self.a_list[low] = self.a_list[low], temp
        # 剩余进行递归
        self.quick_sort(left, low-1)
        self.quick_sort(low+1,right)

    def merge_sort(self, a_list):
        '''
        归并排序
        :return:
        '''
        n = len(a_list)
        if n <= 1:
            return a_list
        mid = n // 2
        left_list = self.merge_sort(a_list[:mid])
        right_list = self.merge_sort(a_list[mid:])

        left_pointer, right_pointer = 0, 0
        sort_list = []

        while left_pointer < len(left_list) and right_pointer < len(right_list):
            if left_list[left_pointer] < right_list[right_pointer]:
                sort_list.append(left_list[left_pointer])
                left_pointer += 1
            else:
                sort_list.append(right_list[right_pointer])
                right_pointer += 1
        sort_list += left_list[left_pointer:]
        sort_list += right_list[right_pointer:]

        return sort_list


if __name__ == "__main__":

    li = [6, 7, 9, 4, 5, 3, 1]
    l = Sorting(li)
    print(li)
    # l.bubble_sort()
    # l.select_sort()
    # l.insertion_sort()
    # l.shell_sort()
    # l.quick_sort()
    l.merge_sort(li)
    print(l.merge_sort(li))





