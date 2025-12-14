"""
@brief BFS
"""

import sys
from collections import defaultdict, deque

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n)]
    
    graph = [[] for _ in range(n+1)]
    for u, v in a:
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n+1)
    visited = [False] * (n+1)
    queue = deque([1])
    visited[1] = True
  
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)
    
    total = 0
    for i in range(2, n+1):
        total += (i - parent[i])

    print(total)

if __name__ == "__main__":
    main()