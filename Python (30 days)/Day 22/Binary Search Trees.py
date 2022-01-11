class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        self.height = 0
        nodes = [root]

        while nodes != []:
            new_nodes = []
            for i in range(len(nodes)):

                if nodes[i].left != None:
                    new_nodes.append(nodes[i].left)

                if nodes[i].right != None:
                    new_nodes.append(nodes[i].right)

            nodes = new_nodes
            self.height += 1

        return self.height - 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)