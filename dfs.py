from stack import Stack


class GNode:

    def __init__(self, key, data=0, neighbors=None):
        self.key = key
        self.data = data
        self.neighbors = neighbors
        self.visited = False

    def __str__(self):
        return ['key = ' + str(self.key) + ': ' + str(self.data)]


class Graph:

    def __init__(self, head):
        self.head = head
        self.stack = Stack()


def _Dfs_helper(graph, tmp, path):
    """
    This is a helper function to the Dfs function.
    :param tmp: GNode
    :return: path (list[str])
    """

    # If the graph is empty or if we passed over every node:
    if tmp is None:
        # returning the final path:
        return path

    # Marking the node as visited:
    tmp.visited = True

    # Adding the key of the node to the path:
    path.append(tmp.key)

    # Pushing the node to the stack:
    graph.stack.push(tmp)

    # Popping out the node after we passed over its neighbors:
    if tmp.neighbors is None:
        graph.stack.pop()

    if tmp.neighbors:

        # Iterating over every neighbor of the node:
        for neighbor in tmp.neighbors:
            _Dfs_helper(graph, neighbor, path)

    return path


def Dfs(graph):
    """
    This function implements the
    dfs(dreath first search) algorithm.
    :param graph: Graph
    :return: path (list[str])
    """

    # Saving the head in a variable:
    tmp = graph.head

    return _Dfs_helper(graph, tmp, [])


if __name__ == '__main__':

    # Define the nodes of the graph:
    g1 = GNode('O', 1)
    g2 = GNode('R', 2)
    g3 = GNode('M', 3, [g1])
    g4 = GNode('A', 4, [g2])

    # The main node of the graph:
    head1 = GNode('Name: ', 0, [g3, g4])

    # Define the graph:
    graph1 = Graph(head1)

    # Printing the result(the path):
    print(Dfs(graph1))