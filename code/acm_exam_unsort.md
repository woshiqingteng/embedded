# ACM exam unsort

**贪吃蛇**

[参考-贪吃蛇](https://blog.csdn.net/satur9/article/details/114419159)

知识点：字典、模拟****1

贪吃蛇只能上下左右移动，如果碰到边界停止不动。当贪吃蛇移动到食物上方则得一分，"A" 代表左移，"W" 代表上移，"S" 代表下移，"D" 代表右移。
第一行输入两个正整数 n 和 m，代表棋盘的行数和列数，接下来输入 n 行长度为 m 的字符串，代表棋盘。字符 "." 代表空地。字符 "*" 代表虫子。字符 "$" 代表食物。再输入只包含 "A"、"W"、"S"、"D" 的字符串代表操作。输出一个整数代表得分。

示例 1：
输入：
3 3 
...
.$.
.*.
WSDSA
输出：
1

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(map(str, data[i].strip())) for i in range(1, n+1)]
    operations = str(data[n+1].strip())

    score = 0
    directions = {
        'W': (-1, 0),  # 上
        'S': (1, 0),   # 下
        'A': (0, -1),  # 左
        'D': (0, 1)    # 右
    }
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                x, y = i, j
                break
        if x != -1:
            break

    for op in operations:
        dx, dy = directions.get(op)
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            if grid[x][y] == '$':
                score += 1
                grid[x][y] = '.'

    print(score)

if __name__ == "__main__":
    main()
```

**字符串表达式**

知识点：字符串、枚举（困难）****2

输入一个包含数字、加号、减号的字符串（可能仅有数字），要求删除一个字符，使得输出的结果最大。

示例 1：
输入：
2021
2021+2022-1
输出：
221
20212021

```python
## eval
def main():
    # input
    s = str(input().strip())
    n = len(s)

    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        try:
            result = eval(string)
            max_result = max(max_result, result)
        except:
            continue

    print(max_result)

if __name__ == "__main__":
    main()

## manual
def calculate(expr):
    result = 0
    current_num = 0
    sign = 1  # 1表示正，-1表示负
    has_digit = False
    
    for ch in expr + '+':  # 加'+'方便处理最后一个数字
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
            has_digit = True
        else:  # 运算符
            if has_digit:
                result += sign * current_num
                current_num = 0
                has_digit = False
                sign = 1 if ch == '+' else -1
    
    return result

def main():
    # input
    s = str(input().strip())
    n = len(s)

    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        result = calculate(string)
        max_result = max(max_result, result)

    print(max_result)

if __name__ == "__main__":
    main()
```

**多叉树**

知识点：DFS****3

[参考-路径总和2](https://leetcode.cn/problems/path-sum-ii/description/)

给你一颗多叉树，但是保证根节点是 1，给定每个节点的权值（一个数组），然后小美可以从根节点出发，在任意位置停下来（可以在叶子节点停，也可以中间停），给一个阈值 m，求所有的路径中，路径和小于 m 的最大值  

示例 1：
输入：
5 10
1 2 3 4 5
1 2
1 3
2 4
2 5
输出：
8

```python
import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    values = list(map(int, data[1].split()))
    u = [int(data[i].split()[0]) for i in range(2, 1+n)]
    v = [int(data[i].split()[1])for i in range(2, 1+n)]
    
    tree = [[] for _ in range(n)]
    for i in range(n-1):
        tree[u[i]-1].append(v[i]-1)
    
    def dfs(node, current):
        current += values[node]
        max_sum = current if current < m else float('-inf')
        for child in tree[node]:
            max_sum = max(max_sum, dfs(child, current))
        
        return max_sum
    
    result = dfs(0, 0)
    print(result if result != float('-inf') else 0)

if __name__ == "__main__":
    main()
```