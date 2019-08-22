from treelib import Tree


class Node(object):
    def __init__(self, data):
        self.data = data


tree = Tree()
tree.create_node('root', 'root', data=Node('ROOT'))
tree.create_node('left', 'left', parent='root', data=Node('left'))
tree.create_node('middle', 'middle', parent='left', data=Node('middle'))
tree.create_node('right', 'right', parent='root', data=Node('right'))

tree.show()
print(tree.depth())
print(str(tree))