from bfs_dfs import bfs, dfs
import sys


def run_bfs():
    for _ in range(500000):
        bfs('A', 'Q')


def run_dfs():
    for _ in range(500000):
        dfs('A', 'Q')


if __name__ == "__main__":
    mode = sys.argv[1].lower()

    if mode == "bfs":
        run_bfs()

    elif mode == "dfs":
        run_dfs()