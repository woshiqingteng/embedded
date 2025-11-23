# ACM

## 2 exam

### 2.1 搜索

**图遍历（打僵尸）**

[参考-岛屿数量](https://www.nowcoder.com/practice/0c9664d1554e466aa107d899418e814e)
[参考-岛屿的最大面积](https://www.nowcoder.com/practice/5568943d3a08403f932a5e54ec3ece71)

知识点：BFS（队列）、DFS（递归、栈）

描述：  
2200年就剩下了2个人，这2个人在大的电子显示器上关注僵尸的动态，城市分成了很多方格，如果相邻的2个方格都至少存在一个僵尸，那么就容易形成一大波僵尸潮，一发导弹可以打掉一个僵尸潮。会送入一个n*m的矩阵，里面每个数字代表了方格内的僵尸数量。问需要发射多少导弹，最大的一波僵尸潮是多少个。

示例 1：  
输入：  
3 3  
0 5 3  
1 0 2  
2 0 1  
输出：  
2 11

```python
## bfs (queue)
import sys
from collections import deque

def bfs(grid, visited, i, j, n, m):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    total = grid[i][j]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                total += grid[nx][ny]
    
    return total

def main():
    # read
    data = sys.stdin.read().split()
    if not data: 
        return
    n, m = int(data[0]), int(data[1])
    grid = []
    index = 2

    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    # initial
    visited = [[False] * m for _ in range(n)]
    missile_count = 0
    max_zombies = 0
    
    # traverse
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > 0:
                missile_count += 1
                zombies = bfs(grid, visited, i, j, n, m)
                max_zombies = max(max_zombies, zombies)
    
    # output
    print(f"{missile_count} {max_zombies}")

if __name__ == "__main__":
    main()

## dfs (recursion)
import sys
sys.setrecursionlimit(10000)

def dfs_recursive(grid, visited, i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] == 0:
        return 0
    
    visited[i][j] = True
    total = grid[i][j]

    total += dfs_recursive(grid, visited, i + 1, j, n, m)
    total += dfs_recursive(grid, visited, i - 1, j, n, m)
    total += dfs_recursive(grid, visited, i, j + 1, n, m)
    total += dfs_recursive(grid, visited, i, j - 1, n, m)
    
    return total

def main():
    # read
    data = sys.stdin.read().split()
    if not data: 
        return
    n, m = int(data[0]), int(data[1])
    grid = []
    index = 2

    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    # initial
    visited = [[False] * m for _ in range(n)]
    missile_count = 0
    max_zombies = 0
    
    # traverse
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > 0:
                missile_count += 1
                zombies = dfs_recursive(grid, visited, i, j, n, m)
                max_zombies = max(max_zombies, zombies)
    
    # output
    print(f"{missile_count} {max_zombies}")

if __name__ == "__main__":
    main()

## dfs (stack)
import sys

def dfs_stack(grid, visited, i, j, n, m):
    stack = []
    stack.append((i, j))
    visited[i][j] = True
    total = grid[i][j]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                stack.append((nx, ny))
                visited[nx][ny] = True
                total += grid[nx][ny]
    
    return total

def main():
    # read
    data = sys.stdin.read().split()
    if not data: 
        return
    n, m = int(data[0]), int(data[1])
    grid = []
    index = 2

    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    # initial
    visited = [[False] * m for _ in range(n)]
    missile_count = 0
    max_zombies = 0
    
    # traverse
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > 0:
                missile_count += 1
                zombies = dfs_stack(grid, visited, i, j, n, m)
                max_zombies = max(max_zombies, zombies)
    
    # output
    print(f"{missile_count} {max_zombies}")

if __name__ == "__main__":
    main()
```

**二叉树（树子节点颜色个数、树最近公共祖先）**

[参考-字母树](https://www.nowcoder.com/discuss/395546774016991232)

知识点：树遍历

描述：
给定一棵有n个节点的树，节点用1,2,…n编号。1号节点为树的根节点，每个节点上有一个字符表示的标记，S表示染色，W表示未染色。求给定
节点的子树中出现的染色节点数。  

第一行输入n-1个正整数，第i个整数表示第i+1号节点的父亲节点 
第二行输入一个长度为n字符串，如'SWWWWSWWW'，表示节点1到节点n的染色状态，S表示染色，W表示未染色  
第三行输入一个数表示要查询的节点，求这个节点子节点染色的节点个数  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    parents = list(map(int, data[0].split()))
    colors = data[1].strip()
    query_node = int(data[2])
    
    # build tree
    n = len(parents) + 1
    tree = [[] for _ in range(n+1)]
    
    for i in range(2, n + 1):
        parent = parents[i - 2]
        tree[parent].append(i)
    
    # query
    count = 0
    for child in tree[query_node]:
        if colors[child - 1] == 'S':
            count += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()
```

[参考-树的最近公共祖先1（LCA)](https://blog.csdn.net/born_with_pride/article/details/141069533)

```python
import sys
from collections import deque

def build_tree(n, edges):
    tree = [[] for _ in range(n+1)]
    depth = [0] * (n+1)
    parent = [0] * (n+1)
    
    # adjacent
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)
    
    # BFS
    queue = deque([1])
    depth[1] = 1
    parent[1] = 0
    
    while queue:
        u = queue.popleft()
        for v in tree[u]:
            if depth[v] == 0:
                depth[v] = depth[u] + 1
                parent[v] = u
                queue.append(v)
    
    return depth, parent

def lca(u, v, depth, parent):
    # same depth
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    
    # common ancesotr
    while u != v:
        u = parent[u]
        v = parent[v]
    
    return u

def main():
    # read
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    edges = []
    
    for _ in range(n-1):
        x = int(data[idx]); y = int(data[idx+1])
        idx += 2
        edges.append((x, y))
    
    m = int(data[idx])
    idx += 1
    
    # solve
    depth, parent = build_tree(n, edges)
    
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        result = lca(u, v, depth, parent)
        print(result)

if __name__ == "__main__":
    main()
```

### 2.2 排序

**分数排序**

给定多组输入，每组两个数字，前面的代表分子，后面的代表分母，对形成的分数进行排序

```python
## cross-method

## fractions
import sys
from fractions import Fraction

def main():
    # read
    data = sys.stdin.read().split()
    fractions = []

    for i in range(0, len(data), 2):
        numerator = int(data[i])
        denominator = int(data[i + 1])
        fractions.append((numerator, denominator))
    
    # Fraction
    sorted_fractions = sorted(fractions, key=lambda x: Fraction(x[0], x[1]))
    
    # output
    for frac in sorted_fractions:
        print(f"{frac[0]} {frac[1]}")

if __name__ == "__main__":
    main()
```


**成绩统计**

n 门考试，求成绩的中位数，算数平均值，去极值后的算数平均值，所有结果要求向下取整。

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:1+n]))

    # sort
    sorted_scores = sorted(scores)
    
    # median
    mid = n // 2
    if n % 2 == 1:
        median = sorted_scores[mid]
    else:
        median = (sorted_scores[mid-1] + sorted_scores[mid]) // 2
    
    # mean
    mean = sum(scores) // n
    
    # trimmed
    if n > 2:
        trimmed_scores = sorted_scores[1:-1]
        trimmed_mean = sum(trimmed_scores) // (n - 2)
    else:
        trimmed_mean = 0
    
    # output
    print(f"{median} {mean} {trimmed_mean}")

if __name__ == "__main__":
    main()
```

### 2.3 分治

**池化**

输入n * n的矩阵（n确保为2的次幂且<=1024），矩阵中元素为整数，对矩阵不断做如下操作：  
1. 将矩阵划分成若干个2*2大小的子矩阵，取出每个子矩阵中第二大的数字；  
2. 将上一步取出的数字重新组成新的矩阵，并不断重复该操作直到最后剩余1个数字。  
输出最后剩余的数字  

示例 1：
输入:
4  
-6 -8 7 4  
-5 -5 14 11  
11 11 -1 -1  
4 9  -2 -4  
输出:  
9

```python
import sys

def find_second_largest(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    # matrix size
    new_size = n // 2
    new_matrix = [[0] * new_size for _ in range(new_size)]
    
    # proces 2x2
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            elements = [
                matrix[i][j],
                matrix[i][j+1],
                matrix[i+1][j],
                matrix[i+1][j+1]
            ]

            elements.sort()
            second_largest = elements[2]
            
            new_matrix[i//2][j//2] = second_largest
    
    return find_second_largest(new_matrix)

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matrix = []

    for i in range(1, n + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)
    
    # solve
    result = find_second_largest(matrix)

    # output
    print(result)

if __name__ == "__main__":
    main()
```

### 2.4 回溯

### 2.5 动态规划

**字符串的权值**

[参考-字符串拆分权值和](https://wenku.csdn.net/answer/3b2n0yprg1)

知识点：滑动窗口、ASCII映射

一个字符串的权值定义为a-b,其中a定位为字符串中存在偶数个字符的个数，b定义为字符串中存在奇数个字符的个数。输入一个字符串，可以任何位置分割成两个子串，求所有子串权值和的最大值。

示例 1：  
输入：  
eggff  
输出：  
1  

```python
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    s = data[0].strip()
    n = len(s)
    
    if n < 2:
        print(0)
        return
    
    # initial
    left_freq = [0] * 26
    right_freq = [0] * 26
    
    # calculate right
    for char in s:
        idx = ord(char) - ord('a')
        right_freq[idx] += 1
    
    right_a, right_b = 0, 0
    for count in right_freq:
        if count > 0:
            if count % 2 == 0:
                right_a += 1
            else:
                right_b += 1
    
    left_a, left_b = 0, 0
    max_sum = (left_a - left_b) + (right_a - right_b)
    
    # traverse
    for i in range(n - 1):
        char = s[i]
        idx = ord(char) - ord('a')
        # update left
        left_freq[idx] += 1
        if left_freq[idx] % 2 == 1:
            if left_freq[idx] > 1:
                left_a -= 1
            left_b += 1
        else:
            left_b -= 1
            left_a += 1
        # update right
        right_freq[idx] -= 1
        if right_freq[idx] == 0:
            right_b -= 1
        elif right_freq[idx] % 2 == 1:
            right_a -= 1
            right_b += 1
        else:
            right_b -= 1
            right_a += 1
        
        # sum
        current_sum = (left_a - left_b) + (right_a - right_b)
        if current_sum > max_sum:
            max_sum = current_sum
    
    print(max_sum)

if __name__ == "__main__":
    main()
```

**数组划分（k个子序列极差和最大）**

一个长度为n的数组，可以分为k个不相交的非空子序列，使得子序列的极差之和最大，返回最大的极差值

示例 1：  
输入：  
5 3
1 2 3 4 5  
说明：n=5, k=3  
输出：  
6  
说明：[1,2,3,4,5] 可拆为{1,5}{2,4}{3} 返回6

示例 2：  
输入：  
5 3
2 2 2 2 2  
说明：n=5, k=3  
输出：  
0  
说明：[2,2,2,2,2] 返回 0

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # solve
    arr.sort()
    if 2 * k <= n:
        t = k
    else:
        t = n - k
    
    result = sum(arr[-t:]) - sum(arr[:t])
    
    # output
    print(result)

if __name__ == "__main__":
    main()
```

**切割字符串（质数和）**

知识点：位运算、DFS、回溯

有一个字符串，其中字符均为 '1'-'9' 的数字，现在可以在这个字符串中可以加任意的 '+' 号，使其成为一个公式。如 '123456' 可以变为 '1+23+456'。但是 '+123456'、'1++23456' 这种不可以。求让这个公式的和（1+23+456=480）为质数，没有质数输出 0，有多少种可能,？

示例 1：
输入：  
123  
输出：  
0  
说明：1+23=24；12+3=15；1+2+3=6；没有质数输出0

```python
## bit operation
import sys
import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # check 3 -> sqrt(num) all odd
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    # read
    data = sys.stdin.read().splitlines()
    if not data:
        return
    s = data[0].strip()
    n = len(s)
    
    # initial
    total_ways = 0
    
    # traverse
    for mask in range(1 << (n - 1)):
        current_sum = 0
        current_num = 0
        
        # bitmask
        for i in range(n):
            current_num = current_num * 10 + int(s[i])
            if (mask >> i) & 1 or i == n - 1:
                current_sum += current_num
                current_num = 0
        
        # prime
        if is_prime(current_sum):
            total_ways += 1
    
    # output
    print(total_ways)

if __name__ == "__main__":
    main()

## DFS
import sys
import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # check 3 -> sqrt(num) all odd
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def dfs(s, start, current_sum):
    if start == len(s):
        return 1 if is_prime(current_sum) else 0
    
    count = 0
    for end in range(start + 1, len(s) + 1):
        num = int(s[start:end])
        count += dfs(s, end, current_sum + num)
    
    return count

def main():
    # read
    data = sys.stdin.read().splitlines()
    if not data:
        return
    s = data[0].strip()
    
    # dfs
    result = dfs(s, 0, 0)

    # output
    print(result)

if __name__ == "__main__":
    main()
```

**数字串处理（形成三的最大倍数、）**

知识点：数论（一个数能被3整除，当且仅当它的各位数字之和能被3整除）

[类似-形成三的最大倍数](https://leetcode.cn/problems/largest-multiple-of-three/description/)

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    if not data:
        print("")
        return
    digits = [int(char) for char in data[0].strip()]
    
    # calculate remainder
    total = sum(digits)
    remainder = total % 3
    
    # sort
    digits.sort(reverse=True)
    
    # removed
    if remainder != 0:
        removed = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] % 3 == remainder:
                digits.pop(i)
                removed = True
                break
        if not removed:
            count = 0
            for i in range(len(digits)-1, -1, -1):
                if digits[i] % 3 == 3 - remainder:
                    digits.pop(i)
                    count += 1
                    if count == 2:
                        removed = True
                        break
    
    # check
    if not digits:
        print("")
    elif all(d == 0 for d in digits):
        print("0")
    else:
        result = "".join(map(str, digits)).lstrip('0')
        print(result if result else "0")

if __name__ == "__main__":
    main()
```

知识点：遍历

计算一个数字字符串能被三整除的最大字符串子串（值最大第一，若多个串相等，取长的字符串）

示例 1：  
输入：  
10000666
输出：  
0000666

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    n = len(s)
    best = ""
    
    # traverse
    for i in range(n):
        if s[i] == '0' and not best:
            continue
            
        current_num = 0
        for j in range(i, n):
            current_num = current_num * 10 + int(s[j])
            # /3
            if current_num % 3 == 0:
                candidate = s[i:j+1]
                # comp
                if not best:
                    best = candidate
                else:
                    if int(candidate) > int(best):
                        best = candidate
                    elif int(candidate) == int(best) and len(candidate) > len(best):
                        best = candidate
    
    # check 0
    if not best:
        for char in s:
            if char == '0':
                return "0"
        return "0"
    
    return best

if __name__ == "__main__":
    result = main()
    print(result)
```

**最大连续段（最大合法子数组、游戏嘲笑子数组）**

知识点：贪心

给定一个 N 个元素的数组，输出其中不包含 0 的子数组的最大长度。

示例 1：  
输入：  
6  
1 2 3 0 4 5  
说明：第一行输入一个 N，表示数组长度，第二行输入 N 个数字，表示数组内容  
输出：
3  
说明：不包含 0 的子数组有 [1, 2, 3] 和 [4, 5]，长度分别为 3 和 2，输出 3  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    # initial
    max_len = 0
    current_len = 0
    
    # traverse
    for num in arr:
        if num != 0:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    
    print(max_len)

if __name__ == "__main__":
    main()
```

知识点：贪心

两个人玩游戏，规则如下：  
1. 如果 a 这次的游戏分数大于上次，b 这次的游戏分数小于上次，则 a 嘲笑b。
2. 如果 a 这次的游戏分数大于上次，b 这次的游戏分数也大于上次，若 a 两次游戏的分差 >b 两次游戏的分差，则 a 嘲笑 b
3. 只有 a 两次游戏的分差 =b 两次游戏的分差，a，b 互不嘲笑  
求 a，b 最长互不嘲笑的子数组长度

示例 1：  
输入：  
1 3 4 5 6 0  
-1 1 3 2 5 1  
输出：  
2  
说明：a=[1,3,4,5,6,0]，b=[-1,1,4,2,5,1]，返回2，只有{1，3}，{-1,1}，a 和 b 互不嘲笑

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    a = list(map(int, data[0].split()))
    b = list(map(int, data[1].split()))
    n = len(a)
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return
    
    # initial
    max_len = 1
    current_len = 1
    
    # traverse
    for i in range(1, n):
        if (a[i] <= a[i-1] and b[i] <= b[i-1]) or (a[i] > a[i-1] and b[i] > b[i-1] and (a[i] - a[i-1]) == (b[i] - b[i-1])):
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    max_len = max(max_len, current_len)

    # output
    print(max_len)

if __name__ == "__main__":
    main()
```

**出现子串"AcMer"的最小代价**

- [acmer 子串代价](https://www.codeleading.com/article/37046020529/)

知识点：滑动窗口

输入一个字符串，使字符串中出现子串AcMer的代价最小  
可对字符串进行以下 2 种操作：  
1. 将其中一个字母转换为其对应大写或小写字母，代价为5。（例如 a->A，D->d）
2. 将其中一个字母转换为相同大小写的其他字母，代价为5。（例如 A->D，d->e）

示例 1：
输入  
aaAAcderrrrr  
输出：  
10  
说明：字串 Acder 中的 d 变为 D 得到 AcDer（代价 5），再将 AcDer 中的 D 变为 M 得到 AcMer（代价 5，一共 10）  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    
    # initial
    target = "AcMer"
    n = len(s)
    min_cost = float('inf')
    
    # traverse
    for i in range(n - 4):
        substring = s[i:i+5]
        cost = 0
        # current cost
        for j in range(5):
            current_char = substring[j]
            target_char = target[j]
            # check
            if current_char == target_char:
                continue
            elif current_char.lower() == target_char.lower():
                cost += 5
            else:
                cost += 5
                if current_char.islower() != target_char.islower():
                    cost += 5
        
        min_cost = min(min_cost, cost)
    
    # output
    print(min_cost)

if __name__ == "__main__":
    main()
```

**包含特定字符的子串数量**

知识点：枚举***

一个字符串，求包括 'r'、'e' 同时不包括 'd' 的子串数量。

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    n = len(s)
    
    # initial
    count = 0
    
    # traverse
    for i in range(n):
        has_r = False
        has_e = False
        has_d = False
        for j in range(i, n):
            char = s[j]
            # check str
            if char == 'r':
                has_r = True
            elif char == 'e':
                has_e = True
            elif char == 'd':
                has_d = True
                break
            if has_r and has_e and not has_d:
                count += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()
```

**牛牛吃饭期望**

知识点：数学

牛牛第一天吃了 1 碗，第 2 天吃了 2 碗，第 i 天吃的碗数是前面任意两天的和，j、k 天（j、k 独立且概率相等），求输出每一天吃的碗数

第一行输入总天数 n  
接下来每行输入第 i 天
输出对应输入第 i 天可能吃的碗数

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    
    # solve
    for i in range(1, n + 1):
        day = int(data[i])
        print(day)

if __name__ == "__main__":
    main()
```

**迷宫寻宝**

知识点：动态规划

有一个迷宫，有 n 个站点。每个站点有左右 2 个宝箱，比如站点 i，左宝箱有财宝 ai,右宝箱有财宝 ci。假设在站点 K，如果当前站点选的宝箱和 K-1 站点宝箱一样，就没有惩罚。如果选了左宝箱，而上一站点选了右宝箱的话，要惩罚 dk-1 个财宝（k-1是下标），如果当前选了右宝箱，而上一站点选的左宝箱的话，那么要惩罚 bk-1个 财宝（k-1是下标）。惩罚的财宝有可能是负值，负值的含义就是不但没有惩罚，还相当于变相奖励。站点 1 没有惩罚。请问走完所有迷宫站点后，最多有多少财宝。

第一行输入 n,代表站点个数  
后面 n 行，每行输入 a, b, c, d 四个数。  
输出为走完所有迷宫站点后，最多的财宝数

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    sites = []
    for i in range(1, n + 1):
        a, b, c, d = map(int, data[i].split())
        sites.append((a, b, c, d))
    
    # initial
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = sites[0][0]
    dp[0][1] = sites[0][2]
    
    # traverse
    for i in range(1, n):
        a, b, c, d = sites[i]
        prev_b, prev_d = sites[i-1][1], sites[i-1][3]
        # left
        dp[i][0] = max(
            dp[i-1][0] + a,
            dp[i-1][1] + a + prev_d
        )
        # right
        dp[i][1] = max(
            dp[i-1][0] + c + prev_b,
            dp[i-1][1] + c
        )

    # output
    print(max(dp[n-1][0], dp[n-1][1]))

if __name__ == "__main__":
    main()
```

**打印次数（困难）**

知识点：字符映射、贪心

输入长度为 n 的一个字符串，从 0 开始逐个遍历字符串中的字符，求 [0-j] 范围的字符串中（如str='abc'， j=1时，str[j] = b），能有几个子串包含str[j]（ab，b），要求按以下格式输出

输入：
abc  
输出：  
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
1 2 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
输入：  
xyax  
输出：  
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0  
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 0  
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 0  
3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 2 0  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    n = len(s)
    
    # initial
    last_occurrence = [-1] * 26
    
    # traverse
    for j in range(n):
        # current char
        current_char = s[j]
        char_index = ord(current_char) - ord('a')
        last_occurrence[char_index] = j
        
        # calculate
        result = [0] * 26
        for i in range(26):
            if last_occurrence[i] != -1:
                result[i] = last_occurrence[i] + 1
        
        # output
        print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()
```

**随机加减（困难）**

知识点：枚举、位运算、动态规划

n 个数，n-1 个加减号，与 m 差值最小的结果，输出结果与 m 之间的绝对值。  
n<=20，m 绝对值小于 2000，每个输入数绝对值小于 100  

示例 1：  
输入：  
10  
1 3 5 3 4  
说明：m = 10，输入数组为 [1, 3, 5, 3, 4]，  
输出：  
0  
说明： 1-3+5+3+4=10，abs(m-10)=0  

```python
## bitmask
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    m = int(data[0])
    nums = list(map(int, data[1].split()))
    n = len(nums)
    
    # initial
    min_diff = float('inf')
    
    # traverse
    for mask in range(1 << (n - 1)):
        current = nums[0]
        # bitmask
        for i in range(1, n):
            if mask & (1 << (i - 1)):
                current -= nums[i]  # 减号
            else:
                current += nums[i]  # 加号
        
        # calculate
        diff = abs(current - m)
        if diff < min_diff:
            min_diff = diff
    
    # output
    print(min_diff)

if __name__ == "__main__":
    main()

## dp
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    m = int(data[0])
    nums = list(map(int, data[1].split()))
    n = len(nums)
    
    # initial
    dp = [set() for _ in range(n)]
    dp[0].add(nums[0])
    
    # traverse
    for i in range(1, n):
        for val in dp[i-1]:
            dp[i].add(val + nums[i])
            dp[i].add(val - nums[i])
    
    # calculate
    min_diff = float('inf')
    for result in dp[n-1]:
        diff = abs(result - m)
        if diff < min_diff:
            min_diff = diff
    
    # output
    print(min_diff)

if __name__ == "__main__":
    main()
```

**包粽子**

知识点：动态规划（背包）

[原题-包粽子](https://www.nowcoder.com/discuss/353156615647993856?sourceSSR=search)

包粽子, 四个数 n, m, c0, d0, 一共 n 克面粉, m 种馅料  
然后 m 行, 每行四个数ai, bi, ci, di, ai 表示一共多少克该种馅料  
每个粽子包法, bi克第 i 种馅料 + ci 克面粉, 收益di, 或者 c0 克面粉, 不包馅料, 收益d0
求最大收益

```python
## Bounded Knapsack
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m, c0, d0 = map(int, data[0].split())
    
    # initial
    dp = [0] * (n + 1)
    
    # Unbounded Knapsack
    for j in range(c0, n + 1):
        dp[j] = max(dp[j], dp[j - c0] + d0)
    
    # Bounded Knapsack
    for i in range(1, m + 1):
        a, b, c, d = map(int, data[i].split())
        max_cnt = a // b
        # reverse traverse
        for j in range(n, -1, -1):
            for k in range(1, min(max_cnt, j // c) + 1):
                if j >= k * c:
                    dp[j] = max(dp[j], dp[j - k * c] + k * d)
    
    print(dp[n])

if __name__ == "__main__":
    main()

## Bounded Knapsack (binary)
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m, c0, d0 = map(int, data[0].split())
    
    # initial
    dp = [0] * (n + 1)
    
    # Unbounded Knapsack
    for j in range(c0, n + 1):
        dp[j] = max(dp[j], dp[j - c0] + d0)
    
    # Bounded Knapsack
    for i in range(1, m + 1):
        a, b, c, d = map(int, data[i].split())
        max_cnt = a // b
        # binary
        k = 1
        while max_cnt > 0:
            cnt = min(k, max_cnt)
            weight = cnt * c
            value = cnt * d
            # 0-1 Knapsack
            for j in range(n, weight - 1, -1):
                dp[j] = max(dp[j], dp[j - weight] + value)
            
            max_cnt -= cnt
            k *= 2
    
    # output
    print(dp[n])

if __name__ == "__main__":
    main()
```

**小明打地鼠**

知识点：动态规划

n x m 网格，小明起始位置为(1,1)，有 k 个地鼠，第 i 个地鼠信息(xi, yi, ti, si)，表示 ti 时刻在 (xi, yi) 位置，如果击中获得 si 分。  
规则：  
移动阶段：在 ti-1 结束, ti 之前，小明可以选择在网格向上下左右移动一格，或不移动。
锤击阶段：在 t 时刻，小明在 (i, j) 击中该位置的所有地鼠，获得相应的分数
请规划线路，使小明获得最高分数。  

示例 1：
输入：  
5 3 3  
1 2 1 1  
1 2 3 2  
3 2 2 1  
说明：第一行 n = 5，m = 3，k = 3；后续 3 行，为地鼠信息

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m, k = map(int, data[0].split())
    moles = []
    for i in range(1, k + 1):
        x, y, t, s = map(int, data[i].split())
        moles.append((x, y, t, s))
    
    # initial
    moles.sort(key=lambda x: x[2])
    dp = [0] * k
    
    # traverse
    for i in range(k):
        x1, y1, t1, s1 = moles[i]
        dp[i] = s1 if abs(x1 - 1) + abs(y1 - 1) <= t1 else 0
        # transition
        for j in range(i):
            x2, y2, t2, s2 = moles[j]
            time_diff = t1 - t2
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist <= time_diff and dp[j] > 0:
                dp[i] = max(dp[i], dp[j] + s1)
    
    # max
    result = max(dp) if dp else 0

    # output
    print(result)

if __name__ == "__main__":
    main()
```

**物品价值**

知识点：贪心、位操作

n个元素的值 a1-an，含正整数、负整数，可以操作 k 次，每个值最多操作一次，使 ai 变成 ai*ai，后续 m 次询问，每次询问时（第 i 次询问需要取 i 个物品），总价值和最大是多少？

示例 1：  
输入：  
5 4 5
-3 -2 2 3 4  
说明：第一行 n=5，k=4，m=5；第二行为 n 个元素值 [-3, -2, 2, 3, 4]  
输出：  
16 25 34 38 40  
说明：问询 1, 2, 3, 4, 5 时，对应输出：16, 25, 34, 38, 40

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, k, m = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # initial
    squared = [x * x for x in arr]
    ans = [-10**18] * (n + 1)
    
    # enumerate
    for mask in range(1 << n):
        op_count = bin(mask).count('1')
        if op_count > k:
            continue
            
        # value
        values = []
        for i in range(n):
            if mask & (1 << i):
                values.append(squared[i])
            else:
                values.append(arr[i])
        
        # prefix
        values.sort(reverse=True)
        prefix_sum = 0
        for t in range(1, n + 1):
            prefix_sum += values[t - 1]
            if prefix_sum > ans[t]:
                ans[t] = prefix_sum
    
    # query
    results = []
    for i in range(1, m + 1):
        if i <= n:
            results.append(str(ans[i]))
        else:
            results.append(str(ans[n]))
    
    print(' '.join(results))

if __name__ == "__main__":
    main()
```

### 2.6 贪心

**学生分组**

知识点：贪心、堆

n 名学生参与测试，对所有学生按照如下要求进行重新排序分组：
1. 每组人数不超过三人
2. 三人组要求最高成绩与最低成绩差值小于 10
3. 两人组要求最高成绩与最低成绩差值小于 20
4. 一人组不做要求
输出 n 个学生最少分多少组。

输入：  
第一行 n  
第二行 n 个数代表 n 个学生的成绩  

```python
## 贪心
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    scores = list(map(int, data[1].split()))
    
    # sort
    scores.sort()
    
    count = 0
    i = 0
    while i < n:
        if i + 2 < n and scores[i + 2] - scores[i] <= 9:
            count += 1
            i += 3
        elif i + 1 < n and scores[i + 1] - scores[i] <= 19:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()

## heap
import sys
import heapq

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    scores = list(map(int, data[1].split()))
    
    # heap
    heapq.heapify(scores)
    sorted_scores = []
    while scores:
        sorted_scores.append(heapq.heappop(scores))
    
    count = 0
    i = 0
    while i < n:
        if i + 2 < n and sorted_scores[i + 2] - sorted_scores[i] <= 9:
            count += 1
            i += 3
        elif i + 1 < n and sorted_scores[i + 1] - sorted_scores[i] <= 19:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()
```

**字典序最大序列**

知识点：贪心、堆

已知一个长度为 n 的序列由 1~n 中的数字组成，保证序列中每个元素各不相同，该序列中的数字可以进行如下操作：
与相邻的数字交换位置，自身和相邻数字同时消耗一次交换机会  
已知每个数字最多有两次交换机会，输入最终得到的字典序最大的序列

输入：  
第一行 n  
第二行 n 个数代表初始序列  
输出：  
字典序最大的序列号  

示例 1：  
输入：  
8  
3 7 2 1 5 6 4 8  
输出：  
7 3 5 6 2 1 8 4

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    # initial
    cnt = [2] * (n + 1)
    result = []
    
    # traverse
    for i in range(n):
        best_num = -1
        best_pos = -1
        
        # current position
        for j in range(i, min(n, i + 3)):
            num = arr[j]
            if num <= best_num:
                continue
            # move
            steps = j - i
            if cnt[num] < steps:
                continue
            # count
            valid = True
            for k in range(i, j):
                if cnt[arr[k]] < 1:
                    valid = False
                    break
            if valid:
                best_num = num
                best_pos = j
        
        if best_num != -1:
            # update
            steps = best_pos - i
            cnt[best_num] -= steps
            for k in range(i, best_pos):
                cnt[arr[k]] -= 1
            # move number
            for k in range(best_pos, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = best_num
        
        # output
        result.append(str(arr[i]))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
```

**数组调整（两数组相等、次数最多数字）**

知识点：贪心

有两个数组 a 和 b，其中数组元素个数都为 n，可以按照序列（i，j）对数组 a[i] 和 b[j] 同时加 1，请问至少执行多少次操作，才能使得数组a和b完全相等，如果无法使得两个数组相等，则输出 -1

输入：  
第一行输入数组元素个数 n；  
第二行输入 n 个整数，表示数组 a 中各个元素的具体值；  
第三行输入 n 个整数，表示数组 b 中各个元素的具体值；  

输出：操作次数

示例 1：
输入：  
4  
1 2 3 5  
1 2 4 4  
输出：  
1  
说明：(i=2，j=3)，表示对数组 a[2] 和数组 b[3] 分别加 1，使得数组 a 和 b 完全相等

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    if sum(a) != sum(b):
        print(-1)
        return
    
    # solve
    total_ops = 0
    for i in range(n):
        diff = b[i] - a[i]
        if diff > 0:
            total_ops += diff
    
    # output
    print(total_ops)

if __name__ == "__main__":
    main()
```

知识点：滑动窗口、双指针、哈希统计

给一个由数字组成的数组 a，可以对数组 a 中的每个元素任意进行+1 、-1 或不执行操作，每个元素最多只允许操作一次，求操作后，出现次数最多的数字的出现次数。  

示例 1：  
输入：  
1 2 3  
输出：  
3  
说明：相同整数的最大个数为 3

```python
## sliding window
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    arr = list(map(int, data[0].split()))
    
    # initial
    arr.sort()
    n = len(arr)
    left = 0
    max_count = 0
    
    # traverse
    for right in range(n):
        while arr[right] - arr[left] > 2:
            left += 1
        max_count = max(max_count, right - left + 1)
    
    # output
    print(max_count)

if __name__ == "__main__":
    main()

## hash
import sys
from collections import defaultdict

def main():
    # read
    data = sys.stdin.read().splitlines()
    arr = list(map(int, data[0].split()))
    
    # count
    count = defaultdict(int)
    for num in arr:
        count[num-1] += 1
        count[num] += 1
        count[num+1] += 1
    
    max_count = max(count.values()) if count else 0

    # output
    print(max_count)

if __name__ == "__main__":
    main()
```

**商店购物、商品折扣**

知识点：贪心、堆

有 n 个商店，第 i 个商店的产品数量为 yi，价格为 xi，如果购买给定数量 m 个产品；输出总价最小的数值。

输入：  
第一行为商店个数 n 及购买个数 m  
接下来 n 行输入，每行两个整数 xi, yi  
输出  
购买 m 个商品所需的最小金额

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    stores = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        stores.append((x, y))
    
    # initial
    stores.sort(key=lambda store: store[0])
    total_cost = 0
    remaining = m
    
    # traverse
    for price, quantity in stores:
        if remaining <= 0:
            break
        take = min(quantity, remaining)
        total_cost += take * price
        remaining -= take
    
    # output
    print(total_cost)

if __name__ == "__main__":
    main()
```

知识点：贪心、堆

购买 n 个商品，价格为 xi，商家为促销提供了 n 个折扣 ai，每个折扣只能使用一次，如何使用折扣使花费最少。

输入：  
第一行输入商品和折扣数目 n  
接下来 n 行输入，每行两个整数xi，ai  
输出：  
购买商品的最小金额（保留三位小数）

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    products = []
    for i in range(1, n + 1):
        x, a = map(float, data[i].split())
        products.append((x, a))
    
    # initial
    products.sort(key=lambda p: p[1], reverse=True)
    total_cost = 0.0
    remaining = n
    
    # traverse
    for price, discount in products:
        if remaining > 0:
            discounted_price = max(0.0, price - discount)
            total_cost += discounted_price
            remaining -= 1
    
    # output
    print("{:.3f}".format(total_cost))

if __name__ == "__main__":
    main()
```

**最多不交叉相同子串（困难）**

知识点：贪心、滑动窗口、双指针

- [原题-LYA的字符串收藏](https://www.nowcoder.com/discuss/660859777223819264)

一个字符串 s，截取连续 k 个相同的字母为子串，最多可以截多少个相同的子串？（子串之间不可重叠）

输入：  
第一行为字符串 s  
第二行为子串长度 k  
输出：  
最大个数  

示例 1：
输入  
acccbcccaaabbb  
3  
输出：  
2  
说明：2 个 ccc 子串，一个 aaa 子串，1个 bbb 字串，ccc 的数量最多，所以输出 2

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    k = int(data[1])
    # initial
    char_count = {}
    i = 0
    n = len(s)
    # cycle
    while i < n:
        # same str
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        # length
        length = j - i
        # update count
        count = length // k
        if s[i] in char_count:
            char_count[s[i]] += count
        else:
            char_count[s[i]] = count
        
        i = j
    
    # max
    max_count = 0
    for count in char_count.values():
        if count > max_count:
            max_count = count
    
    # output
    print(max_count)

if __name__ == "__main__":
    main()
```

**取奇数和最大化**

知识点：贪心

一个数组中取数 [1:n]，要求使取到所有数的和为奇数，且取到每个数均为奇数（若ai是偶数那么取ai-1），特别说明，每个元素要么取奇数要么不取，输出取到的总和的最大值

示例 1：
输入：  
1 2 3 4  
输出：  
7  
说明：3+3+1=7

示例 2：
输入：  
1 3 3 4 5  
输出：  
15  
说明：5+3+3+3+1=15

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    # initial
    total = 0
    min_odd = float('inf')
    for num in arr:
        if num % 2 == 0:
            odd_val = num - 1
        else:
            odd_val = num
        total += odd_val
        if odd_val < min_odd:
            min_odd = odd_val

    # output
    if total % 2 == 1:
        print(total)
    else:
        print(total - min_odd)

if __name__ == "__main__":
    main()
```

**大小写翻转**

知识点：贪心

一个由有 n 个大小写字母组成的字符串，每操作一次可使大小写字母翻转，如，A->a 或 a->A。要求，经过 k 次操作，使得字符串中的大写字母最多，并返回大写字母的个数。

示例 1：  
输入：  
1 3  
A
输出：  
0

示例 2：  
输入：  
5 3  
arBrg
输出：  
4

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    # solve
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = n - upper_count
    
    if k <= lower_count:
        result = upper_count + k
    else:
        result = n - ((k - lower_count) % 2)
    
    # output
    print(result)

if __name__ == "__main__":
    main()
```

**三角形判断**

知识点：数学***

[类似-不可能三角](https://www.nowcoder.com/discuss/750016145939247104?sourceSSR=post)

给定 a, b, c 分别代表三角形的三条边，输入 x, y, z 三个数作为三角形边长，判断能否组成三角形，不能则输出 "can not"；如果能，组成的三角形与a, b, c 组成的三角形相似，则输出 "similar",否则，输出 "can,but not similar"。

判断输入的多个正整数数组能否构成三角形，以及与给定三角形是否相似。  
输入：  
第一行输入一个数组，代表基底三角形，输入保证是合法三角形  
第二行输入一个数字，代表即将要输入n行数组，每个数组长度为 3  
接下来输入n个数组...  
输出：  
对每组输入数组，首先判断数组能否构成三角形，如果能，接着判断是否与基底三角形相似，然后根据情况，每组判断后分别输出：("Similar"、"Can form a triangle but not similar"、"Can not form a triangle")

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    base = sorted(map(int, data[0].split()))
    n = int(data[1])
    
    # traverse
    for i in range(2, 2 + n):
        test = list(map(int, data[i].split()))
        test_sorted = sorted(test)
        
        # triangle
        if test_sorted[0] + test_sorted[1] <= test_sorted[2]:
            print("Can not form a triangle")
            continue
        
        # similar (cross-multi)
        if (test_sorted[0] * base[1] == test_sorted[1] * base[0] and
            test_sorted[1] * base[2] == test_sorted[2] * base[1] and
            test_sorted[0] * base[2] == test_sorted[2] * base[0]):
            print("Similar")
        else:
            print("Can form a triangle but not similar")

if __name__ == "__main__":
    main()
```

**木板排列**

知识点：贪心、二分查找

有 n 个木板，每个木板宽度是 1，第 i 个木板的高度是 ai，输入一行数，分别代表 n 个木板的高度，将这些木板任意顺序竖起来排列，请问可以截取的正方形边长最大是多少。

示例 1：  
输入：  
5 1 2 3 4  
输出：  
3

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    arr = list(map(int, data[0].split()))
    
    # initial
    arr.sort(reverse=True)
    max_side = 0

    # traverse
    for i in range(len(arr)):
        if arr[i] >= i + 1:
            max_side = i + 1
        else:
            break
    
    # output
    print(max_side)

if __name__ == "__main__":
    main()
```

**打枪**

知识点：枚举

假设子弹数量不限。刚开始枪没有安装子弹，一个弹夹有 m 个子弹，安装弹夹需要 a 分钟，安装 1 个子弹 b 分钟，开一枪需要 1 分钟，求牛牛开 n 枪，最小多少分钟。

1 < n, m, a, b < 100000

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m, a, b = map(int, data[0].split())
    
    # initial
    max_clips = (n + m - 1) // m
    min_time = float('inf')
    
    # traverse
    for t in range(max_clips + 1):
        single_bullets = max(0, n - t * m)
        total_time = t * a + single_bullets * b + n
        min_time = min(min_time, total_time)
    
    # output
    print(min_time)

if __name__ == "__main__":
    main()
```

**炸弹（困难）**

知识点：贪心、哈希

有 n 个炸弹，每个炸弹上有一个数字，初始状态下所有的炸弹都是触发状态，按下会变成非触发状态，只有当两个炸弹处于触发状态时且两个炸弹的数字和为 k 时，会爆炸，牛牛需要以最少的按动次数，保证炸弹不会爆炸。

示例 1：  
输入：  
8 8  
5 3 5 7 1 6 8 9  
说明：第一行输入 n=8，k=8；第二行输入炸弹上数字 5 3 5 7 1 6 8 9
输出：  
2  
说明：[5 3] 和 [7 1] 会爆炸，将炸弹 3 或 5，炸弹 7 或 1，按成非触发状态，输出 2 次

```python
import sys
from collections import Counter

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # initial
    freq = Counter(arr)
    visited = set()
    ans = 0
    
    # traverse
    for num in list(freq.keys()):
        if num in visited:
            continue
        if num > k // 2:
            continue
            
        complement = k - num
        if num == complement:
            ans += freq[num] - 1
        elif complement in freq:
            ans += min(freq[num], freq[complement])
            visited.add(complement)
        visited.add(num)
    
    # output
    print(ans)

if __name__ == "__main__":
    main()
```

**蛇吃水果**

知识点：贪心

蛇的初始长度为 L，每吃一颗水果长度 +1，有 n 颗水果，每颗高度为 h，蛇可以吃到不高于自己长度的水果，问蛇最长多少。

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, L = map(int, data[0].split())
    fruits = sorted(map(int, data[1].split()))
    
    # sum
    for h in fruits:
        if L < h:
            break
        L += 1
    
    # output
    print(L)

if __name__ == "__main__":
    main()
```

**格子**

知识点：贪心、堆

第一行输入 N，M，其中 N 代表每个卡片有 2*N 的格数，M 代表有 M 行输入，即 M 个卡片，每行输入有两个数 a 和 b，分别代表卡片的红色格数和绿色格数，红色格数大于绿色格数的就是有效卡片，现知道有个操作可以将绿色格子变成红色，每操作一次即为操作数 1，请问如果 M 个卡片中，最少能变成 M-1 个有效卡片的话，操作的最少数是多少。

示例 1：
输入：  
5 4  
3 7  
5 5  
0 10  
7 3  
说明：  
第一行 N=5，M=4，一共 2*5=10 格，4 张卡片  
后面 4 行，每行分别表示红格和绿格数量，且 a+b = 2*N  
输出：  
4  
说明：M-1=3 张卡片有效，至少需要调整 4 次（调整第1、2、4张）

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    N, M = map(int, data[0].split())
    
    # initial
    total_ops = 0
    cards = []
    
    # traverse
    for i in range(1, M + 1):
        a, b = map(int, data[i].split())
        if a <= b:
            ops_needed = (b - a) // 2 + 1
            cards.append(ops_needed)
        else:
            cards.append(0)
    
    # calculate
    cards.sort()
    total_ops = sum(cards[:M-1])
    
    # output
    print(total_ops)

if __name__ == "__main__":
    main()
```

**大胃王比赛**

知识点：贪心

有三个输入，N 为餐品数量，M 为选手最大饭量，数组为 N 份餐对应的饱腹值，输出选手是否可以吃饱。

示例 1：
输入：  
4 3  
1 2 1 5  
说明：N=4，M=3，数组饱腹值 [1, 2, 1, 5]  
输出：  
Yes

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    N, M = int(data[0]), int(data[1])
    values = list(map(int, data[2:2+N]))
    
    # solve
    total = sum(values)
    if total >= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
```

**买花**

知识点：贪心、堆

[原题-买花](https://wenku.csdn.net/answer/70mdz0b5h2)

一个数组 n 个元素，数组内元素表示花店第 i 种花的总数量，要求每种花只能买奇数支，并且要求买花的总数量也为奇数，问最多能买多少支花。

示例 1：
输入：  
1 10 8 3  
输出：
19  
说明：最多购买 (10-1) + (8-1) + 3 = 19

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    arr = list(map(int, data))
    base_list = []
    for x in arr:
        if x % 2 == 1:
            base_list.append(x)
        else:
            base_list.append(x - 1)
    
    total = sum(base_list)
    if total % 2 == 1:
        print(total)
    else:
        min_val = min(base_list)
        result = total - min_val
        print(result)

if __name__ == "__main__":
    main()
```

**买文具**

给出 n 个店铺，每个店铺卖的文具个数、每个文具的单价，求 k 元最多可以买多少文具？

第一行给 n, k 两个数，分别代表店铺数量和 k 元  
接下来 n 行分别给出两个数，分别代表该店铺的文具总量和文具单价，如
1, 2  
2, 3  
1, 1  
要你输出一个整数，表示能买到的最多的玩具。

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    stationeries = []
    idx = 2
    for _ in range(n):
        count, price = int(data[idx]), int(data[idx+1])
        stationeries.append((price, count))
        idx += 2
    
    # initial
    stationeries.sort()
    total_count = 0
    remaining_money = k
    
    for price, count in stationeries:
        max_buy = min(count, remaining_money // price)
        total_count += max_buy
        remaining_money -= max_buy * price

        if remaining_money <= 0:
            break
    
    print(total_count)

if __name__ == "__main__":
    main()
```

**最大异或数**

知识点：贪心、位运算、动态规划

给定两个正整数 x, k，找到一个不大于 k 的正整数 y，使得 x ors y 最大。  
ors 定义： x 按位异或 y。

示例 1：  
输入  
3  
3 2  
5 4  
10 18  
说明：第一行输入组数；后面每行为对应的 x 和 k
输出：  
1  
2  
17  

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    
    # solve
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        y = 0
        for i in range(31, -1, -1):
            bit = 1 << i
            x_bit = (x >> i) & 1
            # x_bit ^ desired = 1
            desired = 1 - x_bit
            if (y | (desired << i)) <= k:
                y |= desired << i
            elif (y | (x_bit << i)) <= k:
                y |= x_bit << i
        
        results.append(str(y))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

**对称数组**

知识点：贪心、双指针、队列

一个数组，一次可以对相邻 2 个数都加 1，求将数组调整为对称数组的最小次数，如果无法调整为对称数组，返回 -1。

示例 1：  
输入：  
5  
1 1 2 2 1  
说明：第一行为数组长度 5；第二行为输入数组
输出：  
1  

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    # check symmetric
    for i in range(n // 2):
        if arr[i] > arr[n - 1 - i]:
            print(-1)
            return
    
    # traverse
    operations = 0
    for i in range(n // 2):
        j = n - 1 - i
        diff = arr[j] - arr[i]
        
        if diff > 0:
            operations += diff
            if i + 1 < n:
                arr[i + 1] += diff
    
    print(operations)

if __name__ == "__main__":
    main()
```

**字符串加减**

知识点：队列、滑动窗口***

[原题-字符串加减](https://ac.nowcoder.com/acm/contest/11214/I)

给定一个数字字符串 s，可以对每个数字做加 1 或减 1 的操作，现在给定整数 k，希望操作的次数尽可能少，使得操作之后，s 有一个长度为 k 的子串，子串里的所有数字相等，求最小操作次数。

示例 1：  
输入：  
5 3  
59283  
说明：第一行字符串长度 5，k=3；第二行字符串
输出：  
6  
说明：2->3 操作一次 +1，8->3 操作 5 次 -1，59333

```python
import sys
from collections import deque

def main():
    # read
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    s = data[2]
    
    min_operations = float('inf')
    
    # traverse
    for target in range(10):
        costs = [abs(int(ch) - target) for ch in s]

        window = deque()
        current_sum = 0
        
        for i in range(n):
            window.append(costs[i])
            current_sum += costs[i]
            if len(window) > k:
                current_sum -= window.popleft()
            if len(window) == k:
                min_operations = min(min_operations, current_sum)
    
    print(min_operations)

if __name__ == "__main__":
    main()
```

**最少交换次数**

知识点：图论（环分解）、贪心、逆序对

给定数组, 如果当前的 idx+1 != nums[idx]，则需要交换（只能相邻进行交换）, 求最少的交换次数。

示例 1：
输入：  
2 1 3 5 4  
输出：  
2

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data))
    n = len(arr)
    
    # reverse
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    
    print(inversions)

if __name__ == "__main__":
    main()
```

### 2.7 模拟

**对答案**

知识点：计数

牛牛期末考试全部为选择题，且只有 A、B 两个选项，牛牛做题时直接蒙的答案，现在考试结束，牛牛拿到答案后，想知道如果之前蒙的答案全部相反，能不能获得更高的分数，不能获得更高分输出 "Oh Yes",可以则输出 "Oh No",一样则输出 "(O.O)"。
输入第一行为牛牛蒙的答案，第二行为正确答案。

示例 1：  
输入：  
AA  
AB  
输出：  
(O.O) 

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    niuniu_answer = data[0].strip()
    correct_answer = data[1].strip()
    
    # initial
    n = len(niuniu_answer)
    original_correct = 0
    for i in range(n):
        if niuniu_answer[i] == correct_answer[i]:
            original_correct += 1
    
    # reverse
    reversed_correct = n - original_correct
    if original_correct > reversed_correct:
        print("Oh Yes")
    elif original_correct < reversed_correct:
        print("Oh No")
    else:
        print("(O.O)")

if __name__ == "__main__":
    main()
```

**数组模排序**

知识点：排序（冒泡）***

输入一个数组和一个连续区间，顺序遍历区间内每个数 k，然后顺序遍历数组，若 a[i] mod k > a[i+1] mod k，就交换 a[i] 和 a[i+1] 的数值。求遍历完区间，数组的最终序列。

输入：  
第一行输入 2 个数字m n，m 代表数组长度，n代表区间 [1, n]  
第二行代表数组元素  
输出：  
数组，空格连接

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2+m]))
    
    # traverse
    for k in range(1, n + 1):
        for i in range(m - 1):
            mod_i = arr[i] % k
            mod_next = arr[i + 1] % k
            if mod_i > mod_next:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # output
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
```

**字符串嫁接操作**

输入两个字符串 s 和 t，包含可见字符与空格，t 字符串数组长度是偶数，将 t 的后半段嫁接到 s 后面，输出嫁接后的 s 和剩余前半段的 t，需要保留所有字符。

示例 1：  
输入：  
abd  
asdfgg  
说明：第一行字符串 s，第二行字符串 t  
输出：  
abdfgg  
asd  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].rstrip('\n')
    t = data[1].rstrip('\n')
    
    # solve
    half_len = len(t) // 2
    t_first_half = t[:half_len]
    t_second_half = t[half_len:]
    s_grafted = s + t_second_half
    
    # output
    print(s_grafted)
    print(t_first_half)

if __name__ == "__main__":
    main()
```

**密码锁拨动次数**

- [原题-小红的密码锁](https://blog.csdn.net/weixin_49496731/article/details/127215276)

输入两个四位数的整数，表示密码锁的状态，只能逆时针拨动（9->8->...->0->9）密码锁的每一位数字，要求至少拨动多少次，能够使状态 1 变成状态 2

示例 1：  
输入：  
9999  
8888  
输出：  
4  
说明：每一位波动一次，总共 4 次可由状态 1 变为状态 2

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    current = data[0].strip()
    target = data[1].strip()
    
    # traverse
    total_moves = 0
    for i in range(4):
        a = int(current[i])
        b = int(target[i])
        moves = (a - b) % 10
        total_moves += moves
    
    print(total_moves)

if __name__ == "__main__":
    main()
```

**人名游戏记录**

输入一个数 n，其后跟 n 行人名和游戏，表示这个人玩了哪些游戏，要求按人名和游戏名出现的先后顺序输出每个人玩的游戏

示例 1：
输入：
3  
name1:game2  
name2:game3  
name1:game1  
输出：
name1:game2 game1  
name2:game3  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    
    # initial
    person_games = {}
    
    # solve
    for i in range(1, n + 1):
        line = data[i].strip()
        if ':' in line:
            person, game = line.split(':', 1)
            person = person.strip()
            game = game.strip()
            if person in person_games:
                person_games[person].append(game)
            else:
                person_games[person] = [game]
    
    # output
    for person, games in person_games.items():
        print(f"{person}:{' '.join(games)}")

if __name__ == "__main__":
    main()
```

**字符串截取**

知识点：进制转换

[原题-01串切割](https://blog.csdn.net/ouyang_peng/article/details/150503091)

一个字符串，只包含0，1，第 1 次截取开始 1 个，字符串去除截取的子串，第 2 次截取 2 个，以此类推，但长度达到 9 后，重新从 1 开始，当剩余字符不足当前截取长度时停止，输出每次截取子串的十进制数。

示例 1：  
输入：  
01001100  
输出：  
0 2 3

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    
    # initial
    result = []
    current_length = 1
    index = 0
    n = len(s)
    
    # 
    while index + current_length <= n:
        substring = s[index:index + current_length]
        # binary -> demical
        decimal_value = int(substring, 2)
        result.append(str(decimal_value))
        # update
        index += current_length
        current_length += 1
        if current_length > 9:
            current_length = 1
    
    # output
    print(" ".join(result))

if __name__ == "__main__":
    main()
```

**学生成绩统计（祝贺短信）**

知识点：数学

n 个学生考试 m 门课，这些学生中，只要有一门课高于本门课的平均成绩，老师就要给这位学生发祝贺短信，求老师要给多少名学生发祝贺短信。

示例 1：  
输入：  
3 3  
1 2 3  
2 3 2  
2 2 2  
输出：  
3  

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    grades = []
    idx = 2
    for _ in range(n):
        row = list(map(int, data[idx:idx+m]))
        grades.append(row)
        idx += m
    
    # calculate
    avg_grades = []
    for j in range(m):
        total = 0
        for i in range(n):
            total += grades[i][j]
        avg_grades.append(total / n)

    count = 0
    for i in range(n):
        for j in range(m):
            if grades[i][j] > avg_grades[j]:
                count += 1
                break

    print(count)

if __name__ == "__main__":
    main()
```

**数字整除特性**

知识点：遍历

一个正整数 n，判断 n 是否可以被 n 中的每个数整除，求可被整除的个数；

示例 1：  
输入：  
7300  
输出：  
0  

示例 2：  
输入：  
125  
输出：  
2  

```python
n = int(input().strip())
s = str(n)
count = 0
for char in s:
    d = int(char)
    if d != 0 and n % d == 0:
        count += 1
print(count)
```

**01字符串计数**

知识点：计数

输入一个长度为 n 的 01 字符串，要求输出一个长度为 n 的数组，要求数组的每一个元素等于字符串从第 1 个元素开始到当前位置上不等于当前位置字符的累计计数。

示例 1：  
输入：  
010101  
输出：  
0 1 1 2 2 3  

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    
    result = []
    count_0 = 0 
    count_1 = 0
    
    # traverse
    for i, char in enumerate(s):
        if char == '0':
            result.append(str(count_1))
            count_0 += 1
        else:
            result.append(str(count_0))
            count_1 += 1
    
    print(" ".join(result))

if __name__ == "__main__":
    main()
```

**未出现字母的ASCII和**

已知大写字母ASCII值'A'=65，给出一个字符串，求字符串中没有出现的字母ASCII

**质数和**

- [质数和相加/拆解](https://www.nowcoder.com/practice/c96d6acc025541ffb79c579688f8d003?tpId=167&tqId=34053&ru=/exam/oj)

给定一个大于等于2的整数，求最多能有多少个质数求和得到该数。（质数可以重复）

偶数全部2相加，奇数-1先变成偶数，最有一个2编程3

**好格子**

有红、蓝、空的格子（矩阵），红格子上下左右如果有蓝格子，则这个格子定义为好格子，求好格子数量

格子为“R”，邻接格子任意一个为“B”即为好格子，算给出的矩阵中好格子的总数。

**密文解密**

小明收到一串只包含小写字母的密文，解密的规则如下：
（1）如果字符是元音字母，则不作任何改变；
（2）如果字符是辅音字母，则将其替换为以下连续的三个字母：
① 第一位为原字母的本身
② 第二位为离其最近的元音字母，如果与两个元音字母的距离相等，则选择离a这边最近的，不选离z这边近的。
③ 第三位切换原字母的大小写
    请输出解密后的明文。
    例如，元音字母为a、e、i、o、u。输入"ac",输出"acaC"

**贪吃蛇**
贪吃蛇只能上下左右移动，如果碰到边界停止不动。当贪吃蛇移动到食物上方则得一分，“A”代表左移，“W”代表上移，“S”代表下移，“D”代表右移。
第一行输入两个正整数m和n，代表棋盘的行数和列数，接下来输入n行长度为m的字符串，代表棋盘。字符‘.’代表空地。字符‘*’代表虫子。字符‘$’代表食物。再输入只包含“A”"W""S""D"代表操作。输出一个整数代表得分
例：
输入 3 3 
. . .
.$ .
.* .
给出一串操作指令 WSDSA
输出得分：1

输入一个n * m的矩阵，分别用'.'表示空地、'*'表示虫子、'$'表示食物。虫子每吃到一个食物加一分，输入确保有且只有一只虫子。
另外输入一行包含"WSAD"的操作，W表示虫子向上走一格，S表示虫子向下走一格，A表示向左走一格，D表示向右走一格。
要求，输出虫子执行完"WSAD"操作后，得到的分数。

**打印"里”字**

输入描述
一个正整数 n，代表"里”字的大小。1 <= n <= 30
输出描述
输出 11*n 行，每行输出一个长度为 11*n 的，仅包含'.'和'*'的字符串，这些'*'从视觉上组成了'里'字的形状

**棋子移动**

双陆棋：棋子可以在线性棋盘(1-2019)位置移动，如果目标位置已有棋子则不可以移动。每次操作将棋子向前移动一格。给定2个数组，一个表示初始棋子的位置，一个表示每次操作的棋子序号。问操作完之后各棋子的位置。

有2019个方块，每个方块操作一次代表向右移动一次，每个棋子可以在一个位置停留
第一行输入n，代表棋子个数
第二行输入n个数，代表从1-n号棋子每个棋子的初始位置
第三行输入m，代表操作次数
接下来m行，每行一个数字，代表操作的棋子编号
求最终n个棋子的位置
注意：棋子和棋盘的方格占用需要单独考虑。移动时需要注意棋盘的位置

**固定形状隔离覆盖（格子染色、印章规范）**

知识点：遍历、切比雪夫距离、贪心***

描述：  
小红有一个 2x2 的印章，要求不能相邻盖章（公共边或公共角均不可）以及重复盖章。现在小红忘记了自己的盖章顺序，给定一张盖完后的表格，帮助小红确认盖章是否规范。0 代表未盖章的格子，1 代表盖章后的格子

输入：  
第一行输入两个整数 x, y，代表表格的行与列  
接下来给出一张 x 行 y 列的表  

输出：  
表格规范输出 Yes，否则输出 No  

示例 1：  
输入：  
4 4  
1 1 0 0  
1 1 0 0  
0 0 1 1  
0 0 1 1  
输出：  
No  
解释：两个章存在相邻角

示例 2:  
输入：  
5 6  
1 1 0 0 0 0  
1 1 0 0 0 0  
0 0 0 1 1 0  
0 0 0 1 1 0  
0 0 0 0 0 0  
输出：  
Yes

```python
import sys

def main():
    # read data
    data = sys.stdin.read().split()
    if not data:
        print("No")
        return
    
    x = int(data[0])
    y = int(data[1])
    index = 2
    grid = []
    for i in range(x):
        row = list(map(int, data[index:index+y]))
        index += y
        grid.append(row)
    
    # check range
    if x < 2 or y < 2:
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    print("No")
                    return
        print("Yes")
        return
    
    stamps = []
    # find 2x2 lattice
    for i in range(x - 1):
        for j in range(y - 1):
            if (grid[i][j] == 1 and rid[i][j+1] == 1 and grid[i+1][j] == 1 and grid[i+1][j+1] == 1):
                stamps.append((i, j))
    
    # check adjacent(Chebyshev distance)
    n = len(stamps)
    for i in range(n):
        for j in range(i + 1, n):
            i1, j1 = stamps[i]
            i2, j2 = stamps[j]
            if max(abs(i1 - i2), abs(j1 - j2)) < 2:
                print("No")
                return
    
    # check covered
    covered = [[False] * y for _ in range(x)]
    for (i, j) in stamps:
        covered[i][j] = True
        covered[i][j+1] = True
        covered[i+1][j] = True
        covered[i+1][j+1] = True
    
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1 and not covered[i][j]:
                print("No")
                return

    # pass
    print("Yes")

if __name__ == "__main__":
    main()
```


**去掉一个字符使得计算表达式结果最大（困难）**

输入一个包含数字、加号、减号的字符串（可能仅有数字），要求删除一个字符，使得输出的结果最大。
例如：
输入2021，输出221。思路：删除字符'0'，若删除其他字符则结果均小于221
输入2021+2022-1，输出20212021。思路：删除'+'，则计算表达式变为：
20212022-1，结果为20212021。可以验证，若删除其他字符则结果均小于此。

给定一个字符串，字符串由数字和加减号组成，删除任意一个字符，求出这串字符串结果的最大值
str = "1103+123+44-132"

**包车**

包车，[l,r]区间如果没有人定，则包车成功。输入T组区间，按顺序判断是否可以包车，统计可以包车的区间数量。

**字符串插入**

一个有字符串str是否能够由ab通过任意位置插入构成，若能构成输出YES，否则NO。
比如：abab、aabb YES； aaab NO；

**数组删除**

数组n，随机取i，j，如果|n[i]-n[j]|<=1，删除大的那个值，  
求数组最终能否只剩一个值

**删除公共字符**

[原题](https://www.nowcoder.com/practice/f0db4c36573d459cae44ac90b90c6212)


### 2.8 数学

**骰子期望次数**

知识点：数学

有一个 N 面的骰子，小红希望掷出 X,Y(X 不等于 Y)，第二行输入骰子每面的数字，求理论掷出 X 和 Y 需要的总次数，保留小数点后一位。

示例 1：  
输入：  
2 1 2  
1 2  
说明：第一行 N=2，X=1，Y=2；第二行输入骰子每面的数字
输出：  
4.0  

示例 2：  
输入：  
5 1 2  
1 2 2 2 3  
输出：  
8.3   

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    X = int(data[1])
    Y = int(data[2])
    faces = list(map(int, data[3:3+n]))
    
    # initial
    count_X = faces.count(X)
    count_Y = faces.count(Y)
    p_X = count_X / n
    p_Y = count_Y / n
    
    # calculate
    if p_X == 0 or p_Y == 0:
        result = 0.0
    else:
        result = 1.0 / (p_X * p_Y)
    
    # output
    print("{:.1f}".format(result))

if __name__ == "__main__":
    main()
```

**位运算（X与Y的对数）**

知识点：位运算

有整数 X、Y、A、B，其中 X<=Y，X、Y位取与得到A，X、Y位取或得到B。

示例 1：  
输入：  
4 7  
说明：输入 A=4, B=7  
输出：  
2  
说明：（4,7）（5,6），输出 2

```python
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        A = int(data[index])
        B = int(data[index + 1])
        index += 2
        bits = max(A.bit_length(), B.bit_length(), 1)
        mask = (1 << bits) - 1
        if A & (~B) & mask != 0:
            results.append("0")
        else:
            D = B & (~A) & mask
            k = bin(D).count('1')
            if k == 0:
                results.append("1")
            else:
                results.append(str(2 ** (k - 1)))
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
```

**异或找缺失数**

知识点：数学（异或）

存在一个数组，该数组中元素为从 1 到 n 的整数，互不重复，已知该数据的长度 n 和在缺少某个元素时的数组剩余元素的异或和，希望得到该数组缺失的元素。

输入：第一行为用例个数，之后第一行为第一个用例，包含两个数n,k，n表示整数，k表示为当前异或和  
输出：缺失的整数  

示例 1：  
输入：  
2  
5 2  
10 14  
输出：  
3  
5  

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        # xor
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        
        missing = total_xor ^ k
        results.append(str(missing))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

**好数的异或和**

知识点：位运算***

小红定义了好数：某一数值的二进制中的 "1" 的个数为偶数，则为好数，小红拿到了 n 个元素的数组，输出其中好数的异或和。

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    xor_result = 0
    for num in arr:
        count_ones = bin(num).count('1')
        if count_ones % 2 == 0: 
            xor_result ^= num 
            
    print(xor_result)

if __name__ == "__main__":
    main()
```

**减2^k操作次数**

给定一个数组，每次操作可以从数组中取任意个元素，对其同时减少2^k（k任选），最少进行多少次操作，可以将整个数组所有元素变为0

给你一个数组，你可以选择2的k次方的数，来对这个数组中的数字进行相减，问当数组中的数字全都变成0的时候，最小的操作次数。（15分）
1 2 3
第一次使用2来对2和3进行操作，变成 1 0 1  
第二次使用1对剩余进行操作，变成 0 0 0  
一共两次操作次数

**函数f(x)=lowbit(x)的求和**

知识点：位运算

小红定义函数f(x)为x二进制数的最低位1对应的数，比如10(1010)对应的数为2,12(1100)对应的数为4。输入整数n，输出i/f(i)【1<=i<=n】的加和
输入：正整数n
输出：i/f(i)【1<=i<=n】的加和

```python
import sys

def main():
    # read
    n = int(sys.stdin.readline().strip())
    
    # solve
    total_sum = 0
    for i in range(1, n + 1):
        # min bit 1
        f_i = i & -i
        total_sum += i // f_i
    
    print(total_sum)

if __name__ == "__main__":
    main()
```

**四个数的最小公约数**

知识点：数学

输入四个正整数，求他们的最小公约数（要求输出值大于1），如果没有则返回 -1

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    a, b, c, d = map(int, data)
    
    # solve
    min_val = min(a, b, c, d)
    for i in range(2, min_val + 1):
        if a % i == 0 and b % i == 0 and c % i == 0 and d % i == 0:
            print(i)
            return

    print(-1)

if __name__ == "__main__":
    main()
```

**墙壁划线**

[原题](https://www.nowcoder.com/practice/fbae28533ca04bd0ba088329cb46210d)

计算a*b大小的砖砌成的横X块,竖Y块构成的墙面，从左上角到右下角的对角线以及右上角到左下角的对角线一共穿越了多少次砖的边界
输入：a,b,x,y
输出：sum(左对角线经过每条砖缝与+右对角线经过每条砖缝)

**火箭飞出大气层**

发射火箭，地球半径为R，球心坐标为（0，0，0），发射点坐标为x,y,z，火箭三个坐标向的速度为vx，vy，vz，请问火箭飞出大气层的时刻，输入t组，每组一行，每行行输入分别为，y，z，vx，vy，vz，R，每行输出一个时刻

**按二进制1的奇偶性转换大小写**

将字符串转换为大写
输入一个全是小写的字符串，它的下标p从1开始，直到n，如果下标的二进制表示中1的数量为奇数，则把对应的字母转换为大写，否则不变
例：
输入：abcdefg
输出：ABcDefG
// 1 2 3 4 5 6 7
0000 0001 % 2=1
0000 0010 % 2 =0
0000 0011%2 = 1
000 0001 % 2 =1

**红黑数相乘之和**

输入n个整数的数组ai，再输入n个字母的字符串si，si只包含‘R’或'B'，si为'R'代表ai为红数，si为'B'代表ai为黑数，取一个红数与一个黑数相乘得到红黑数，问所有红黑数的和为多少？
输入：第一行输入整数n
第二行输入n个整数数组ai
第三行输入长度为n的字符串si
输出：所有红黑数之和
例1：
输入：3
1 2 3
RBR
输出：8
说明：2*1+2*3=8
例2：
输入：6
1 2 3 4 5 6
BBBBBB
输出：0
说明：只有黑数

输入一个整数数组a，长度为n
输入字符串：RRBRBB，长度为n，代表数组中对应数字是红还是黑
R代表红，B代表黑，R和B是一对红黑数，红黑数的值为数组对应的数字相乘
求所有红黑数的和

**区间操作（倍数下标加1）**

一个长度为n，值为0的数组，每次输入三个数l,r,v，对序列[l~r]，如果下标是v的倍数，则该下标对应的值＋1，操作次数为q次,输出操作完的数组
例
5 2
1 4 1
1 5 2
第一次操作[1 1 1 1 0]（1~4是1的倍数）
第二次操作[1 2 1 2 0]（2和4是2的倍数）
输出 [1 2 1 2 0]

数组a初始每个值为0，输入t组（l,r,v），在区间[l,r]中的v的倍数的索引对应的值+1，输出最终的数组a
如1,4,2，区间[1,4]中2的倍数为2, 4，（数组索引从0开始）即a[1],a[3]均+1

**正六边形求面积**

[原题-正六边形阴影面积计算](正六边形阴影面积计算)

知识点：数学（分隔6个三角形）***

正六边形每个点代表运动员某个维度的分值。中心点代表0，顶点代表100。正六边形边长为 L，每条轴分别用 x1, x2, ..., x6 代表学生的一项能力（0<=xi<=100，轴为 100），阴影面积代表综合能力。

输入：  
L  
x1 x2 x3 x4 x5 x6  
输出：  
阴影面积，要求输出误差小于1e-6。

```python
import sys
import math

def main():
    # read
    data = sys.stdin.read().split()
    L = float(data[0])
    abilities = list(map(float, data[1:7]))
    
    # initial
    lengths = [L * ability / 100.0 for ability in abilities]
    
    # calculate
    shadow_area = 0.0
    for i in range(6):
        j = (i + 1) % 6
        triangle_area = 0.5 * lengths[i] * lengths[j] * math.sin(math.pi / 3)
        shadow_area += triangle_area
    
    # output
    print("{:.7f}".format(shadow_area))

if __name__ == "__main__":
    main()
```

**分苹果**

知识点：二分查找、动态规划***

m 个苹果 n 个小孩。每个小孩 1-n 编号。小明的编号是 k。尽可能公平分配，相邻的小孩分到的数目差距不能大于 1。小明分到的苹果数目最多，输出最大值。每个小朋友至少分到一个苹果（m>=n>1, n>=k>=1）

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    m, n, k = int(data[0]), int(data[1]), int(data[2])
    
    # initial
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0
    
    # traverse
    for i in range(1, n + 1):
        for j in range(i, m + 1):
            for x in range(1, j - i + 2):
                if i > 1 and abs(x - dp[i-1][j-x]) > 1:
                    continue
                if i == k:
                    dp[i][j] = max(dp[i][j], x)
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-x])
    
    print(dp[n][m])

if __name__ == "__main__":
    main()
```

**病毒**

有一个病毒初始体积 t = 1，第 i 秒体积增加 i 平方。例如 i = 2，第2秒时，体积增加 2 * 2 = 4，则第2秒时病毒的体积为：1 + 4 = 5。
人类开发了病毒解药，解药能杀死体积为 k 的病毒。
输入 k，要求输出一次性能杀死病毒的最大体积。
例如：
k = 3，则输出 1。说明：k = 3 说明解药最多一次性杀死体积为 3 的病毒，而病毒在第一秒时体积为 1，第二秒时体积为 5，因此只能选择在第一秒杀死病毒，因此一次性能杀死体积为 1 的病毒
k = 9，则输出 5。说明：k = 9 说明解药最多一次性杀死体积为 9 的病毒，而病毒在第一秒时体积为 1，第二秒时体积为 5，第三秒时体积为 14，因此必须选择在第二秒杀死病毒，因此一次性能杀死体积为 5 的病毒。

**数组加减1**

长度为n的数组，对其元素进行加减一操作，问最少要操作多少次后满足：均值为m，最小值>=K

**子数组除法**

给一个数组n，进行k段切割（k>1）得到子数组，如果能找到index为k-1的子数组的和能整除index为k的子数组的和，则输出yes，否则输出No


**最大操作数计算（01字符串重排）（困难）**

小明原先有一个字符串S（字符串S中只包含0和1），但是由于特殊原因，S被打乱成了S’（字符串S‘中只包含0和1，且0，1的数量和原先S是一样的），现在小明知道字符串S’是什么样的。
现在小明只能通过交换S‘中相邻元素的值来尝试复原出字符串S（记一次交换为一次操作），可以确定的是：S‘变为S时，总的操作次数最大，请输出这个最大操作数。（根据题意和输入输出演示，1，1对调和0，0对调不计入操作数中）
输入S':001
输出：2
则S'通过操作后可能变成的（或者说’0‘，’0‘，’1‘组合成的）字符串一共有”001“，”100","010",操作数分别为 0，2，1，所以输出2 = max(0,2,1)，也就是这个例子中原先的S应当为”100“

### 2.9 其他

**两人相向行走（最小价值差）**

- [路径总和](https://leetcode.cn/problems/path-sum-ii/description/)

两个人从起点和终点往中间走，求走过节点的和delta最小是多少 两个人相向而行, 在路上经过一些数字, 每个数字的位置有不同的价值,分别计算两个人分别走几步,最好总价值的差值的绝对值最小,输出最小绝对值和分别走几步

给你一颗多叉树，但是保证根节点是1，给定每个节点的权值（一个数组），然后小美可以从根节点出发，在任意位置停下来（可以在叶子节点停，也可以中间停），给一个阈值m，求所有的路径中，路径和小于m的最大值
样例，一共5个节点，下面的5行表示5个节点，每一行的第一个数表示这个节点有几个子节点，这一行剩下的数字表示该节点的子节点。
1 2
1 3
1 4
1 5
0

**最长合法括号子序列**

"（'“）”组成的字符串，求最长的合法子序列长度
如：“（）”、“（）（）”、“（（））”、“（（）（））”均为合法子序列；“）（”、“（（”、“（（）”均为不合法子序列。

**括号序列期望**

字符串包含{,},?.小红有魔法，把？变成{或}的概率分别是50%。求组成括号对的期望E
输入：包含{，}，？的字符串
输出：期望E

输入字符串“()?)??)”，？为左右括号的概率0.5，计算一共有多少对括号（）

**括号有效性判断**

- [?有效的括号字符串](https://leetcode.cn/problems/valid-parenthesis-string/description/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号
给定一个输入，输出是否有效

```python
import sys

def is_valid(s: str) -> bool:
    """使用栈数据结构检查括号是否匹配"""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping.values():  # 左括号入栈
            stack.append(char)
        elif char in mapping.keys():  # 右括号检查匹配
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return not stack  # 栈空则匹配成功

def main():
    # 读取所有输入
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    # 解析测试用例数量
    n = int(data[0])
    
    # 处理每个测试用例
    for i in range(1, n + 1):
        s = data[i].strip()
        result = is_valid(s)
        print(str(result).lower())  # 输出true/false

if __name__ == "__main__":
    main()
```

**括号调整次数计算**

给定2个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断经过几次调整字符串把它变成有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号
如：
如：
输入:2
（ {[ ] ]）-> 一次调整
   （ {[ ] ]} ->两次调整
输出: 
1
2

- 未整理

**敏感词**

[类似](https://www.nowcoder.com/discuss/678023391353270272)

敏感词：给定一个字符串数组，表示敏感词；再给定一个字符串，表示需要查找的文本。问文本中的敏感词一共有多少？

**连续反转字符串**

[原题](https://blog.csdn.net/bthbt/article/details/138012290)

输入一个长度为n的字符串，输入一个整数k，对这k个数进行反转，i为1~n-k+1，例如，输入一个字符串长度为5的字符串Hello，输入k=3
i=1 对[1,3]字符串反转，结果为leHlo
i=2，对[2,4]字符串反转，结果为llHeo
i=3,对[3,5]字符串反转，结果为lloeH
最终输出lloeH

**完美集合**
[参考](https://blog.csdn.net/tomatoin/article/details/106599264)

完美集合，集合内没有重复数字为完美集合，能够删除k次，求删除k次后能否构成完美集合。
arr = [1, 2, 4, 6, 2, 4, 5];

**非递减数组**

知识点：贪心

长度为 N 的数组，每次操作可以对一个数加 1，计算数组变为非递减数组的最小操作数

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    if n <= 1:
        print(0)
        return
    
    # traverse
    count = 0
    prev = arr[0]
    for i in range(1, n):
        if arr[i] < prev:
            count += prev - arr[i]
        else:
            prev = arr[i]
    
    print(count)

if __name__ == "__main__":
    main()
```

**多字符串匹配**

给一个长字符串，给一堆小字符串，问出现的次数，如Helloworld，Hello world owo均出现一次

**最小操作树**

[原题](https://blog.csdn.net/DerrickKose/article/details/126885519)

一个数有n个节点，每个节点对应一个权值ai，输入第i根线连接节点v,u，多少次变化能使得节点数与权值对应

**最小权值和**

输入一个共3个数的数组，第一个数的权值为0，后面每个数的权值为当前数与前一个数作差的绝对值，三个数的顺序可以打乱，求这个数组权值和的最小值
例如给定5 5 11 权值和最小为6
排序 11 5 5 权值和为0+6+0结果为6

**数组区间内索引倍数值加1**

给定一个数组，将指定区间内索引为k的倍数的值加1，不断给出区间及k值，求出操作后最后的数组。
arr = [1, 3, 45, 67, 89, 23, 12, 11, 14]
[2, 8, 3]

**数组相减相等**

给一个非负数组， 1 2 3 ，每次取两个不同的数相减，结果替换其中一个，可以重复无限次，直到最后数组元素和最小，比如先取 1 2操作，得到1 1 3 再重复操作得到 1 1 1

**数组相减消除**

给定一个数组，任意两个数相减小于等于1就消掉任意一个数，问能否消除至一个数字。