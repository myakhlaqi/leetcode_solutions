
# It creates a class called Node.
class Node:

    def __init__(self, val):
        """
        The first parameter of the function is self, which refers to the object itself. 

        The second parameter is val, which is the value to be stored in the node. 

        The third parameter is next, which is a pointer to the next node. 

        The fourth parameter is prev, which is a pointer to the previous node. 

        The data members __val, __next, and __prev are initialized to the values of the parameters val,
        next, and prev, respectively. 

        The data members __val, __next, and __prev are declared as private. 

        The data members __val, __next, and __prev are accessed using the getter and setter methods. 

        The getter and

        :param val: The value of the node
        """
        self.__val = val
        self.__next = None
        self.__prev = None

        #self.__prev= None
    def getVal(self):
        """
        The function getVal() returns the value of the private variable __val
        :return: The value of the private variable __val
        """
        return self.__val

    def setVal(self, v):
        self.__val = v

    # A getter method for the private variable __next.
    def getNext(self):
        return self.__next

    def setNext(self, n) -> None:
        self.__next = n

    def getPrev(self):
        return self.__prev

    def setPrev(self, n) -> None:
        self.__prev = n
    # A property decorator. It is a way to create a property in a class.
    val = property(getVal, setVal)
    # A property decorator. It is a way to create a property in a class.
    next = property(getNext, setNext)
    prev = property(getPrev, setPrev)


# It's a linked list class that has a head, size, and current node. It has a getSize method, a get
# method, an addAtHead method, an addAtTail method, an addAtIndex method, a deleteAtIndex method, a
# next method, an iter method, and a string method
class MyLinkedList:

    def __init__(self, *args):
        """
        The function takes in a list of integers and adds them to the linked list
        """
        self.__head = None
        self.__size = 0
        self.__current = None
        if args:
            for i in args:
                self.addAtTail(int(i))

    def getSize(self):
        """
        It returns the size of the square.
        :return: The size of the square.
        """
        return self.__size
    Size = property(getSize)

    def get_value(self, index: int) -> int:
        """
        If the head is not None, then we create a variable called current_node and set it equal to the
        head. We also create a variable called counter and set it equal to 0. Then we create a while
        loop that will run as long as current_node is not None. Inside the while loop, we check if the
        counter is equal to the index. If it is, then we return the value of the current node. If it
        isn't, then we set current_node equal to the next node and increment the counter by 1. If the
        head is None, then we return -1

        :param index: The index of the node you want to get the value from
        :type index: int
        :return: The value of the node at the given index.
        """
        if self.__head:
            current_node = self.__head
            counter = 0
            while current_node:
                if(counter == index):
                    return current_node.val
                current_node = current_node.next
                counter += 1
        return -1

    def get_node(self, index: int) -> Node:
        """
        If the head is not None, then we create a variable called current_node and set it equal to the
        head. We also create a variable called counter and set it equal to 0. Then we create a while
        loop that will run as long as current_node is not None. Inside the while loop, we check if the
        counter is equal to the index. If it is, then we return the value of the current node. If it
        isn't, then we set current_node equal to the next node and increment the counter by 1. If the
        head is None, then we return -1

        :param index: The index of the node you want to get the value from
        :type index: int
        :return: The value of the node at the given index.
        """
        if self.__head:
            current_node = self.__head
            counter = 0
            while current_node:
                if(counter == index):
                    return current_node
                current_node = current_node.next
                counter += 1
        return None

    def addAtHead(self, val: int) -> None:
        """
        It adds a new node at the head of the linked list.

        :param val: int
        :type val: int
        """
        """
        It adds a new node at the head of the linked list.
        
        :param val: int
        :type val: int
        """
        new_node = Node(val)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def addAtTail(self, val: int) -> None:
        """
        It adds a new node at the end of the linked list.

        :param val: the value to add to the end of the list
        :type val: int
        """

        new_node = Node(val)
        if self.__head:
            current_node = self.__head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.__head = new_node
        self.__size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        If the index is out of bounds, do nothing. If the index is 0, add to the head. If the index is the
        size of the list, add to the tail. Otherwise, find the node at the index - 1, and add the new node
        after it

        :param index: the position you want to insert the new node
        :type index: int
        :param val: the value to add
        :type val: int
        :return: The return value is the value of the node at the given index.
        """
        # sourcery skip: extract-method
        if index > self.__size or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.__size:
            self.addAtTail(val)
        else:
            current_node = self.__head
            counter = 0
            while counter < index - 1:
                current_node = current_node.next
                counter += 1
            new_node = Node(val)
            new_node.next = current_node.next
            current_node.next = new_node
        self.__size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        If the index is valid, then we set the next pointer of the node at index-1 to the node at index+1

        :param index: the position of the element to delete. Counting starts at 0
        :type index: int
        :return: The return value is the value of the node at the given index.
        """
        if index >= self.__size or index < 0:
            return
        if(index == 0):
            self.__head = self.__head.next
        else:
            current_node = self.__head
            counter = 0
            while counter < index - 1:
                current_node = current_node.next
                counter += 1
            if(index == self.__size - 1):
                current_node.next = None
            else:
                current_node.next = current_node.next.Next
        self.__size -= 1

    def __next__(self):
        if self.__current:
            value = self.__current.val
            self.__current = self.__current.next
            return value
        else:
            raise StopIteration

    def __iter__(self):
        self.__current = self.__head
        return self

    def __str__(self) -> str:  # sourcery skip: use-fstring-for-formatting
        return ("[{}]".format(",".join([str(x) for x in iter(self)])))

    def get_tail(self) -> Node:
        tail = None
        curr = self.__head
        while curr:
            tail = curr
            curr = curr.next
        return tail

    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head
    head = property(get_head, set_head)


class MyDLinkedList:

    def __init__(self, *args):
        """
        The function takes in a list of integers and adds them to the linked list
        """
        self.__head = None
        self.__size = 0
        self.__current = None
        if args:
            for i in args:
                self.addAtTail(int(i))

    def getSize(self):
        """
        It returns the size of the square.
        :return: The size of the square.
        """
        return self.__size
    Size = property(getSize)

    def get_value(self, index: int) -> int:
        """
        If the head is not None, then we create a variable called current_node and set it equal to the
        head. We also create a variable called counter and set it equal to 0. Then we create a while
        loop that will run as long as current_node is not None. Inside the while loop, we check if the
        counter is equal to the index. If it is, then we return the value of the current node. If it
        isn't, then we set current_node equal to the next node and increment the counter by 1. If the
        head is None, then we return -1

        :param index: The index of the node you want to get the value from
        :type index: int
        :return: The value of the node at the given index.
        """
        if self.__head:
            current_node = self.__head
            counter = 0
            while current_node:
                if(counter == index):
                    return current_node.val
                current_node = current_node.next
                counter += 1
        return -1

    def get_node(self, index: int) -> Node:
        """
        If the head is not None, then we create a variable called current_node and set it equal to the
        head. We also create a variable called counter and set it equal to 0. Then we create a while
        loop that will run as long as current_node is not None. Inside the while loop, we check if the
        counter is equal to the index. If it is, then we return the value of the current node. If it
        isn't, then we set current_node equal to the next node and increment the counter by 1. If the
        head is None, then we return -1

        :param index: The index of the node you want to get the value from
        :type index: int
        :return: The value of the node at the given index.
        """
        if self.__head:
            current_node = self.__head
            counter = 0
            while current_node:
                if(counter == index):
                    return current_node
                current_node = current_node.next
                counter += 1
        return None

    def addAtHead(self, val: int) -> None:
        """
        It adds a new node at the head of the linked list.

        :param val: int
        :type val: int
        """
        """
        It adds a new node at the head of the linked list.
        
        :param val: int
        :type val: int
        """
        new_node = Node(val)
        new_node.next = self.__head
        new_node.prev = None
        if self.__head:
            self.__head.prev = new_node
        self.__head = new_node
        self.__size += 1

    def addAtTail(self, val: int) -> None:
        """
        It adds a new node at the end of the linked list.

        :param val: the value to add to the end of the list
        :type val: int
        """

        new_node = Node(val)
        new_node.next = None
        new_node.prev = None
        if self.__head:
            current_node = self.__head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
        else:
            self.__head = new_node
        self.__size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        If the index is out of bounds, do nothing. If the index is 0, add to the head. If the index is the
        size of the list, add to the tail. Otherwise, find the node at the index - 1, and add the new node
        after it

        :param index: the position you want to insert the new node
        :type index: int
        :param val: the value to add
        :type val: int
        :return: The return value is the value of the node at the given index.
        """
        # sourcery skip: extract-method
        if index > self.__size or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.__size-1:
            self.addAtTail(val)
        else:
            current_node = self.__head
            counter = 0
            while counter < index - 1:
                current_node = current_node.next
                counter += 1
            new_node = Node(val)
            new_node.next = current_node.next
            new_node.prev = current_node

            current_node.next.prev = new_node
            current_node.next = new_node

        self.__size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        If the index is valid, then we set the next pointer of the node at index-1 to the node at index+1

        :param index: the position of the element to delete. Counting starts at 0
        :type index: int
        :return: The return value is the value of the node at the given index.
        """
        if index >= self.__size or index < 0:
            return
        if(index == 0):
            if(self.__head.next):
                self.__head.next.prev = None
            self.__head = self.__head.next
        else:
            current_node = self.__head
            counter = 0
            while counter < index - 1:
                current_node = current_node.next
                counter += 1
            if(index == self.__size - 1):
                current_node.next = None
            else:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
        self.__size -= 1

    def __next__(self):
        if self.__current:
            value = self.__current.val
            self.__current = self.__current.next
            return value
        else:
            raise StopIteration

    def __iter__(self):
        self.__current = self.__head
        return self

    def __str__(self) -> str:  # sourcery skip: use-fstring-for-formatting
        return ("[{}]".format(",".join([str(x) for x in iter(self)])))

    def get_tail(self) -> Node:
        tail = None
        curr = self.__head
        while curr:
            tail = curr
            curr = curr.next
        return tail

    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head
    head = property(get_head, set_head)
# Your MyLinkedList object will be instantiated and called as such:

# obj = MyLinkedList(*[1,2,3,4,5,6])
# # print(obj)
# print(obj.get_tail().Value)
# obj.addAtIndex(3,0)
# print(obj)
# obj.deleteAtIndex(2)
# print(obj)
# obj.addAtHead(6)
# print(obj)
# obj.addAtTail(4)
# print(obj)
# print(obj.get_value(4))
# # obj = MyLinkedList(*[1,2,3,4,5])
# # print(obj)
# # for i in range(5):
# #     obj.deleteAtIndex(i)
# #     #print("{}:{},".format(i, obj.get(i)))
# #     print(obj)
