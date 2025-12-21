"""
@brief BFS

思路：
    构建邻接表
    队列遍历节点，初始为根节点，对节点每个邻居遍历
    使用符号位数组（第一个为真），符号位为假（未遍历），将该符号位设为真、该邻居父节点设为该节点、添加邻居节点到队列
    计算 2-n 的 i-partent[i] 和
"""

import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n)]
    
    graph = [[] for _ in range(n+1)]
    for u, v in a:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([1])
    parent = [0] * (n+1)
    visited = [False] * (n+1)
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