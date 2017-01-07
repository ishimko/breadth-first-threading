from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.neighbour = None
        self.data = data


def example_tree():
    r"""
          1
         / \
        2   3
      /     / \
     4     6   7
    """
    _1 = tree = Node(1)
    _2 = _1.left = Node(2)
    _3 = _1.right = Node(3)
    _4 = _2.left = Node(4)
    _6 = _3.left = Node(6)
    _7 = _3.right = Node(7)

    return tree


def breadth_first_queue(node, node_func):
    queue = deque()
    queue.append(node)
    while queue:
        current_node = queue.popleft()
        node_func(current_node)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def breadth_first_neighbours(node, node_func):
    while node:
        line_start = node
        while node:
            node_func(node)
            node = node.neighbour
        node = line_start.left


def connect_neighbours(node):
    while node:
        previous_node = line_start = None
        while node:
            if node.left:
                line_start = process_node(node.left, previous_node, line_start)
                previous_node = node.left
            if node.right:
                line_start = process_node(node.right, previous_node, line_start)
                previous_node = node.right
            node = node.neighbour
        node = line_start


def process_node(node, previous_node, line_start):
    if not line_start:
        line_start = node
    else:
        previous_node.neighbour = node
    return line_start


def main():
    tree = example_tree()
    connect_neighbours(tree)

    breadth_first_queue_result = []
    breadth_first_queue(tree, lambda node: breadth_first_queue_result.append(node.data))

    breadth_first_neighbours_result = []
    breadth_first_neighbours(tree, lambda node: breadth_first_neighbours_result.append(node.data))

    assert breadth_first_neighbours_result == breadth_first_queue_result


if __name__ == '__main__':
    main()
