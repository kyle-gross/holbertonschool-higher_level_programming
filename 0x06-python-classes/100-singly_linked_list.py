#!/usr/bin/python3
"""This module contains the class Node which defines
   a node of a singly linked list
"""


class Node:
    """This class creates nodes for a singly linked list"""

    def __init__(self, data, next_node=None):
        """This method constructs a node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class creates singly linked lists"""
    def __init__(self):
        """Constructs a linked list object"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node in a linked list ordered by value"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        temp = self.__head
        if value <= temp.data:
            new_node.next_node = temp
            self.__head = new_node
            return

        while temp.next_node:
            if temp.next_node.data > value:
                break
            temp = temp.next_node

        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """returns string version of self"""
        data = []
        current = self.__head
        while current is not None:
            data.append(current.data)
            current = current.next_node
        return "%s" % ('\n'.join(str(i) for i in data))
