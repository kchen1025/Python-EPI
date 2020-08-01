from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def checkSym(sub1, sub2):
        if not sub1 and not sub2:
            return True
        elif sub1 and sub2:
            return (sub1.data==sub2.data and checkSym(sub1.right,sub2.left) and checkSym(sub1.left,sub2.right) )
        return False

    return not tree or checkSym(tree.left, tree.right)


if __name__ == '__main__':
    one = BinaryTreeNode(1)
    two = BinaryTreeNode(2)
    three = BinaryTreeNode(3)
    four = BinaryTreeNode(4)
    five = BinaryTreeNode(5)

    one.left = two
    one.right = four
    two.right = three
    four.right = five

    print(is_symmetric(one))

    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
