import json
import os
from pyecharts import options as opts
from pyecharts.charts import Page, Tree
from treelib import Tree as json_tree


class Node(object):
    def __init__(self, data):
        self.data = data


tree = json_tree()
tree.create_node('root', 'root', data=Node('ROOT'))
tree.create_node('left', 'left', parent='root', data=Node('left'))
tree.create_node('middle', 'middle', parent='left', data=Node('middle'))
tree.create_node('right', 'right', parent='root', data=Node('right'))

tree.show()
tree_data = tree.to_json(sort=True, reverse=False)
print(tree_data)


# tree_file = open('./tree_json.json', 'w')
# tree_file.write(tree_data)


def tree_base() -> Tree:
    with open(os.path.join("tree_json.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    c = (
        Tree()
            .add("", [j], orient="TB", symbol="roundRect", symbol_size=[20, 10], label_opts={"color": "blue", "position": "top"})
            .set_global_opts(title_opts=opts.TitleOpts(title="Tree"))
    )
    return c


tree_base().render()
