"""
@brief DFS

思路：
    构建邻接表，初始化父节点数组
    递归遍历，设置该节点的父节点，遍历该节点的邻居节点，邻居节点不是父节点，继续递归，邻居节点作为节点，上一个节点作为父节点
    dfs(1, 0)
    计算 2-n 的 i-partent[i] 和
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n)]
    
    graph = [[] for _ in range(n+1)]
    for u, v in a:
        graph[u].append(v)
        graph[v].append(u)
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