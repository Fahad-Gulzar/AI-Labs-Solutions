# Define the tree as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Depth Limited Search (DLS)
def depth_limited_search(start, goal, limit):
    if start == goal:
        return True
    if limit <= 0:
        return False

    for neighbor in graph.get(start, []):
        if depth_limited_search(neighbor, goal, limit - 1):
            return True
    return False

# Iterative Deepening Depth First Search (IDDFS)
def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if depth_limited_search(start, goal, depth):
            print(f"Goal node '{goal}' found at depth {depth}")
            return True
    print(f"Goal node '{goal}' not found within depth {max_depth}")
    return False

# Example usage:
start_node = 'A'
goal_node = 'G'
max_depth = 5

print("\n--- Depth Limited Search (DLS) with depth = 3 ---")
result_dls = depth_limited_search(start_node, goal_node, 3)
print(f"DLS result: {'Found' if result_dls else 'Not Found'}")

print("\n--- Iterative Deepening DFS (IDDFS) ---")
result_iddfs = iddfs(start_node, goal_node, max_depth)
print(f"IDDFS result: {'Found' if result_iddfs else 'Not Found'}")