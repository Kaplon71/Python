import os
import re
import random
import unittest

def count_Files(path):
    number_of_files = len(os.listdir(path))
    print('the number of files is ' + str(number_of_files))
    return number_of_files

def tree_Req(path):
    a = os.listdir(path)
    print('Files found in path: ' + path + ': ' + str(a))
    for files in a:
        new_path = path + "/" + files
        if os.path.isdir(new_path):
            tree_Req(new_path)

def delete_Word(word, text):
    return text.replace(word,'')

def delete_Word_Re(word, text):
    target = re.compile(word)
    text = target.sub('', text)
    return text

def replace_Word(replacement, text):
    for key, value in replacement.items():
        text = text.replace(key, value)
    return text

def replace_Word_Re(replacement, text):
    for key, value in replacement.items():
        target = re.compile(key)
        text = target.sub(value, text)
    return text

def bogo_Sort(a):
    while is_Sorted(a) == False:
        shuffle(a)
    return a

def bozo_Sort(a):
    n = len(a)
    while is_Sorted(a) == False:
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        a[r1], a[r2] = a[r2], a[r1]
    return a

def is_Sorted(a):
    for i in range(0, len(a)-1):
        if (a[i] > a[i+1]):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]



class treeNode:
    def __init__(self, value=None):
        self.value = value
        self.edges = {}
        self.children = []

    def add_child(self, node, edge_value=None):
        self.children.append(node)
        self.edges[node] = edge_value

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child, edge_value in self.edges.items():
            ret += "\t" * (level + 1) + f"[edge: {edge_value}]\n"
            ret += child.__str__(level + 1)
        return ret

class tree:
    def __init__(self, root=None):
        self.root = root

    def traverse(self):
        return self._traverse_recursive(self.root)

    def _traverse_recursive(self, node):
        if node is None:
            return []
        nodes = [node.value]
        for child in node.children:
            nodes.extend(self._traverse_recursive(child))
        return nodes

    def __str__(self):
        return str(self.root) if self.root else "<Empty Tree>"

class testTree(unittest.TestCase):
    def setUp(self):
        self.root = treeNode("root")
        self.child1 = treeNode("child1")
        self.child2 = treeNode("child2")
        self.child1_1 = treeNode("child1_1")
        self.child1_2 = treeNode("child1_2")
        self.child2_1 = treeNode("child2_1")

        self.root.add_child(self.child1, "edge_root_child1")
        self.root.add_child(self.child2, "edge_root_child2")
        self.child1.add_child(self.child1_1, "edge_child1_child1_1")
        self.child1.add_child(self.child1_2, "edge_child1_child1_2")
        self.child2.add_child(self.child2_1, "edge_child2_child2_1")

        self.tree = tree(self.root)

    def test_traverse(self):
        expected_traversal = ["root", "child1", "child1_1", "child1_2", "child2", "child2_1"]
        result = self.tree.traverse()
        self.assertEqual(result, expected_traversal)

    def test_str_representation(self):
        tree_str = str(self.tree)
        self.assertIn("root", tree_str)
        self.assertIn("child1", tree_str)
        self.assertIn("edge_root_child1", tree_str)
        self.assertIn("edge_child1_child1_1", tree_str)

    def test_edge_values(self):
        self.assertEqual(self.root.edges[self.child1], "edge_root_child1")
        self.assertEqual(self.root.edges[self.child2], "edge_root_child2")
        self.assertEqual(self.child1.edges[self.child1_1], "edge_child1_child1_1")

    def test_empty_tree(self):
        empty_tree = tree()
        self.assertEqual(str(empty_tree), "<Empty Tree>")


if __name__ == "__main__":
    unittest.main()
    path = '/Users/tm1pl/Desktop/mPyton'
    #count_Files(path)
    #tree_Req(path)




    replacement = dict()
    replacement['bear'] = 'badger'
    replacement['notBear'] = 'notBadger'

    text = "bear bear notBear definetlyNotBear"

    text = replace_Word(replacement, text)
    print(text)
    text = delete_Word('definetlyNotBear', text)
    print(text)

    text = replace_Word_Re(replacement, text)
    print(text)
    text = delete_Word_Re('definetlyNotBear', text)
    print(text)


    max = 10
    random_Array = []
    for i in range(0, max):
        random_Array.append(random.randint(0, 100))
    print(random_Array)

    array1 = bogo_Sort(random_Array)
    array2 = bozo_Sort(random_Array)
    print(array1)
    print(array2)