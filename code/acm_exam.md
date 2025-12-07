# ACM

## 2 exam

### 2.1 搜索

**二叉树（树子节点颜色个数、树最近公共祖先、最小操作树）**

[参考-字母树](https://www.nowcoder.com/discuss/395546774016991232)

知识点：树遍历****24

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

知识点：BFS、队列

[原题-最小操作树](https://blog.csdn.net/DerrickKose/article/details/126885519)

给定一颗根为 1 号节点的数，每个节点初始权值为 1。现在每次可以选择一个节点，使其子树所有节点的权值加 1，最少多少次操作可以使得每个节点的权值等于其编号。  

第一行：树上节点数量 - 2≤n≤100000；  
接下来n-1行：u号节点和v号节点间有一条边相连 - 1≤u,v≤n  

输出最小操作次数  

示例 1：  
输入：  
3    
1 2    
1 3     
输出：    
3  

```python
import sys
from collections import defaultdict, deque

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    
    # build tree
    tree = defaultdict(list)
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        tree[u].append(v)
        tree[v].append(u)
    
    # BFS
    visited = [False] * (n + 1)
    depth = [0] * (n + 1)
    operations = 0
    
    queue = deque()
    queue.append(1)
    visited[1] = True
    depth[1] = 1
    
    while queue:
        node = queue.popleft()
        operations += depth[node]
        
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)
    
    print(operations)

if __name__ == "__main__":
    main()
```

**字符查找（敏感词、字符串匹配）**

知识点：滑动窗口

[类似-敏感词](https://www.nowcoder.com/discuss/678023391353270272)

给定一个字符串数组，表示敏感词；再给定一个字符串，表示需要查找的文本。问文本中的敏感词一共有多少？

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    sensitive_words = []
    i = 0
    while i < len(data) and data[i].strip():
        sensitive_words.append(data[i].strip())
        i += 1
    text = data[i].strip() if i < len(data) else ""
    
    # count
    total_count = 0
    for word in sensitive_words:
        count = 0
        start = 0
        while True:
            pos = text.find(word, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1
        total_count += count
    
    print(total_count)

if __name__ == "__main__":
    main()
```

知识点：滑动窗口

给一个长字符串，给一堆小字符串，问出现的次数，如Helloworld，Hello world owo均出现一次

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    text = data[0].strip()
    patterns = [line.strip() for line in data[1:] if line.strip()]
    
    result = {}
    for pattern in patterns:
        count = 0
        start = 0
        while True:
            pos = text.find(pattern, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1
        result[pattern] = count
    
    for pattern in patterns:
        print(f"{pattern}: {result[pattern]}")

if __name__ == "__main__":
    main()
```

**连续反转字符串**

[原题-连续反转字符串](https://blog.csdn.net/bthbt/article/details/138012290)

知识点：滑动窗口、队列

输入一个长度为 n 的字符串，输入一个整数 k，对这 k 个数进行反转，i 为 1~n-k+1，例如，输入一个字符串长度为 5 的字符串Hello，输入 k=3  
i=1 对[1,3]字符串反转，结果为leHlo
i=2，对[2,4]字符串反转，结果为llHeo
i=3,对[3,5]字符串反转，结果为lloeH
最终输出lloeH

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    k = int(data[1])
    
    n = len(s)
    result = list(s)
    
    # traverse
    for i in range(n - k + 1):
        left, right = i, i + k - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

    print(''.join(result))

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

### 2.2 排序

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

### 2.4 回溯

### 2.5 动态规划

**切割字符串（质数和）**

知识点：位运算、DFS、回溯****8

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

**牛牛吃饭期望**

知识点：数学****5

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

**包粽子**

知识点：动态规划（背包）****15

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

**小明打地鼠（困难）**

知识点：动态规划****17

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

### 2.6 贪心

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

**商店购物**

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

知识点：贪心****23

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

**木板排列**

[参考-最大正方形面积](https://blog.csdn.net/qq_20091631/article/details/142135903)

知识点：贪心、二分查找****19

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

知识点：枚举****6

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

[参考-两数之和](https://leetcode.cn/problems/two-sum/)

知识点：贪心、哈希****10

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

**最大异或数**

知识点：贪心、位运算、动态规划****11

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

[参考-对称数组](https://blog.csdn.net/qq_55207368/article/details/147232170)

知识点：贪心、双指针、队列****16

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

**最少交换次数**

知识点：图论（环分解）、贪心、逆序对****20

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

**完美集合**

知识点：贪心

[参考-完美的数组](https://blog.csdn.net/tomatoin/article/details/106599264)

完美集合，集合内没有重复数字为完美集合，能够删除k次，求删除k次后能否构成完美集合。
arr = [1, 2, 4, 6, 2, 4, 5];

```python
import sys
from collections import defaultdict

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data[:-1]))
    k = int(data[-1])

    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1

    deletions_needed = 0
    for count in freq.values():
        if count > 1:
            deletions_needed += count - 1
    
    if deletions_needed <= k:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
```

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

### 2.7 模拟

**数字整除特性**

知识点：遍历****22

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

知识点：ASCII映射

已知大写字母ASCII值'A'=65，给出一个字符串，求字符串中没有出现的字母ASCII和

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip().upper()
    
    total_ascii = sum(range(65, 91))
    appeared_ascii = 0
    appeared_letters = set()
    for char in s:
        if 'A' <= char <= 'Z' and char not in appeared_letters:
            appeared_ascii += ord(char)
            appeared_letters.add(char)

    result = total_ascii - appeared_ascii
    print(result)

if __name__ == "__main__":
    main()
```

**好格子**

知识点：BFS****9

有红、蓝、空的格子（矩阵），红格子上下左右如果有蓝格子，则这个格子定义为好格子，求好格子数量

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    
    grid = []
    for i in range(1, n + 1):
        grid.append(list(data[i].strip()))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    good_cells = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 'B':
                        good_cells += 1
                        break
    
    print(good_cells)

if __name__ == "__main__":
    main()
```

**密文解密**

[参考-小红切字符串](https://www.nowcoder.com/questionTerminal/f3ff2b43d0ee4c6ca7af9e93f81d382b)

知识点：查找

小明收到一串只包含小写字母的密文，解密的规则如下：
（1）如果字符是元音字母，则不作任何改变；
（2）如果字符是辅音字母，则将其替换为以下连续的三个字母：
① 第一位为原字母的本身
② 第二位为离其最近的元音字母，如果与两个元音字母的距离相等，则选择离a这边最近的，不选离z这边近的。
③ 第三位切换原字母的大小写
    请输出解密后的明文。
    例如，元音字母为a、e、i、o、u。输入"ac",输出"acaC"

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    
    vowels = set('aeiou')
    result = []
    
    for char in s:
        if char in vowels:
            result.append(char)
        else:
            result.append(char)
            c = char
            distance = 0
            found_vowel = None
            
            while found_vowel is None:
                distance += 1
                prev_char = chr(ord(c) - distance)
                if prev_char >= 'a' and prev_char in vowels:
                    found_vowel = prev_char
                    break
                next_char = chr(ord(c) + distance)
                if next_char <= 'z' and next_char in vowels:
                    found_vowel = next_char
                    break
            
            result.append(found_vowel)

            result.append(char.upper())
    
    print(''.join(result))

if __name__ == "__main__":
    main()
```

**包车**

知识点：区间判断****14

包车，[l,r]区间如果没有人定，则包车成功。输入T组区间，按顺序判断是否可以包车，统计可以包车的区间数量。

```python
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    T = int(data[0])
    booked = []
    success_count = 0
    
    for i in range(1, T + 1):
        l, r = map(int, data[i].split())
        can_book = True
        for start, end in booked:
            if not (r < start or l > end):
                can_book = False
                break
        
        if can_book:
            success_count += 1
            booked.append((l, r))
    
    print(success_count)

if __name__ == "__main__":
    main()
```

**字符串插入**

知识点：双指针****21

一个有字符串str是否能够由ab通过任意位置插入构成，若能构成输出YES，否则NO。
比如：abab、aabb YES； aaab NO；

```python
import sys
import re

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()

    pattern = r'^(a+|b+|a+b+|b+a+)$'
    
    if re.match(pattern, s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
```

**数组删除**

知识点：贪心

给定一个数组，任意两个数相减小于等于 1 就消掉任意一个数，问能否消除至一个数字。

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data))
    if len(arr) == 1:
        print("true")
        return
    
    arr.sort()
    can_eliminate = True
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            can_eliminate = False
            break
    
    print("true" if can_eliminate else "false")

if __name__ == "__main__":
    main()
```

数组n，随机取i，j，如果|n[i]-n[j]|<=1，删除大的那个值，  
求数组最终能否只剩一个值

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data))
    
    if not arr:
        print("false")
        return
    
    min_val = min(arr)
    max_val = max(arr)

    if max_val - min_val <= 1:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
```

**删除公共字符**

[原题](https://www.nowcoder.com/practice/f0db4c36573d459cae44ac90b90c6212)


### 2.8 数学

**骰子期望次数**

知识点：数学****18

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

**减2^k操作次数（困难）**

知识点：贪心、位运算****4

给你一个数组，你可以选择2的k次方的数，来对这个数组中的数字进行相减，问当数组中的数字全都变成0的时候，最小的操作次数。（15分）
1 2 3
第一次使用2来对2和3进行操作，变成 1 0 1  
第二次使用1对剩余进行操作，变成 0 0 0  
一共两次操作次数

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data))
    
    needed_powers = set()
    
    for num in arr:
        while num > 0:
            lowest_bit = num & -num
            needed_powers.add(lowest_bit)
            num -= lowest_bit
    
    print(len(needed_powers))

if __name__ == "__main__":
    main()
```

**火箭飞出大气层**

知识点：数学****7

发射火箭，地球半径为R，球心坐标为（0，0，0），发射点坐标为x,y,z，火箭三个坐标向的速度为vx，vy，vz，请问火箭飞出大气层的时刻，输入t组，每组一行，每行行输入分别为，y，z，vx，vy，vz，R，每行输出一个时刻

```python
import sys
import math

def main():
    # read
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    
    results = []
    for i in range(1, t + 1):
        x, y, z, vx, vy, vz, R = map(float, data[i].split())
        
        a = vx*vx + vy*vy + vz*vz
        b = 2*(x*vx + y*vy + z*vz)
        c = x*x + y*y + z*z - R*R
        
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            results.append("0")
        else:
            t1 = (-b + math.sqrt(discriminant)) / (2*a)
            t2 = (-b - math.sqrt(discriminant)) / (2*a)
            if t1 > 0 and t2 > 0:
                result = min(t1, t2)
            elif t1 > 0:
                result = t1
            elif t2 > 0:
                result = t2
            else:
                result = 0
            results.append(f"{result:.6f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

**区间操作（倍数下标加1）**

知识点：数学****12

一个长度为n，值为0的数组，每次输入三个数l,r,v，在区间 [l, r]，如果索引是v的倍数，则该索引对应的值＋1，输出最终数组
例
5 2
1 4 1
1 5 2
第一次操作[1 1 1 1 0]（1~4是1的倍数）
第二次操作[1 2 1 2 0]（2和4是2的倍数）
输出 [1 2 1 2 0]


```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    q = int(data[1])
    
    arr = [0] * n
    idx = 2
    
    for _ in range(q):
        l = int(data[idx]) - 1
        r = int(data[idx + 1]) - 1
        v = int(data[idx + 2])
        idx += 3
        
        start = (l // v) * v
        if start < l:
            start += v
        
        for i in range(start, r + 1, v):
            arr[i] += 1
    
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
```

**子数组除法**

知识点：枚举****25

给一个数组n，进行k段切割（k>1）得到子数组，如果能找到index为k-1的子数组的和能整除index为k的子数组的和，则输出yes，否则输出No

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    found = False
    for k in range(2, n + 1):
        if prefix[k - 1] != 0 and (prefix[n] - prefix[k - 1]) % prefix[k - 1] == 0:
            found = True
            break
    
    print("Yes" if found else "No")

if __name__ == "__main__":
    main()
```

**最小权值和**

知识点：数学

输入一个共3个数的数组，第一个数的权值为0，后面每个数的权值为当前数与前一个数作差的绝对值，三个数的顺序可以打乱，求这个数组权值和的最小值
例如给定5 5 11 权值和最小为6
排序 11 5 5 权值和为0+6+0结果为6

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    nums = list(map(int, data))
    
    nums.sort()
    a, b, c = nums
    min_weight = c - a
    
    print(min_weight)

if __name__ == "__main__":
    main()
```

**数组区间内索引倍数值加1**

知识点：模运算

给定一个数组，将指定区间内索引为k的倍数的值加1，不断给出区间及k值，求出操作后最后的数组。
arr = [1, 3, 45, 67, 89, 23, 12, 11, 14]
[2, 8, 3]

```python
import sys

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data[:9]))
    operations = list(map(int, data[9:])) 
    
    # traverse
    for i in range(0, len(operations), 3):
        start = operations[i] - 1
        end = operations[i + 1] - 1
        k = operations[i + 2]
        for j in range(start, end + 1):
            if (j + 1) % k == 0:
                arr[j] += 1
    
    # output
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
```

**数组相减相等**

知识点：数学

给一个非负数组， 1 2 3 ，每次取两个不同的数相减，结果替换其中一个，可以重复无限次，直到最后数组元素和最小，比如先取 1 2操作，得到1 1 3 再重复操作得到 1 1 1

```python
import sys
import math
from functools import reduce

def main():
    # read
    data = sys.stdin.read().split()
    arr = list(map(int, data))
    
    # gcd
    gcd_all = reduce(math.gcd, arr)
    max_val = max(arr)
    result = [i for i in range(0, max_val + 1, gcd_all)]
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

### 2.9 其他

**判断字符串符合条件的好串最大数？**

**计算工资**

知识点：数学****26

第一个月工资a元，每个月工资递增b元，求第N个月的时候，工资总和。