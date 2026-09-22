from collections import deque
import time

# Same graph is used for both BFS and DFS
# Total nodes = 17
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': ['P'],
    'P': ['Q'],
    'Q': []
}


def bfs(start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# Start and goal nodes
start = 'A'
goal = 'Q'


# Run BFS and DFS only when this file is executed directly
if __name__ == "__main__":

    # Number of trials
    trials = 3

    # Number of runs per trial
    runs_per_trial = 10000

    bfs_times = []
    dfs_times = []

    # BFS - 3 trials
    for trial in range(trials):
        start_time = time.perf_counter()

        for _ in range(runs_per_trial):
            bfs_nodes = bfs(start, goal)

        end_time = time.perf_counter()

        bfs_runtime = (end_time - start_time) * 1000
        bfs_times.append(bfs_runtime)

    # DFS - 3 trials
    for trial in range(trials):
        start_time = time.perf_counter()

        for _ in range(runs_per_trial):
            dfs_nodes = dfs(start, goal)

        end_time = time.perf_counter()

        dfs_runtime = (end_time - start_time) * 1000
        dfs_times.append(dfs_runtime)

    # Results
    print("Total Nodes: 17")
    print("Start Node:", start)
    print("Goal Node:", goal)
    print()

    print("BFS Nodes Expanded:", bfs_nodes)

    for i in range(trials):
        print("BFS Trial", i + 1, "Runtime:", bfs_times[i], "ms")

    print("BFS Average Runtime:",
          sum(bfs_times) / trials, "ms")

    print()

    print("DFS Nodes Expanded:", dfs_nodes)

    for i in range(trials):
        print("DFS Trial", i + 1, "Runtime:", dfs_times[i], "ms")

    print("DFS Average Runtime:",
          sum(dfs_times) / trials, "ms")

    print()

    print("Number of Trials:", trials)
    print("Runs per Trial:", runs_per_trial)