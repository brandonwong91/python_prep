class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def list_print(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def insert_beginning(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode

    def insert_end(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def insert_between(self, middle_node, newdata):
        if middle_node is None:
            print("Empty Node")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def remove_node(self, remove_key):
        HeadVal = self.headval

        if HeadVal is not None:
            if HeadVal.dataval == remove_key:
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while HeadVal is not None:
            if HeadVal.dataval == remove_key:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if HeadVal == None:
            return

        prev.nextval = HeadVal.nextval
        HeadVal = None


######################

list1 = LinkedList()
list1.headval = Node("Lorem")
node2 = Node("ipsum")
node3 = Node("dolor")
list1.headval.nextval = node2
node2.nextval = node3

print("Default String:")
list1.list_print()

print("Insert Beginning:")
list1.insert_beginning("Begin")
list1.list_print()

print("Insert End:")
list1.insert_end("End")
list1.list_print()

print("Insert In Between:")
list1.insert_between(list1.headval.nextval, "between")
list1.list_print()

print("Removing: between")
list1.remove_node("between")
list1.list_print()