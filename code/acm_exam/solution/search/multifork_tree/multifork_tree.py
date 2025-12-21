"""
@brief DFS

思路：
    构建树
    DFS，节点和当前权值，当前权值加上该节点权值，最大值初始化为当前权值，遍历该节点所有子节点，更新最大值，返回最大值
    dfs(0, 0)
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    values = list(map(int, data[1].split()))
    a = [tuple(map(int, data[i].split())) for i in range(2, 1+n)]
    
    tree = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = a[i]
        tree[u-1].append(v-1)
    
    def dfs(node, total):
        total += values[node]
        max_sum = total if total < m else 0
        for child in tree[node]:
            current = dfs(child, total)
            max_sum = max(max_sum, current)
        
        return max_sum
    
    result = dfs(0, 0)
    print(result)

if __name__ == "__main__":
    main()