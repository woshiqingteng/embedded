""" 
@brief DFS

说明：
    DFS 初始 1 a[0]，分别更新加减并返回最小值，到达数组末尾，返回当前数值和 m 的差的绝对值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    a = list(map(int, data[1].split()))

    def dfs(i, total):
        if i == n:
            return abs(total - m)
        add = dfs(i+1, total + a[i])
        sub = dfs(i+1, total - a[i])

        return min(add, sub)
    
    result = dfs(1, a[0])

    print(result)

if __name__ == "__main__":
    main()