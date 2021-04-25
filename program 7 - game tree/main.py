import sys


class Node:
    def __init__(self, data, andor):
        self.left = None
        self.right = None
        self.data = data
        self.andor = andor

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def fill_tree(node):
    ready = True if node.left.data != -1 else False
    if not ready:
        fill_tree(node.left)
        fill_tree(node.right)

    l = node.left.data
    r = node.right.data

    if node.andor == "and":
        node.data = l & r
    else:
        node.data = l | r

    return node


def build_tree(n, leaf_list):
    root = Node(-1, "and")

    curr = "or"
    curr_leaves = [root]

    for level in range(n):
        temp = []
        for leaf in curr_leaves:
            left = Node(-1, curr)
            right = Node(-1, curr)
            leaf.left = left
            leaf.right = right
            temp.append(left)
            temp.append(right)
        if curr == "or":
            curr = "and"
        else:
            curr = "or"
        curr_leaves = temp

    for i in range(len(curr_leaves)):
        curr_leaves[i].data = leaf_list[i]

    root = fill_tree(root)

    return root


def expected_leaves(node):
    l = node.left.data
    r = node.right.data
    leaf = True if not node.left.left else False

    if leaf:
        if node.andor == "and":
            if l == 0 and r == 0:
                return 1
            elif l == 1 and r == 1:
                return 2
            else:
                return 1.5
        else:
            if l == 0 and r == 0:
                return 2
            elif l == 1 and r == 1:
                return 1
            else:
                return 1.5

    if node.andor == "and":
        if l == 0 and r == 0:
            return 0.5 * expected_leaves(node.left) + 0.5 * expected_leaves(node.right)
        elif l == 1 and r == 1:
            return expected_leaves(node.left) + expected_leaves(node.right)
        else:
            if l == 1:
                return 0.5 * (expected_leaves(node.left) + expected_leaves(node.right)) + 0.5 * expected_leaves(node.right)
            else:
                return 0.5 * (expected_leaves(node.left) + expected_leaves(node.right)) + 0.5 * expected_leaves(node.left)
    else:
        if l == 0 and r == 0:
            return expected_leaves(node.left) + expected_leaves(node.right)
        elif l == 1 and r == 1:
            return 0.5 * expected_leaves(node.left) + 0.5 * expected_leaves(node.right)
        else:
            if r == 1:
                return 0.5 * (expected_leaves(node.left) + expected_leaves(node.right)) + 0.5 * expected_leaves(
                    node.right)
            else:
                return 0.5 * (expected_leaves(node.left) + expected_leaves(node.right)) + 0.5 * expected_leaves(
                    node.left)


for line in sys.stdin:
    n = int(line.rstrip())
    break

for line in sys.stdin:
    leaves = line.rstrip()
    break

leaf_list = []

for leaf in leaves:
    leaf_list.append(int(leaf))


root = build_tree(n, leaf_list)

print(expected_leaves(root))
