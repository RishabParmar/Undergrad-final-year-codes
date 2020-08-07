# Binary search tree and breadth first search


class BinaryTree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, node, data):
        if node.data:
            while True:
                if data <= node.data:
                    if node.left is None:
                        node.left = BinaryTree(data)
                        print("Inserted to the left", data)
                        break
                    else:
                        node = node.left
                        print("Left shift:", node.data)
                elif data > node.data:
                    if node.right is None:
                        node.right = BinaryTree(data)
                        print("Inserted to the right", data)
                        break
                    else:
                        node = node.right
                        print("Right shift:", node.data)
        else:
            self.data = data


root = BinaryTree(40)
root.insert(node=root, data=10)
root.insert(node=root, data=8)
root.insert(node=root, data=9)
root.insert(node=root, data=11)
root.insert(node=root, data=50)
print("Created the binary search tree!")

# Breadth First Search(BFS)

queue = [root]
while len(queue) != 0:
    obj = queue.pop(0)
    if obj.left is not None:
        queue.append(obj.left)
    if obj.right is not None:
        queue.append(obj.right)
    print(" -> ", obj.data, "")


