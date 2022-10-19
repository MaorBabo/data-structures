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


def _insert(root, key, data):
    """
    helper function for the method insert.
    :param root: binary search tree
    :param key: int
    :param data: some value
    :return: None
    """

    if key == root.key:
        root.data = data

    elif key < root.key:
        if root.left is None:
            root.left = TNode(key, data)

        _insert(root.left, key, data)

    else:
        if root.right is None:
            root.right = TNode(key, data)

        _insert(root.right, key, data)


def _minimum(root):
    """
    helper function for the method minimum
    :param root: binary search tree
    :return: key
    """

    if root.left is None:
        return root.key

    return _minimum(root.left)


def _depth(root):
    """
    helper function for the method depth
    :param root: binary search tree
    :return: int
    """

    if root is None:
        return -1

    return 1 + max(_depth(root.left), _depth(root.right))


def _maximum(root):
    """
    Helper function of the maximum method.
    :param root: Binary search tree.
    :return: The node that contain the max key.
    """

    if root.right is None:
        return root

    return _maximum(root.right)


def _len(root):
    """
    Helper function to the method __len__
    :param root: Binary search tree.
    :return: int
    """

    if root is None:
        return 0

    return 1 + _len(root.left) + _len(root.right)


class BinarySearchTree:

    def __init__(self, seq=None):
        """
        Creating Binary search tree
        :param seq: List[Tuple[key, data], ...]
        """
        self.root = None

        if seq is not None:
            for key, data in seq:
                self.insert(key, data)

    def lookup(self, key):
        """
        Looks for a given key
        :param key: int
        :return: True if found the ket None otherwise
        """

        # Calling for helper function
        return _lookup(self.root, key)

    def insert(self, key, data):
        """
        inserting data to an existing node
        with the given key or creating a new one.
        :param key: int
        :param data: some value
        :return: None
        """
        if self.root is None:
            self.root = TNode(key, data)
        _insert(self.root, key, data)

    def minimum(self):
        """
        finding the most minimal key in the tree
        :return: key
        """

        if self.root is None:
            return

        return _minimum(self.root)

    def maximum(self):
        """
        Finding the max key in the tree.
        :return: The node that contain the max key.
        """

        if self.root is None:
            return

        return _maximum(self.root)

    def depth(self):
        """
        calculating the depth of a binary tree
        :return: int
        """

        return _depth(self.root)

    def __len__(self):
        """
        find the number of nodes in the tree.
        :return: int
        """

        return _len(self.root)


tree = BinarySearchTree([(3, 'a'), (2, 'b'), (4, 'c'), (5, 'd')])
print(len(tree))
