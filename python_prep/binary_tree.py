class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert_node(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data


    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)
        if self.right:
            print self.right.print_tree()

    # Left -> Root -> Right
    def in_order_traversal(self, root):
        result = []
        if root:
            result = self.in_order_traversal(root.left)
            result.append(root.data)
            result = result + self.in_order_traversal(root.right)
        return result

    # Root -> Left -> Right
    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result

    # Left -> Right -> Root
    def postorder_traversal(self, root):
        result = []
        if root:
            result = result + self.postorder_traversal(root.left)
            result = result + self.postorder_traversal(root.right)
            result.append(root.data)
        return result

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " not found in tree"
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return str(data) + " not found in tree"
            return self.right.find(data)
        else:
            print(str(self.data) + " is found!")


root = Tree(25)
root.insert_node(15)
root.insert_node(50)
root.insert_node(10)
root.insert_node(22)
root.insert_node(35)
root.insert_node(70)
root.insert_node(4)
root.insert_node(12)
root.insert_node(18)
root.insert_node(24)
root.insert_node(31)
root.insert_node(44)
root.insert_node(66)
root.insert_node(90)

root.print_tree()
print ("""
            25
      15          50
  10     22    35    70
4   12 18 24 31 44 66 90
""")


print(root.in_order_traversal(root))

print(root.preorder_traversal(root))

print(root.postorder_traversal(root))

root.find(31)