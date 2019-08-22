from _collections_abc import Iterator


class MultiNode(object):
    """构造节点结构，提供接口"""

    def __init__(self, element=None, *sibling_node):
        self.element = element
        self.sibling_node = sibling_node

    def get_element(self):
        """返回节点值"""
        return self.element

    def dict_form(self):
        """将节点按字典形式返回"""
        # 判断sibling_node是否为迭代对象
        # print(self.sibling_node[0])
        if not isinstance(self.sibling_node[0], Iterator):
            # 将sibling数组转换为字典
            key_list = []
            num = 1
            # print(len(self.sibling_node[0]))
            while num <= len(self.sibling_node[0]):
                # print(num)
                key_list.append('sibling%d' % num)
                num += 1
            dict_set = dict(zip(key_list, self.sibling_node[0]))
            dict_set["element"] = self.element
        else:
            dict_set = {
                "element": self.element
            }
        return dict_set

    def __str__(self):
        return str(self.element)


class MultiTree:
    def __init__(self, tree_node=None):
        self.root = tree_node

    def set_up_from_dict(self, dict_instance):
        if not isinstance(dict_instance, dict):
            return None
        else:
            node_queue = []
            dict_queue = []
            node = MultiNode(dict_instance["element"])
            self.root = node
            node_queue.append(node)
            dict_queue.append(dict_instance)
            while len(dict_queue):
                dict_in = dict_queue.pop(0)
                node = node_queue.pop(0)
                if isinstance(dict_in.get("sibling1", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("sibling1", None), dict):
                        dict_queue.append(dict_in.get("sibling1", None))
                        left_node = MultiNode(dict_in.get("sibling1", None)["element"])
                        node_queue.append(left_node)
                    else:
                        left_node = MultiNode(dict_in.get("sibling1", None))
                    node.left = left_node

                if isinstance(dict_in.get("sibling2", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("sibling2", None), dict):
                        dict_queue.append(dict_in.get("sibling2", None))
                        right_node = MultiNode(dict_in.get("sibling2", None)["element"])
                        node_queue.append(right_node)
                    else:
                        right_node = MultiNode(dict_in.get("sibling2", None))
                    node.right = right_node


node_a = MultiNode('A', ['B', 'C'])
print(node_a.dict_form())
print(MultiTree().set_up_from_dict(node_a.dict_form()))
