"""
@brief DFS
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n)]
    
    graph = [[v for u, v in a if i == u] + [u for u, v in a if i == v] for i in range(n+1)]
    parent = [0] * (n+1)
  
    def dfs(node, par):
        parent[node] = par
        for neighbor in graph[node]:
            if neighbor != par:
                dfs(neighbor, node)
    dfs(1, 0)
    
    total = sum(i - parent[i] for i in range(2, n+1))

    print(total)

if __name__ == "__main__":
    main()