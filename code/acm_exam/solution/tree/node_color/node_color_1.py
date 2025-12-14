"""
@brief BFS
"""

import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    p = list(map(int, data[0].split()))
    color = list(data[1].strip())
    query = int(data[2].strip())

    n = len(p) + 1
    queue = deque([query])
    count = 0
    
    child = [[] for _ in range(n+1)]
    for i, parent in enumerate(p, start=2):
        child[parent].append(i)

    while queue:
        node = queue.popleft()
        if color[node-1] == 'S':
            count += 1
        for i in child[node]:
            queue.append(i)
        # queue.extend(child[node])
    
    print(count)

if __name__ == "__main__":
    main()