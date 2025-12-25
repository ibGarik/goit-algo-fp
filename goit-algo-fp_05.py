import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color_gradient(n, start_hex, end_hex):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    
    color_list = []
    
    for i in range(n):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (n - 1))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (n - 1))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (n - 1))
        color_list.append(rgb_to_hex((r, g, b)))
        
    return color_list

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def dfs_visualize(root):
    if root is None:
        return

    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes, "#330066", "#DDA0DD")
    
    stack = [root]
    visited_order = []
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    for i, node in enumerate(visited_order):
        node.color = colors[i]
        
    draw_tree(root, "DFS (Глибина)")

def bfs_visualize(root):
    if root is None:
        return

    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes, "#00008B", "#87CEFA")

    queue = collections.deque([root])
    visited_order = []
    
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for i, node in enumerate(visited_order):
        node.color = colors[i]

    draw_tree(root, "BFS (Ширина)")

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(2)

dfs_visualize(root)
bfs_visualize(root)