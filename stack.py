"""
This file implements the Stack class.
"""


class Stack:

    def __init__(self):
        self.__stack = []
        self.__size = 0

    def __repr__(self):
        s = 'Stack: '
        for item in self.__stack[::-1]:
            s += str(item) + ' -> '

        return s[:-3] + ', Size: ' + str(self.__size)

    def push(self, item):
        """
        This method pushes items to the head of the stack.
        :param item: Some value.
        :return: None.
        """
        self.__stack.append(item)
        self.__size += 1

    def pop(self):
        """
        This method pops out the item in the head of the stack.
        :return: item
        """
        if self.is_empty():
            raise Exception('Stack is empty!')

        result = self.__stack[self.__size - 1]
        self.__stack = self.__stack[0: self.__size - 1]
        self.__size -= 1
        return result

    def is_empty(self):
        """
        This method checks if the stack is empty.
        :return: boolean value (True/False).
        """
        return self.__size == 0

    def top(self):
        """
        This method returns the value of the item placed the top of the stack.
        :return: Some value or an Error message if the stack is empty.
        """
        if self.is_empty():
            raise Exception('There are no items in the stack!')

        return self.__stack[self.__size - 1]

    def sort_stack(self):
        """
        This method sort the items in
        the stack from lowest to biggest.
        :return: sorted stack.
        """
        stk = Stack()

        while not self.is_empty():
            temp = self.pop()

            while not stk.is_empty() and stk.top() > temp:
                self.push(stk.pop())

            stk.push(temp)
        return stk


