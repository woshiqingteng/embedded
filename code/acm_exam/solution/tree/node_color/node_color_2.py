"""
@brief DFS
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    p = list(map(int, data[0].split()))
    color = list(data[1].strip())
    query = int(data[2].strip())

    n = len(p) + 1
    
    child = [[] for _ in range(n+1)]
    for i, parent in enumerate(p, start=2):
        child[parent].append(i)

    def dfs(node):
        count = 1 if color[node-1] == 'S' else 0
        for c in child[node]:
            count += dfs(c)
        return count
    
    print(dfs(query))

if __name__ == "__main__":
    main()