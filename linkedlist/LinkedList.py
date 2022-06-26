"""
Node represents the item in the linked List
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

"""
LinkedList data structure
"""


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    def insert(self, node: Node):
        if node is None:
            print("Can't add empty or none data into the LinkedList")
            return
        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def insert_at(self, position, node):
        if position < 0 or node is None:
            print("Invalid arguments passed")
        curr_pos = 1
        temp = self.head
        while curr_pos < position - 1 and temp is not None:
            temp = temp.next
            curr_pos += 1

        if curr_pos == 0:
            if self.head is not None:
                temp.next = self.head
            self.head = node

        if temp is None:
            if self.tail is not None:
                self.tail.next = node
            self.tail = node
        else:
            node.next = temp.next
            temp.next = node


def main():
    weekdays = LinkedList()
    weekdays.insert(Node("Monday"))
    weekdays.insert(Node("Tuesday"))
    weekdays.insert(Node("Thursday"))
    weekdays.insert_at(6, Node("Sat"))
    weekdays.insert_at(3, Node("Wed"))
    weekdays.insert_at(7, Node("Sunday"))
    weekdays.insert_at(5, Node("Friday"))
    weekdays.print()


if __name__ == "__main__":
    main()
