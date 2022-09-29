class TNode:

    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key) + ': ' + str(self.data)


def _lookup(root, key):
    """
    This is helper function for the lookup method.
    :param root: pointer to a binary search tree
    :param key: int
    :return: optional(True/None)
    """
    if root is None:
        return

    if root.key == key:
        return True

    elif root.key < key:
        return _lookup(root.right, key)

    else:
        return _lookup(root.left, key)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def lookup(self, key):
        """
        Looks for a given key
        :param key: int
        :return: True if found the ket None otherwise
        """

        # Calling for helper function
        return _lookup(self.root, key)


