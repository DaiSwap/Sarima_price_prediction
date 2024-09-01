def dls(node, goal, depth):

  if depth == 0:
    return False

  if node == goal:
    return True

  for neighbor in graph[node]:
    if dls(neighbor, goal, depth - 1):
      return True

  return False


# Example usage:

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': [],
  'F': [],
  'G': [],
}

start_node = 'A'
goal_node = 'G'
depth_limit = 3

if dls(start_node, goal_node, depth_limit):
  print('Goal node found!')
else:
  print('Goal node not found.')
  
dls(start_node,goal_node,depth_limit)  