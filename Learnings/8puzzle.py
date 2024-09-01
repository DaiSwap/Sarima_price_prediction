from collections import deque

def is_goal_state(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Define your goal state here
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = find_empty_space(state)
    
    if empty_col > 0:
        neighbor_left = [row[:] for row in state]
        neighbor_left[empty_row][empty_col], neighbor_left[empty_row][empty_col - 1] = neighbor_left[empty_row][empty_col - 1], neighbor_left[empty_row][empty_col]
        neighbors.append((neighbor_left, "left"))

    if empty_col < 2:
        neighbor_right = [row[:] for row in state]
        neighbor_right[empty_row][empty_col], neighbor_right[empty_row][empty_col + 1] = neighbor_right[empty_row][empty_col + 1], neighbor_right[empty_row][empty_col]
        neighbors.append((neighbor_right, "right"))

    if empty_row > 0:
        neighbor_up = [row[:] for row in state]
        neighbor_up[empty_row][empty_col], neighbor_up[empty_row - 1][empty_col] = neighbor_up[empty_row - 1][empty_col], neighbor_up[empty_row][empty_col]
        neighbors.append((neighbor_up, "up"))

    if empty_row < 2:
        neighbor_down = [row[:] for row in state]
        neighbor_down[empty_row][empty_col], neighbor_down[empty_row + 1][empty_col] = neighbor_down[empty_row + 1][empty_col], neighbor_down[empty_row][empty_col]
        neighbors.append((neighbor_down, "down"))

    return neighbors

def find_empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def solve_puzzle(initial_state):
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if is_goal_state(current_state):
            return path

        for neighbor_state, move in get_neighbors(current_state):
            if neighbor_state not in (state for state, _ in queue):
                queue.append((neighbor_state, path + [(neighbor_state, move)]))

    return None

def print_solution_path(solution_path):
    if solution_path:
        print("Solution Found:")
        for step, (state, move) in enumerate(solution_path):
            print(f"Step {step + 1}: Move {move}")
            for row in state:
                print(row)
            print("-----")
    else:
        print("No solution found!")

initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
solution_path = solve_puzzle(initial_state)
print_solution_path(solution_path)
