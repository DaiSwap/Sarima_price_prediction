class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def depth_limited_search(node, target, depth_limit):
    return dfs(node, target, depth_limit)

def dfs(node, target, depth_limit):
    if depth_limit == 0:
        return None
    if node.data == target:
        return node
    for child in node.children:
        result = dfs(child, target, depth_limit - 1)
        if result is not None:
            return result
    return None

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6), Node(7)]

target_value = 5
depth_limit = 3

result_node = depth_limited_search(root, target_value, depth_limit)

if result_node:
    print(f"Target {target_value} found in the tree")
else:
    print(f"Target {target_value} not found within the depth limit")
