"""
This file implement the Queue structure.
"""


class Queue:

    def __init__(self, max_size, size=0, front=0, tail=0):
        self.__max_size = max_size
        self.__queue = [None] * max_size
        self.__size = size
        self.__front = front
        self.__tail = tail

    def __repr__(self):
        s = ''
        for i in range(self.__size):
            index = int((self.__front + i) % self.__max_size)
            s += str(self.__queue[index]) + ', '
        return s[:-2]

    def enqueue(self, item):
        """
        This method put the input value in the end of the queue.
        :param item: some value.
        :return: None
        """
        if self.is_full():
            raise Exception('The queue is full!')

        self.__queue[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def dequeue(self):
        """
        This method pops out the firs value in the queue.
        :return: None
        """
        if self.is_empty():
            raise Exception('The queue is empty!')

        print(self.__queue[self.__front], 'is removed!')
        self.__front = int((self.__front + 1) % self.__max_size)
        self.__size -= 1
        # We don't actually remove the items but the items will be override.

    def is_empty(self):
        """
        This method checks if the queue is empty.
        :return: boolean expression (True/False).
        """

        return self.__size == 0

    def is_full(self):
        """
        This method checks if the queue is full.
        :return: boolean expression (True/False).
        """

        return self.__size == self.__max_size


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class NQueue:
    """
    This class implement queue using linked list and nodes.
    """

    def __init__(self, front=None, tail=None):
        self.__front = front
        self.__tail = tail

    def __repr__(self):
        if self.is_empty():
            return '[]'
        s = '['
        tmp = self.__front

        while tmp is not None:
            s += str(tmp.data) + ', '
            tmp = tmp.next

        return s[:-2] + ']'

    def is_empty(self):
        return self.__front is None

    def enqueue(self, item):
        new = Node(item)

        if self.is_empty():
            self.__front = self.__tail = new

        else:
            self.__tail.next = new
            self.__tail = new

    def dequeue(self):
        if self.is_empty():
            raise Exception('The queue is empty!')

        else:
            tmp = self.__front.data
            self.__front = self.__front.next

        if self.__front is None:
            self.__tail = None

        return tmp
