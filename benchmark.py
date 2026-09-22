import timeit
from bfs_dfs import bfs, dfs

start = 'A'
goal = 'Q'

# Number of repetitions
runs = 100000

# Measure BFS time
bfs_time = timeit.timeit(
    lambda: bfs(start, goal),
    number=runs
)

# Measure DFS time
dfs_time = timeit.timeit(
    lambda: dfs(start, goal),
    number=runs
)

# Calculate average time per search
bfs_average = (bfs_time / runs) * 1_000_000
dfs_average = (dfs_time / runs) * 1_000_000

print("BFS Average Time:", round(bfs_average, 2),
      "microseconds/search")

print("DFS Average Time:", round(dfs_average, 2),
      "microseconds/search")