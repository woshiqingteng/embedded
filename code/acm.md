# ACM Mode

## 0 ACM template

### 0.1 python

#### 0.1.1 input

**single-line input with same type**

```python
data = list(map(int, input().split()))
print(data)

# 示例输入: 1 2 3 4 5
# 输出: [1, 2, 3, 4, 5]
```

**single-line input with different types**

```python
line = input().split()
n = int(line[0])
m = float(line[1])
s = line[2]
print(f"整数: {n}, 浮点数: {m}, 字符串: {s}")

# 示例输入: 42 3.14 hello
# 输出: 整数: 42, 浮点数: 3.14, 字符串: hello
```

**multi-line input with fixed rows**

```python
"""Method 1"""
n = int(input())
data = []
for i in range(n):
    line = list(map(int, input().split()))
    data.append(line)
print(data)

# 示例输入:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 输出: [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

"""Method 2"""
n = int(input())
pairs = []
for i in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))
print(pairs)

# 示例输入:
# 3
# 1 2
# 3 4
# 5 6
# 输出: [(1, 2), (3, 4), (5, 6)]
```

**multi-line input with unfixed rows**

```python
"""Method 1: EOF"""
import sys

data = []
for line in sys.stdin:
    if not line.strip():  # 空行判断
        break
    nums = list(map(int, line.split()))
    data.append(nums)
print(data)

"""Method 2: specific termination"""
data = []
while True:
    line = input().strip()
    if line == "" or line == "0":  # 空行或特定值终止
        break
    nums = list(map(int, line.split()))
    data.append(nums)
print(data)
```

**small data input**

`input()`

**large data input**

`sys.stdin.readline()`

#### 0.1.2 output

**small data output**
`print()`

**large data output**

`sys.stdout.write()`

#### 0.1.2 template

**small data**

```python
def main():
    #
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 
    result = sum(arr) * m
    
    #
    print(result)

if __name__ == "__main__":
    main()
```

**large data**

```python
import sys

def main():
    #
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    # 
    result = sum(arr) * m
    
    #
    sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
    main()
```

## 1 11月编程考试练习题

### 1.1 小苯的数字权值 *

**知识点：数论**

**描述**

定义正整数 n 的权值为 n 的正因子的数量，即

$wt(n)=\tau(n)，$

其中 $\tau(n)$ 表示 n 的因子个数。

给定一个正整数 x，你可以将 x 分解为若干个大于 1 的正整数 $p_1, p_2, \cdots, p_k (k \ge 1)$，要求

$p_1 \times p_2 \times \cdots \times p_k = x$；

最大化

$\sum_{i=1}^{k} wt(p_i)$。

请你求出在最优分解下，上述表达式的最大可能值。

**输入描述：**

第一行输入一个整数 $T (1 \le T \le 10^4)$ 表示测试数据组数。

此后 T 行，每行输入一个整数 $x (2 \le x \le 2 \times 10^5)$。

**输出描述：**

对于每组数据，在一行上输出对应的最大权值和。

**示例 1**

> 输入
>
>> 3  
>> 2  
>> 10  
>> 123  
>
> 输出
>
>> 2  
>> 4  
>> 4  
> 
> 说明
>> 对于 x=2，无法再分解，只能取自身，wt(2)=2。  
>> 对于 x=10，最优方案为 $10=2 \times 5$，wt(2)=2, wt(5)=2，总和 2+2=4。  
>> 对于 x=123，最优方案为 $123=3 \times 41$，wt(3)=2, wt(41)=2，总和 4。

**python**

```python
""" 
质因数分解
单一质因子幂->拆成多个质数
多个质因子->不拆分
"""

import sys

def solve(x):
    v = []  # 记录质因子和其出现的次数
    i = 2
    while i * i <= x:
        if x % i:
            i += 1
        else:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            v.append((i, cnt))
    if x > 1:
        v.append((x, 1))
    if len(v) == 1: 
        return v[0][1] * 2  # 只有一个质因子
    res = 1
    for t in v:
        res *= (t[1] + 1)
    return res

def main():
    data = sys.stdin.read().split()
    T = int(data[0])
    nums = list(map(int, data[1:1 + T]))
    
    for num in nums:
        result = solve(num)
        print(result)

if __name__ == "__main__":
    main()
```

### 1.2 小红的子序列逆序对 *

* 1

**知识点：动态规划、归并排序、树状数组**

**描述**

小红拿到了一个数组，她想知道该数组所有子序列的逆序对数量之和是多少？

定义一个数组的子序列是，数组中取若干元素（可以不连续）按原数组顺序形成的新数组。

**输入描述：**

第一行输入一个正整数 n，代表数组的大小。

第二行输入 n 个正整数 $a_i$，代表数组的元素。

$1 \le n, a_i \le 10^5$

**输出描述：**

一个整数，代表所有子序列的数量之和。由于答案过大，请对 $10^9+7$ 取模。

**示例 1**

> 输入
>
>> 3  
>> 2 3 1
> 
> 输出
>
>> 4
>
> 说明：
>
>> [2, 3, 1] 的逆序对数量为 2，[2, 1] 和 [3, 1] 的逆序对数量为1，其余逆序对数量为0。

**python**

```python
""" 
            time        space
1 树状数组  O(nlogn)    O(n)
2 动态规划  O(n^2)      O(n)
3 归并排序  O(nlogn)    O(n)
"""

import sys

MOD = 10**9 + 7

def count_inversions(arr):
    if len(arr) <= 1:
        return 0, arr
    
    mid = len(arr) // 2
    left_count, left_sorted = count_inversions(arr[:mid])
    right_count, right_sorted = count_inversions(arr[mid:])
    
    merge_count, merged = merge(left_sorted, right_sorted)
    total_count = (left_count + right_count + merge_count) % MOD
    
    return total_count, merged
    
def merge(left, right):
    merged = []
    i = j = 0
    count = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i  # All remaining elements in left are greater than right[j]
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return count, merged

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    if n == 0:
        print(0)
        return
    
    arr = list(map(int, data[1:1+n]))
    
    if n < 2:
        print(0)
        return
    
    # Count inversions in the array
    inversion_count, _ = count_inversions(arr.copy())
    
    # Calculate 2^(n-2) mod MOD
    power = pow(2, n-2, MOD)
    
    # Total = inversion_count * 2^(n-2) mod MOD
    result = (inversion_count * power) % MOD
    
    print(result)

if __name__ == "__main__":
    main()
```

### 1.3 小美的彩带（python3超时，pypy3通过）

* 1

**知识点：树状数组、离线查询**

**描述**

小美的彩带是由一条长度为 n 的彩带一直无限循环得到的，彩带的每一个位置都有一个颜色，用 $a_i$  表示。因此当 $i>n$ 时，$a_i = a_{i-n}$。

小美每次会从左往右或从右往左剪一段长度为 x 的彩带，她想知道她每次剪下来的彩带有多少种颜色。

**输入描述**

第一行输入两个整数 $n, q(1 \le n, q \le 2 \times 10^5 )$ 代表彩带长度、剪彩带次数。
 
第二行输入 n 个整数 $a_1, a_2, \cdots, a_n (1 \le a_i \le 10^9)$ 代表彩带每一个位置的颜色。
 
此后 q 行，每行输入一个字符 c 和一个整数 $x (1 \le x \le 10^9; c \in 'L', 'R')$ 代表裁剪方向和裁剪长度，其中 'L' 说明从左往右剪，'R' 说明从右往左剪。

**输出描述**

对于每一次裁剪彩带，在一行上输出一个整数代表颜色数量。

**示例 1**

> 输入
>
>> 6 4  
>> 1 1 4 5 1 4  
>> L 2  
>> L 3  
>> R 12  
>> R 1  
>
> 输出
>
>> 1  
>> 3  
>> 3  
>> 1
>
> 说明
>  
>> 第一次剪彩带，剪下来的是 [1, 1] ，有 {1} 这 1 种颜色；  
>> 第二次剪彩带，剪下来的是 [4, 5, 1] ，有 {1, 4, 5} 这 3 种颜色；  
>> 第三次剪彩带，剪下来的是 [4, 1, 5, 4, 1, 1, 4, 1, 5, 4, 1, 1] ，有 {1, 4, 5} 这 3 种颜色。  
>> 第四次剪彩带，剪下来的是 [4] ，有 {4} 这一种颜色。

**python**

```python
"""
python3超时，pypy3通过
"""
import sys
from array import array

def main():
    input = sys.stdin.readline
    n0, q = map(int, input().split())
    arr = list(map(int, input().split()))
    N = n0 * 2

    # 坐标压缩
    vals = sorted(set(arr))
    comp = {v: i for i, v in enumerate(vals)}
    M = len(vals)

    b = array('I', [0]) * N
    for i in range(n0):
        cv = comp[arr[i]]
        b[i] = cv
        b[i + n0] = cv

    # 读取查询，生成 L/R
    Ls = [0] * q
    Rs = [0] * q
    l = 0
    r = N - 1
    for idx in range(q):
        parts = input().split()
        c = parts[0]
        x = int(parts[1])
        if c == 'L':
            R = l + x - 1
            if R >= N:
                Lq, Rq = 0, n0 - 1
            else:
                Lq, Rq = l, R
            y = x % N
            l += y
            if l >= n0: l -= n0
            if l >= n0: l -= n0
        else:
            L = r - x + 1
            if L < 0:
                Lq, Rq = 0, n0 - 1
            else:
                Lq, Rq = L, r
            y = x % N
            r -= y
            if r < n0: r += n0
            if r < n0: r += n0
        Ls[idx] = Lq
        Rs[idx] = Rq

    # 链表桶：list of list
    head = [[] for _ in range(N)]
    for i in range(q):
        head[Ls[i]].append(i)

    # Fenwick Tree + last
    bit = array('i', [0]) * (N + 1)
    last = array('i', [0]) * M
    ans = [0] * q

    # 本地引用
    b_local = b
    head_local = head
    last_local = last
    bit_local = bit
    ans_local = ans
    N_local = N

    # 主循环，从右向左
    for pos in range(N_local - 1, -1, -1):
        v = b_local[pos]
        prev = last_local[v]
        if prev != 0:
            # BIT add -1
            i = prev
            t = bit_local
            while i <= N_local:
                t[i] -= 1
                i += i & -i
        # BIT add +1
        i = pos + 1
        t = bit_local
        while i <= N_local:
            t[i] += 1
            i += i & -i
        last_local[v] = pos + 1

        # 回答查询
        bucket = head_local[pos]
        for qi in bucket:
            Rpos = Rs[qi]
            # BIT sum
            s = 0
            j = Rpos + 1
            t = bit_local
            while j > 0:
                s += t[j]
                j -= j & -j
            ans_local[qi] = s

    # 输出
    sys.stdout.write('\n'.join(map(str, ans_local)) + '\n')


if __name__ == "__main__":
    main()
```

### 1.4 小美和大富翁 *

**描述**

小美在玩《大富翁》游戏，游戏中有 n + 1 个城市排成一排，编号从 0 到 n，第 i 个城市上有一个数字 $a_i$，表示到达第 i 个城市可以获得 $a_i$ 枚金币。

每一轮开始时小美会获得四张卡牌，分别可以跳跃 1、2、3、4 个城市，例如小美可以从城市 1 跳跃 3 个城市到达城市 4。当小美使用完这 4 张卡牌后，会开启新的一轮。

初始时，小美拥有 0 枚金币，在任意时刻，小美的金币数量都必须大于等于 0，小美想知道她从第 0 个城市出发，到达第 n 个城市最多可以获得多少枚金币。

**输入描述**

第一行输入一个整数 $n ( 1 \le n \le 10^5)$ 表示城市个数。

第二行输入 n 个整数 $a_1, a_2, \cdots, a_n (-10^9 \le a_i \le 10^9 )$ 表示到达城市 1 到 n 可以获得的金币数量（第 0 个城市无法获得金币）。
**输出描述**

在一行上输出一个整数表示答案；如果无法到达第 n 个城市，则输出 -1。

**示例 1**

> 输入
>> 10  
>>
>> -1 2 3 4 -9 -9 -1 3 -1 -1  
>
> 输出  
>
>>9  
>
> 说明
>
>> 最优的方法是：  
>>
>> 第 1 步：使用跳跃 3 的卡牌，从 0 跳到 3，获得 3 枚金币；  
>>
>> 第 2 步：使用跳跃 1 的卡牌，从 3 跳到 4，获得 4 枚金币，共有 7 枚金币；  
>>
>> 第 3 步：使用跳跃 4 的卡牌，从 4 跳到 8，获得 3 枚金币，共有 10 枚金币；  
>>
>> 第 4 步：使用跳跃 2 的卡牌，从 8 跳到 10，获得 -1 枚金币，共有 9 枚金币。

**python**

```python
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = [0] + list(map(int, input().split()))  # 城市编号从1开始，a[0]=0

    f = [[-1]*16 for _ in range(n+1)]  # f[i][j]表示到达城市i，状态j的最大金币
    f[0][15] = 0  # 起点状态，15表示所有4张卡牌都可用

    for i in range(1, n+1):
        for j in range(1, 16):  # 当前状态
            for k in range(4):  # 使用跳跃卡牌1~4
                if (j >> k) & 1:  # 如果卡牌k+1未使用过，不可用
                    continue
                last_state = j ^ (1 << k)
                last_pos = i - (k + 1)
                if last_pos < 0:
                    continue
                if f[last_pos][last_state] == -1:
                    continue
                if f[last_pos][last_state] + a[i] < 0:
                    continue
                f[i][j] = max(f[i][j], f[last_pos][last_state] + a[i])
        # 单独考虑j=15（新一轮开始）
        for k in range(4):
            last_pos = i - (k + 1)
            if last_pos < 0:
                continue
            last_state = 1 << k
            if f[last_pos][last_state] == -1:
                continue
            if f[last_pos][last_state] + a[i] < 0:
                continue
            f[i][15] = max(f[i][15], f[last_pos][last_state] + a[i])

    res = max(f[n])
    print(res)

if __name__ == "__main__":
    main()
```

### 1.5 小美的数组删除 *

**描述**

小美有一个长度为 n 的数组 $a_1, a_2, \cdots, a_n$，他可以对数组进行如下操作：
- 删除第一个元素 $a_1$，同时数组的长度减一，花费为 x。
- 删除整个数组，花费为 $k \times MEX(a)$（其中 MEX(a) 表示 a 中未出现过的最小非负整数。例如 [0, 1, 2, 4] 的 MEX 为 3）。

小美想知道将 a 数组全部清空的最小代价是多少，请你帮帮他吧。

   **输入描述**

每个测试文件均包含多组测试数据。第一行输入一个整数 $ T (1 \le T \le 1000)$ 代表数据组数，每组测试数据描述如下：

第一行输入三个正整数 $n, k, x (1 \le n \le 2 \times 10^5, 1 \le k, x \le 10^9)$ 代表数组中的元素数量、删除整个数组的花费系数、删除单个元素的花费。

第二行输入 n 个整数 $a_1, a_2, \cdots, a_n (0 \le a_i \le n)$，表示数组元素。

除此之外，保证所有的 n 之和不超过 $2 \times 10^5$。

**输出描述**

对于每一组测试数据，在一行上输出一个整数表示将数组中所有元素全部删除的最小花费。

**示例 1**

> 输入
> 
>> 1
>>
>> 6 3 3
>>
>> 4 5 2 3 1 0
>
> 输出
> 
>> 15
>
> 说明
> 
>> 若不执行操作一就全部删除，MEX{4, 5, 2, 3, 1, 0} = 6，花费 18；
>> 
>> 若执行一次操作一后全部删除，MEX{5, 2, 3, 1, 0} = 4，花费 3 + 12；
>> 
>> 若执行两次操作一后全部删除，MEX{2, 3, 1, 0} = 4，花费 6 + 12；
>> 
>> 若执行三次操作一后全部删除，MEX{3, 1, 0} = 2，花费 9 + 6；
>> 
>> 若执行四次操作一后全部删除，MEX{1, 0} = 2，花费 12 + 6；
>> 
>> 若执行五次操作一后全部删除，MEX{0} = 1，花费 15 + 3；
>> 
>> 若执行六次操作一，MEX{} = 0，花费 18；

**python**

```python
""" 
枚举+哈希表
"""
T = int(input())
for _ in range(T):
    n, k, x = map(int, input().split())
    a = [0]+list(map(int, input().split()))
    res = 10**18  # 初始化最小花费为一个极大值
    mex = 0  # 表示数组a中未出现过的最小非负整数
    nums_set = set()  # 存储a数组的所有元素
    for i in range(n, -1, -1):
        while mex in nums_set:  # 当前while循环最多只会执行n次
            mex += 1
        res = min(res, i * x + mex * k)
        nums_set.add(a[i ])
    print(res)
```

### 1.6 小美的数字删除（部分通过） *

**描述**

小红拿到了一个正整数，她每次可以删除其中一个数位，但必须保证每次删除后，该正整数都是 3 的倍数且大于 0。小红想知道，自己最多可以进行多少次这样的删除操作？

**输入描述**

有多组数据，第一行输入一个整数 T，代表数据组数。

接下来 T 行，每行一个正整数 n。

$1 \le T \le 100$  

$1 \le n \le 10^{1000}$

**输出描述**

输出 T 行，表示每组数据的答案。

**示例 1**

> 输入
>> 
>> 2
>>
>> 25
>>
>> 333
> 
> 输出
> 
>> 0
>>
>> 2
> 
> 说明
> 
>> 第一组数据：显然小红不能进行任何操作。  
>>
>> 第二组数据：可以删两次 3。

**示例 2**

> 输入
> 
>> 1
>>
>> 103252
>
> 输出
> 
>> 2
> 
> 说明
> 
>> 第一次必须删除第一个数 1（删除其他的数均不能保证变成 3 的倍数），该数变为 3252。  
>>
>> 第二次删除第一个数 3，该数变成 252。

**python**

```python
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        s = data[index]
        index += 1
        
        # 计算数字和模3
        total = sum(int(char) for char in s) % 3
        count = 0
        current = s
        
        # 阶段1: 如果总和模3不为0，删除一个使模3为0的数字
        if total != 0:
            found = False
            # 从右向左查找可以删除的数字
            for i in range(len(current)-1, -1, -1):
                if int(current[i]) % 3 == total:
                    new_s = current[:i] + current[i+1:]
                    # 移除前导零
                    new_s_stripped = new_s.lstrip('0')
                    if new_s_stripped:
                        current = new_s_stripped
                        count += 1
                        found = True
                        break
            if not found:
                results.append(str(count))
                continue
        
        # 阶段2: 删除模3为0的数字
        while len(current) > 1:
            found = False
            # 从右向左查找可以删除的模3为0的数字
            for i in range(len(current)-1, -1, -1):
                if int(current[i]) % 3 == 0:
                    new_s = current[:i] + current[i+1:]
                    new_s_stripped = new_s.lstrip('0')
                    if new_s_stripped:
                        current = new_s_stripped
                        count += 1
                        found = True
                        break
            if not found:
                break
        
        results.append(str(count))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

### 1.7 小美的数字串 *

**描述**

小红拿到了一个数字串（由 '1'~'9' 组成，不含 '0'），她准备截取一段连续子串，使得该子串表示的正整数小于 k。你能帮她求出有多少种截取方案吗？

**输入描述**

第一行输入一个数字串，长度不超过200000。

第二行输入一个正整数 k。

$1 \le k \le 10^9$

**输出描述**

小于 k 的截取方案数。

**示例 1**

>输入
> 
>> 1234
>>
>> 23 
>
> 输出
> 
>> 5
> 
> 说明
> 
>> 共有1, 2, 3, 4, 12这五种截取方法。

**python**

```python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
     
    s = data[0]
    k = int(data[1])
 
    count = 0
    n = len(s)
 
    for i in range(n):
        if s[i] == '0':
            continue  # 跳过以 0 开头的子串
         
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num >= k:
                break
            count += 1
 
    print(count)
 
if __name__ == "__main__":
    main()
```

### 1.8 小美的 01 串 *

**描述**

小红拿到了一个 01 串。所谓 01 串，指仅由 '0' 和 '1' 两种字符组成的字符串。

小红可以进行任意次以下操作：
- 选择字符串的一个字符，将其取反（'0' 变 '1' 或者 '1' 变 '0'）。

小红定义一个 01 串为好串，当且仅当该 01 串不包含 "010" 子串和 "101" 子串。

例如，"1001"是好串，但 "100100" 则不是好串。

小红想知道，自己最少操作多少次可以将给定字符串变成好串？

**输入描述**

一个长度不超过 100000的、仅由 '0' 和 '1' 组成的字符串。

**输出描述**

一个整数，代表该字符串变成好串的最小操作次数。

**示例 1**

> 输入
>
>> 1001
>
> 输出
>
>> 0

**示例 2**

> 输入
>
>> 100100
>
> 输出
>
>> 1
>
> 说明
>
>> 变成 100110 即可。仅需操作一次。

**python**

```python
import sys

for i in sys.stdin:
    s = i.strip()
    ans = 0
    n = len(s)
    idx = 0
    while idx < n - 3:
        if s[idx : idx + 3] in ["101", "010"]:
            ans += 1
            idx += 3
        else:
            idx += 1
    print(ans)
```

### 1.9 小红的爆炸串（二） *

**描述**

小红定义一个字符串会爆炸，当且仅当至少有 k 对相邻的字母不同。

例如，当 k = 2 时，"arc" 会爆炸，而 "aabb" 则不会爆炸。

小红拿到了一个长度为 n 的字符串，她想知道该字符串中有多少子串是不会爆炸的？

**输入描述**

第一行输入两个正整数 n 和 k，用空格隔开。

第二行输入一个长度为 n 的字符串。

$1 \le k \le n \le 2 \times 10^5$

**输出描述**

一个整数，代表不会爆炸的子串数量。

**示例 1**

> 输入
> 
>> 4 1
>>
>> abba
> 
> 输出
> 
>> 5
> 
> 说明
> 
>> 长度为 1 的子串均不会爆炸。
>>
>> 长度为 2 的子串只有 "bb" 不会爆炸。
>>
>> 其余子串均会爆炸。

**python**

```python
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    s = data[2].strip()
    
    # 预处理前缀和数组
    # pre_sum[i] 表示 s[0..i-2] 中相邻字母不同的对数
    pre_sum = [0] * (n + 1)
    # pre_sum[0] = 0, pre_sum[1] = 0 (单个字符没有相邻对)
    for i in range(2, n + 1):
        # 检查 s[i-2] 和 s[i-1] 是否不同
        if s[i-2] != s[i-1]:
            pre_sum[i] = pre_sum[i-1] + 1
        else:
            pre_sum[i] = pre_sum[i-1]
    
    ans = 0
    # 对于每个左端点 l
    for l in range(n):
        # target = pre_sum[l+1] + k
        target = pre_sum[l+1] + k
        
        # 在 pre_sum[l+1..n] 中查找第一个 >= target 的位置
        # bisect_left 返回插入位置，使得所有左边的元素都 < target
        idx = bisect.bisect_left(pre_sum, target, l+1, n+1)
        
        # 满足条件的子串数量 = max(0, idx - l - 1)
        count = idx - l - 1
        if count > 0:
            ans += count
    
    sys.stdout.write(str(ans))

if __name__ == "__main__":
    main()
```

### 1.10 小红拼图（缺少图片） *

**描述**

小红正在玩一个拼图游戏，她有一些完全相同的拼图组件：

小红准备用这些组件来拼成一些图案。这些组件可以通过顺时针旋转 90 度、180 度、270 度变成不同的形态。我们定义旋转 0 度用字符 'W' 表示，旋转 90 度用字符 'D' 表示，旋转 180 度用字符 'S' 表示，旋转270度用字符 'A' 表示：

小红想知道，自己是否能按照给定的规则拼出图形？

请注意：若两个组件相邻，那么必须凹进去的和凸出来的完美契合！“凸凸”和“凹凹”的相邻都是不合法的。

**输入描述**

第一行输入一个正整数 t，代表询问次数。

每组询问的输入如下：

第一行输入两个正整数 n 和 m，代表拼成的图形的行数和列数。

接下来的 n 行，每行输入一个长度为 m 的字符串。

字符串仅由 'W'、'A'、'S'、'D' 和 '*' 五种字符组成，其中 '*' 代表空出来的格子，其余的格子的含义如题面所述。

$1 \le t \le 10$

$1 \le n, m \le 100$

**输出描述**

输出 t 行，如果可以完成拼接，则输出 "Yes"，否则输出 "No"。

**示例 1**

> 输入
> 
>> 3
>>
>> 1 3
>>
>> AWD
>>
>> 2 3
>>
>> *S*
>>
>> *W*
>>
>> 2 2
>>
>> AW
>>
>> SD
> 
> 输出
> 
>> Yes
>>
>> No
>>
>> Yes
> 
> 说明
>
>> 第一次询问拼接如下：
>> 
>>
>> 
>> 第二次询问，显然无法拼接（两个组件会冲突）。
>>
>> 第三次询问，可以拼接如下：
>> 
>>

**python**

```python
""" 
模拟
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    t = int(data[0].strip())
    idx = 1
    results = []
    
    # 定义每个组件四个方向的凹凸状态：[上, 右, 下, 左]
    # 1表示凸，0表示凹
    comp = {
        'W': [1, 1, 0, 1],  # 0度
        'D': [1, 1, 1, 0],  # 90度  
        'S': [0, 1, 1, 1],  # 180度
        'A': [1, 0, 1, 1],  # 270度
        '*': [2, 2, 2, 2]   # 空格子，特殊处理
    }
    
    for _ in range(t):
        # 读取n和m
        while idx < len(data) and data[idx].strip() == "":
            idx += 1
        if idx >= len(data):
            break
            
        nm_line = data[idx].strip().split()
        idx += 1
        while len(nm_line) < 2 and idx < len(data):
            nm_line += data[idx].strip().split()
            idx += 1
            
        n = int(nm_line[0])
        m = int(nm_line[1])
        
        # 读取网格
        grid = []
        for i in range(n):
            if idx < len(data):
                grid.append(data[idx].strip())
                idx += 1
        
        valid = True
        
        # 检查水平相邻（左右）
        for i in range(n):
            for j in range(m-1):
                left_char = grid[i][j]
                right_char = grid[i][j+1]
                
                if left_char == '*' or right_char == '*':
                    continue
                
                # 左边的右边边 与 右边的左边边
                left_right = comp[left_char][1]  # 右边
                right_left = comp[right_char][3] # 左边
                
                # 凹凸必须相反才能契合：1和0可以，0和1可以，但1和1不行，0和0不行
                if left_right == right_left:
                    valid = False
                    break
            
            if not valid:
                break
        
        # 检查垂直相邻（上下）
        if valid:
            for i in range(n-1):
                for j in range(m):
                    top_char = grid[i][j]
                    bottom_char = grid[i+1][j]
                    
                    if top_char == '*' or bottom_char == '*':
                        continue
                    
                    # 上边的下边 与 下边的上边
                    top_bottom = comp[top_char][2]  # 下边
                    bottom_top = comp[bottom_char][0] # 上边
                    
                    if top_bottom == bottom_top:
                        valid = False
                        break
                
                if not valid:
                    break
        
        results.append("Yes" if valid else "No")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

### 1.11 小红的奇偶抽取（答案修复） *

**描述**

小红拿到了一个正整数，她希望把数位中的奇数和偶数分别抽取出来然后做差，请你求出这个差的绝对值。

例如，302938 的奇数抽取出来是 393，偶数抽取出来是 28，最终的差的绝对值是 365。

**输入描述**

一个整数 n。

$1 \le n \le 10^{14}$

**输出描述**

一个整数，代表最终差的绝对值。

**示例 1**

> 输入
>
>> 302938
>
> 输出
>> 365

**示例 2**

> 输入
>
>> 124634
>
> 输出
>> 2451

**python**

```python
def main():
    n_str = input().strip()
    odd_digits = []
    even_digits = []
    for char in n_str:
        digit = int(char)
        if digit % 2 == 1:
            odd_digits.append(char)
        else:
            even_digits.append(char)
    odd_num = int(''.join(odd_digits)) if odd_digits else 0
    even_num = int(''.join(even_digits)) if even_digits else 0
    result = abs(odd_num - even_num)
    print(result)

if __name__ == "__main__":
    main()
```

### 1.12 游游的整数切割 *

**描述**

游游拿到了一个正整数，她希望将它切割成两部分，使得它们的和为偶数。游游想知道有多少种合法的切割方案？

注：切割后的正整数允许出现前导零。

**输入描述**

一个正整数，大小不超过 $10^{100000}$

**输出描述**

一个整数，代表切割的方案数。

**示例 1**

> 输入
> 
>> 103
>
> 输出
> 
>> 1
> 
> 说明
> 
>> 切割成 1+03=4 是合法的，但 10+3=13 为奇数，不符合要求。所以有 1 种合法方案。

**python**

```python
s = input().strip()
n = len(s)
if n == 1:
    print(0)
else:
    last_char = s[-1]
    count = 0
    for i in range(1, n):
        left_last = s[i-1]
        if (int(left_last) % 2) == (int(last_char) % 2):
            count += 1
    print(count)
```

### 1.13 小红的数位操作 *

**描述**

小红拿到了一个正整数 n，她可以进行若干次操作，每次操作将选择一个数位，使其加 1 或者减 1。不过有两条限制：
1. 每个数位最多只能操作一次。
2. 如果选择的是 9，则无法进行加 1 操作。如果选择的是 0，则无法进行减 1 操作。

小红希望最终 n 成为 p 的倍数，你能帮小红输出操作结束后的整数 n 吗？

**输入描述**

两个正整数 n 和 p。

$1 \le n, p \le 10^{13}$

**输出描述**

如果无解，请输出 -1。

否则输出一个整数（如果操作后包含了前导零，请将前导零一起输出），代表操作结束后的整数。有多解时输出任意即可。

**示例 1**

> 输入
> 
>> 72 7
> 
> 输出
>
>> 63

**示例 2**

> 输入
> 
>> 101 123456789
> 
>> 输出
>
>> 000

**示例 3**

> 输入
> 
>> 40 9
> 
> 输出
> 
>> -1

**python**

```python
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n_str = data[0]
    p = int(data[1])
    
    # 特殊情况：p=1，任何数都是1的倍数
    if p == 1:
        print(n_str)
        return
    
    n = int(n_str)
    len_s = len(n_str)
    
    # 检查原始数字是否是p的倍数
    if n % p == 0:
        print(n_str)
        return
    
    # 预计算权重：weights[i] = 10^(len_s-1-i) mod p
    weights = [0] * len_s
    for i in range(len_s):
        exp = len_s - 1 - i
        weights[i] = pow(10, exp, p)
    
    orig_mod = n % p
    current = list(n_str)
    found = [False]  # 使用列表以便在递归中修改
    
    # DFS with backtracking
    def dfs(i, current_mod):
        if found[0]:
            return
        
        if i == len_s:
            if current_mod % p == 0:
                print(''.join(current))
                found[0] = True
            return
        
        original_digit = int(current[i])
        original_char = current[i]
        
        # Option 1: No operation
        dfs(i+1, current_mod)
        if found[0]:
            return
        
        # Option 2: Add 1
        if original_digit != 9:
            new_digit = original_digit + 1
            delta = (new_digit - original_digit) * weights[i]
            new_mod = (current_mod + delta) % p
            current[i] = str(new_digit)
            dfs(i+1, new_mod)
            current[i] = original_char
            if found[0]:
                return
        
        # Option 3: Subtract 1
        if original_digit != 0:
            new_digit = original_digit - 1
            delta = (new_digit - original_digit) * weights[i]
            new_mod = (current_mod + delta) % p
            current[i] = str(new_digit)
            dfs(i+1, new_mod)
            current[i] = original_char
            if found[0]:
                return
    
    dfs(0, orig_mod)
    if not found[0]:
        print(-1)

if __name__ == "__main__":
    main()
```

### 1.14 小美走公路 *

**描述**

有一个环形的公路，上面共有 n 站，现在给出了顺时针第 i 站到第 i + 1 站之间的距离（特殊的，也给出了第 n 站到第 1 站的距离）。小美想沿着公路第 x 站走到第 y 站，她想知道最短的距离是多少？

**输入描述**

第一行输入一个正整数 n，代表站的数量。

第二行输入 n 个正整数 $a_i$，前 n - 1 个数代表顺时针沿着公路走，i 站到第 i + 1 站之间的距离；最后一个正整数代表顺时针沿着公路走，第 n 站到第 1 站的距离。

第三行输入两个正整数 x 和 y，代表小美的出发地和目的地。

**示例 1**

> 输入
> 
>> 3
>>
>> 1 2 2
>>
>> 2 3
>
> 输出
> 
>> 2

**示例 2**

> 输入
> 
>> 3
>>
>> 1 2 2
>>
>> 1 3
> 
> 输出 
>
>> 2

**python**

```python
N = int(input())

dis = [int(x) for x in input().split()]

location = [int(y) for y in input().split()]

distance_1 = 0
distance_2 = 0

for i in range(min(location)-1,max(location)-1):
    distance_1 +=  dis[i]
    dis[i] = 0
distance_2 = sum(dis)

print(min(distance_1,distance_2))
```

### 1.15 小美的排列询问 *

**描述**

小美拿到了一个排列。她想知道在这个排列中，x 和 y 是否是相邻的。你能帮帮她吗？

排列是指一个长度为 n 的数组，其中 1 到 n 每个元素恰好出现一次。

**输入描述**

第一行输入一个正整数 n，代表排列的长度。  

第二行输入 n 个正整数 $a_i$，代表排列的元素。  

第三行输入两个正整数 x 和 y，用空格隔开。

$1 \le n \le 200000$  

$1 \le a_i, x, y \le n$  

保证 $x \ne y$

**输出描述**

如果 x 和 y 在排列中相邻，则输出 "Yes",否则输出 "No"。

**示例 1**

> 输入 
>
>> 4
>>
>> 1 4 2 3
>>
>> 2 4 
>
> 输出
> 
>> Yes

**示例 2**

> 输入
> 
>> 5
>>
>> 3 4 5 1 2
>> 
>> 3 2
>
> 输出
> 
>> No

**python**

 ```python
def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    x, y = map(int, input().split())
    
    pos = [0] * (n + 1)
    for idx, num in enumerate(arr):
        pos[num] = idx
        
    idx_x = pos[x]
    idx_y = pos[y]
    
    if abs(idx_x - idx_y) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
```

### 1.16 函数 *

**描述**

对于一个十进制正整数 x，如果 x 的每一位数字只可能是 1, 2, 3 中的其中一个，则称 x 是完美数。如：123, 1, 3321 都是完美数而 5, 1234 则不是。

牛牛想写一个函数 f(n)，使得其返回最大的不大于 n 的完美数，请你帮助牛牛实现这个函数。

**输入描述**

第一行一个正整数 T 表示单组测试数据的组数。

接下来 T 行每行一个正整数 n。  

$(1 \le T \le 10^5, 1 \le n \le 10^{18})$

**输出描述**

对于每组输入的 n，输出 f(n) 的值。

**示例 1**

> 输入
> 
>> 4  
>>
>> 213  
>>
>> 3244  
>>
>> 22  
>>
>> 100  
> 
> 输出
> 
>> 213
>>
>> 3233  
>>
>> 22  
>>
>> 33  
> 
> 说明
> 
>> 如题所述：f(213) = 213, f(3244) = 3233, f(22) = 22, f(100) = 33。

**python**

```python
def find_largest_perfect(s):
    path = []
    flag = False
    n_len = len(s)
    for i in range(n_len):
        d = int(s[i])
        if flag:
            path.append('3')
            continue
        found = False
        for c in [3, 2, 1]:
            if c <= d:
                path.append(str(c))
                if c < d:
                    flag = True
                found = True
                break
        if not found:
            j = len(path) - 1
            while j >= 0:
                current_digit = int(path[j])
                if current_digit > 1:
                    new_digit = current_digit - 1
                    path[j] = str(new_digit)
                    rest_length = n_len - (j + 1)
                    rest = '3' * rest_length
                    return ''.join(path[:j + 1]) + rest
                j -= 1
            return '3' * (n_len - 1)
    return ''.join(path)

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n_str = data[i]
        res = find_largest_perfect(n_str)
        results.append(res)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### 1.17 子序列 *

**描述**

在数学中，某个序列的子序列是从最初序列通过去除某些元素但不破坏余下元素的相对位置而形成的新序列，如对于字符串 "abc"，"ab" 和 "ac" 都是其子序列，而 "cb" 和 "ca" 不是。

牛牛有一个长度为 n 的仅由小写字母组成的字符串 s，牛牛想知道 s 有多少子序列恰好包含 k 种字母？

**输入描述**

第一行输入两个正整数 n 和 k。

第二行输入一个长度为 n 的仅包含小写字母的字符串 s。

$(1 \le n \le 10^5, 1 \le k \le 26)$

**输出描述**

由于答案可能会很大，因此你只需要输出子序列个数对 $10^9 + 7$ 取模的结果即可。

**示例 1**

> 输入 
>
>> 6 5
>>
>> eecbad 
>
> 输出
>
>> 3
> 
> 说明
> 
>> 显然 s 有两个子序列 "ecbad" 满足要求，同时 s 自己也满足要求，因此答案为 3。

**示例 2**

>> 输入
> 
>> 10 2
>>
>> aaaccebecd
> 
> 输出
>
>> 126

**python**

```python
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    s = data[1].strip()
    
    # 统计每种字母的出现次数
    from collections import Counter
    freq = Counter(s)
    counts = list(freq.values())
    m = len(counts)  # 实际出现的不同字母种类数
    
    if m < k:
        print(0)
        return
    
    MOD = 10**9 + 7
    
    # dp[i][j] 表示从前i种字母中选择恰好j种字母的方案数
    # 优化为一维数组
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for cnt in counts:
        # 对于当前字母，有 (2^cnt - 1) 种非空选择方式
        ways = (pow(2, cnt, MOD) - 1) % MOD
        
        # 从后往前更新，避免重复使用
        for j in range(min(k, len([x for x in counts if x > 0])), 0, -1):
            if j <= k:
                dp[j] = (dp[j] + dp[j-1] * ways) % MOD
    
    print(dp[k] % MOD)

if __name__ == "__main__":
    main()
```

### 1.18 散落的金币（部分通过）

**描述**

零零碎碎的金币规律的洒在了长度为 N 米的道路上，且每间隔一米就会有一堆金币。道路的始端编号为 1,末端编号为 N。现在牛牛起初在编号为 K 处，开始在这条路上收集金币。最后也要回到编号 K 处。但是固执的牛牛这能进行一下操作：
- 每次在一个点只拿一枚金币，初始时可以不拿金币。
- 留在当前位置或者移动到相邻位置取金币（即移动时每次只能移动一米），但是他不会移动到没有金币的地方更不会在没有金币的地方停留（如果该处没有金币了，他就无法往这个点的方向行进了。即不能跳过该点继续行进）。

请你编写一个程序，帮助牛牛计算一下，牛牛最多可以获得多少金币

**输入描述**

第一行给出两个正整数 N 和 K。

第二行给出 N 个正整数 $A_i$,表示编号为 i 处的地方有 $A_i$枚金币。用空格间隔。

$1 \leq N \leq 100000$

$1 \leq K \leq N$

$0 \leq A_i \leq 10^9$

**输出描述**

输出牛牛最多可以获得枚金币

**示例 1**

> 输入
> 
>> 4 1
> 
>> 3 2 2 1
>
> 输出
> 
>> 8
> 
> 说明
> 
>> 牛牛的路径可以为 $1 \to 2 \to 3 \to 4 \to 3 \to 2 \to 1 \to 1 \to 1$

**示例 2**

> 输入
> 
>> 5 3
>> 
>> 2 1 0 1 2
> 
> 输出
> 
>> 0
> 
> 说明
> 
>> 如果牛牛从点 3 移动到相邻的另一个点，牛牛最终不会回到点 3(因为点 3 没有金币)，所以牛牛不能移动。

**示例 3**

> 输入
> 
>> 5 3
>> 
>> 3 1 3 1 3
>
> 输出
> 
>> 5
> 
> 说明
> 
>> $3 \to 2 \to 3 \to 4 \to 3 \to 3$

**python**

```python
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    if a[k-1] == 0:
        print(0)
        return
        
    total = a[k-1]
    
    i = k - 2
    while i >= 0 and a[i] > 0:
        total += a[i]
        if a[i] == 1:
            break
        i -= 1
        
    i = k
    while i < n and a[i] > 0:
        total += a[i]
        if a[i] == 1:
            break
        i += 1
        
    print(total)

if __name__ == "__main__":
    main()
```

### 1.19 相遇 *

**描述**

街道可以看作一维数轴，街边共有 n 个行人，第 i 个人在一维道路上的初始位置为 $x_i$，并有一个初始朝向 $a_i$：
- 若 $a_i = 0$，则代表第 i 个人向左行走；
- 若 $a_i = 1$，则代表第 i 个人向右行走。

保证所有行人的行走速度相同，且不存在两个人的初始位置重合。

在经过足够长的时间后，若在某一时刻两个人的位置重合，则称他们发生了一次相遇。

请计算总共有多少对行人会相遇。

**输入描述**

第一行输入一个整数 $n (1 \le n \le 10^5)$，表示行人数目。

此后 n 行，第 i 行输入两个整数 $x_i, a_i (0 \le x_i \le 10^9; 0 \le a_i \le 1)$，分别表示第 i 个人的初始位置和行走朝向。

除此之外，保证 $x_i$ 互不相同。

**输出描述**

输出一个整数，表示会发生相遇的行人对数。

**示例 1**

> 输入 
>
>> 3
>>
>> 1 1
>>
>> 2 0
>>
>> 3 1
> 
> 输出
> 
>> 1 
>
> 说明
> 
>> 在这个样例中，有且只有第一个人和第二个人会相遇。

**示例 2**

>> 输入
> 
>> 5
>>
>> 23 1
>>
>> 3 1
>>
>> 1 0
>>
>> 45 0
>>
>> 66 1
> 
> 输出
> 
>> 2

**python**

```python
""" 
O(n log n)
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    people = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        a = int(data[idx + 1])
        idx += 2
        people.append((x, a))
    
    # 按位置升序排序
    people.sort(key=lambda p: p[0])
    
    right_count = 0
    total_meet = 0
    
    for x, a in people:
        if a == 1:
            # 向右走，记录
            right_count += 1
        else:
            # 向左走，会与前面所有向右的人相遇
            total_meet += right_count
    
    print(total_meet)

if __name__ == "__main__":
    main()
```

### 1.20 小红的 red 字符串

**描述**

小红拿到了一个只包含 'r'、'e'、'd' 三种字母的字符串。她想知道，有多少子串满足 'r'、'e'、'd' 三种字母的数量严格相等？

**输入描述**

一个仅包含'r'、'e'、'd'三种字符的字符串。长度不超过200000。

**输出描述**

三种字母的数量相等的子串个数。

**示例 1**

> 输入
> 
>> redrde
> 
> 输出
> 
>> 4
> 
> 说明
> 
>> 共有以下四个合法子串：
>> 
>> [red] rde
>> 
>> r [edr] de
>> 
>> red [rde]
>> 
>> [redrde]

**python**

```python
""" 
差分前缀 + 哈希映射
"""
def main():
    s = input().strip()
    n = len(s)
    count_r = 0
    count_e = 0
    count_d = 0
    dic = {}
    dic[(0, 0)] = 1
    
    for char in s:
        if char == 'r':
            count_r += 1
        elif char == 'e':
            count_e += 1
        elif char == 'd':
            count_d += 1
        
        A = count_r - count_e
        B = count_r - count_d
        
        key = (A, B)
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
            
    total = 0
    for count in dic.values():
        total += count * (count - 1) // 2
        
    print(total)

if __name__ == "__main__":
    main()
```

### 1.21 小红的与运算

**描述**

小红拿到了一个数组，她想在其中选择 k 个数，使得这 k 个数的按位与运算的值尽可能大。你能帮帮她吗？

**输入描述**

第一行输入两个正整数 n 和 k，用空格隔开。  

第二行输入 n 个正整数 $a_i$，代表小红拿到的数组。  

$1 \le k \le n \le 100000$  

$1 \le a_i \le 10^9$

**输出描述**

选 k 个数按位与运算的最大值

**示例 1**

> 输入
> 
>> 5 2  
>>
>> 2 3 4 6 5
> 
> 输出
> 
>> 4
> 
> 说明
> 
>> 选择5和6，位与运算为4。

**python**

```python
""" 
贪心 + 位运算
"""
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    ans = 0
    for i in range(30, -1, -1):
        candidate = ans | (1 << i)
        count = 0
        for num in arr:
            if (num & candidate) == candidate:
                count += 1
        if count >= k:
            ans = candidate
            
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.22 小红的 v 三元组

**描述**

小红拿到了一个数组 $a_1, a_2 \cdots a_n $，她想知道有多少组 (i, j, k) 为 “v 三元组”：

第一个数和第三个数相等。且第一个数大于第二个数。

用数学语言描述：

$1 \le i < j < k \le n$

$a_i = a_k$ 且 $a_i > a_j$

**输入描述**

第一行输入一个正整数 n，代表数组的元素个数。

第二行输入 n 个正整数 $a_i$，代表小红拿到的数组。

$3 \le n \le 100000$

$0 \le a_i \le 10^9$

**输出描述**

v 三元组的数量。

**示例 1**

> 输入
> 
>> 6
>> 
>> 3 1 3 4 3 4
> 
> 输出
> 
>> 3
> 
> 说明
> 
>> (1,2,3)
>> 
>> (1,2,5)
>> 
>> (4,5,6)

**python**

```python
import sys

class Fenw:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def update(self, index, delta):
        i = index
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
            
    def query(self, index):
        res = 0
        i = index
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    pos_dict = {}
    for idx, val in enumerate(a):
        if val not in pos_dict:
            pos_dict[val] = []
        pos_dict[val].append(idx)
    
    values = sorted(pos_dict.keys())
    
    fenw = Fenw(n)
    ans = 0
    for x in values:
        P = pos_dict[x]
        P.sort()
        m = len(P)
        part1 = 0
        part2 = 0
        for k in range(1, m):
            pos_k = P[k]
            if pos_k - 1 < 0:
                S_val = 0
            else:
                S_val = fenw.query(pos_k)
            part1 += k * S_val
        for i in range(0, m - 1):
            pos_i = P[i]
            S_val_i = fenw.query(pos_i + 1)
            part2 += (m - i - 1) * S_val_i
        ans += part1 - part2
        for p in P:
            fenw.update(p + 1, 1)
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.23 Monica 的数树（缺少图片）

**描述**

Monica 拿到了一棵有根树，根节点为 1 号节点。每个节点被染成红色或者蓝色。

假设第 i 个节点的权值 $a_i$ 定义为：从根节点到该节点的路径上，红色节点和蓝色节点的数量之差（红色节点数减去蓝色节点数后取绝对值）。请你帮 Monica 计算出所有节点的权值之和。

**输入描述**

第一行输入一个正整数 n，代表节点的数量。

第二行输入一个长度为 n 的字符串，字符 'R' 代表第 i 个节点被染成红色，字符 'B' 代表第 i 个节点被染成蓝色。

接下来的 n - 1 行，每行输入两个正整数 u 和 v，代表节点 u 和节点 v 有一条路径连接。

$1 \le n \le 10^5$

**输出描述**

所有节点的权值之和。

**示例 1**

> 输入
>
>> 5
>> 
>> RBRBB
>> 
>> 2 5
>> 
>> 1 5
>> 
>> 4 1
>> 
>> 3 5
> 
> 输出
> 
>> 3
>
> 说明
>
>> 这棵树的结构如上图。
>> 
>> 根节点到1号节点的路径只有一个红色节点（因为 1 号节点本身即为根节点），红色节点和蓝色节点的数量差是 1。所以 1 号节点的权值为 1。
>> 
>> 根节点到 2 号节点的路径有 1 个红色节点，2 个蓝色节点，红色节点和蓝色节点的数量差是 1。所以 2 号节点的权值为 1。
>> 
>> 根节点到3号节点的路径有 2 个红色节点，1 个蓝色节点，红色节点和蓝色节点的数量差是1。所以 3 号节点的权值为 1。
>> 
>> 4 号节点和 5 号节点的权值为 0，因为根节点到这两个节点的路径上，红蓝点的数量相等。
>> 
>> 所有点权值和为 3。

**python**

```python
import collections
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    graph = [[] for _ in range(n+1)]
    index = 2
    for _ in range(n-1):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        
    colors = [0] * (n+1)
    for i in range(1, n+1):
        colors[i] = s[i-1]
        
    diff = [0] * (n+1)
    if colors[1] == 'R':
        diff[1] = 1
    else:
        diff[1] = -1
        
    visited = [False] * (n+1)
    queue = collections.deque()
    queue.append(1)
    visited[1] = True
    total = 0
    while queue:
        u = queue.popleft()
        total += abs(diff[u])
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if colors[v] == 'R':
                    diff[v] = diff[u] + 1
                else:
                    diff[v] = diff[u] - 1
                queue.append(v)
                
    print(total)

if __name__ == "__main__":
    main()
```

### 1.24 小欧的括号操作

**python**

```python
""" 
栈
"""
s = input()
stack = []
for c in s:
    flag = False
    while len(stack) != 0 and c == ')' and stack[-1] == '(':
        stack.pop()
        flag = True
    if flag: stack.append('(')
    else:stack.append(c)
print(len(stack))
```

### 1.25 小欧的选数乘积

**描述**

小欧拿到了两个正整数 x 和 y，她想进行一些操作，使得 x 不小于 y。每一轮操作：从给定的整数数组 a 中选定一个元素 $a_i$，将 x 乘以 $a_i$，并删掉 a 数组中所有的等于 $a_i$ 的数字。

小欧想知道，自己最少进行多少轮操作，才可以使得 x 不小于 y？

**输入描述**

第一行输入两个正整数 x 和 y，用空格隔开。

第二行输入一个正整数 n，代表数组大小。

第三行输入 n 个正整数 $a_i$，代表数组的元素。

$1 \le x, y, a_i \le 10^9$

$1 \le n \le 10^5$

**输出描述**

如果小欧无法在有限的操作下使得 x 不小于 y，则输出 -1。

否则输出一个整数，代表小欧的操作次数。

**示例 1**

> 输入
> 
>> 3 40
>> 
>> 4
>> 
>> 2 3 4 4
> 
> 输出
> 
>> 3
> 
> 说明
> 
>> 第一次操作，小欧选择数字 3，x 变成 9，此时数组为 [2, 4, 4]
>> 
>> 第二次操作，小欧选择数字 4，x 变成 36，此时数组为 [2]
>> 
>> 第三次操作，小欧选择数字 2，x 变成 72，此时数组为空。三次操作后 x 不小于 y
>> 
>> 操作的方式不是唯一的，但可以证明操作的最小次数为 3。

**示例 2**

> 输入
> 
>> 2 5
>> 
>> 5
>> 
>> 2 2 2 2 2
> 
> 输出
> 
>> -1
> 
> 说明
>
>> 当小欧选择 2 后，x 变成 4，但此时数组为空。因此无法继续操作，x 永远不可能不小于 $y$。

**示例 3**

> 输入
> 
>> 5 5
>> 
>> 5
>> 
>> 2 2 2 2 2
> 
> 输出
> 
>> 0
> 
> 说明
>
>> 小欧不需要任何操作。

**python**

```python
def main():
    import sys
    data = sys.stdin.read().split()
    x = int(data[0])
    y = int(data[1])
    n = int(data[2])
    a = list(map(int, data[3:3+n]))
    
    if x >= y:
        print(0)
        return
        
    unique_a = sorted(set(a), reverse=True)
    
    cur = x
    count = 0
    for num in unique_a:
        cur *= num
        count += 1
        if cur >= y:
            print(count)
            return
            
    print(-1)

if __name__ == "__main__":
    main()
```

### 1.26 小红的子树操作

**描述**

小红拿到了一棵有根树，i 号节点的权值为 $a_i$。已知 1 号节点为根节点。

小红有 q 次操作，每次操作会选择一个节点 x，使得 x 为根的子树上，所有节点的权值乘以 y。

小红想知道，在 q 次操作结束以后，对于$i \in [1, n]$，以节点 i 为根的子树的所有点权值乘积末尾有多少个 0？

**输入描述**

第一行输入一个正整数 n，代表节点的数量。

第二行输入 n 个正整数 $a_i$，代表每个节点的权值。

接下来的 n - 1 行，每行输入两个正整数 u 和 v，代表节点 u 和节点 v 有一条边相连。

接下来的一行输入一个正整数 q，代表操作次数。

接下来的 q 行，每行输入两个正整数 x 和 y，代表小红的一次操作。

$1 \le n, q \le 10^5$

$1 \le a_i, y \le 10^9$

$1 \le x, u, v \le n$

**输出描述**

输出一行 n 个正整数，分别代表 1 号节点到 n 号节点，每个节点的子树权值乘积尾零的数量。

**示例1**

> 输入
> 
>> 5
>>
>> 1 2 6 3 1
>>
>> 1 2
>>
>> 1 3
>>
>> 2 4
>>
>> 2 5
>>
>> 1
>>
>> 2 5
> 
> 输出
> 
>> 2 1 0 0 0
> 
> 说明
>
>> 操作后 2 号、4 号、5 号节点都乘以 5，每个节点的权值分别是 [1, 10, 6, 15, 5]
>> 
>> 1 号节点为根的子树乘积是 4500，末尾有 2 个 0。
>> 
>> 2 号节点为根的子树乘积是 750，末尾有 1 个 0。
>> 
>> 3 号节点为根的子树乘积是 6，末尾有 0 个 0。
>> 
>> 4 号节点为根的子树乘积是 15，末尾有 0 个 0。
>> 
>> 5 号节点为根的子树乘积是 5，末尾有 0 个 0。

**python**

```python
""" 
树
"""
import sys
from collections import deque

def count_factor(num, base):
    cnt = 0
    while num % base == 0:
        cnt += 1
        num //= base
    return cnt

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)
        
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
                
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)
    rev = [0] * (n + 1)
    stack = [1]
    time = 1
    next_index = [0] * (n + 1)
    while stack:
        u = stack[-1]
        if in_time[u] == 0:
            in_time[u] = time
            rev[time] = u
            time += 1
        if next_index[u] < len(children[u]):
            v = children[u][next_index[u]]
            next_index[u] += 1
            stack.append(v)
        else:
            stack.pop()
            out_time[u] = time - 1
            
    init2 = [0] * (n + 1)
    init5 = [0] * (n + 1)
    for i in range(1, n + 1):
        init2[i] = count_factor(a[i], 2)
        init5[i] = count_factor(a[i], 5)
        
    q = int(next(it))
    diff2 = [0] * (n + 2)
    diff5 = [0] * (n + 2)
    
    for _ in range(q):
        x = int(next(it))
        y = int(next(it))
        c2 = count_factor(y, 2)
        c5 = count_factor(y, 5)
        diff2[in_time[x]] += c2
        if out_time[x] + 1 <= n:
            diff2[out_time[x] + 1] -= c2
        diff5[in_time[x]] += c5
        if out_time[x] + 1 <= n:
            diff5[out_time[x] + 1] -= c5
            
    op2 = [0] * (n + 1)
    op5 = [0] * (n + 1)
    for i in range(1, n + 1):
        op2[i] = op2[i - 1] + diff2[i]
        op5[i] = op5[i - 1] + diff5[i]
        
    f2 = [0] * (n + 1)
    f5 = [0] * (n + 1)
    for i in range(1, n + 1):
        node = rev[i]
        f2[node] = init2[node] + op2[i]
        f5[node] = init5[node] + op5[i]
        
    sub2 = [0] * (n + 1)
    sub5 = [0] * (n + 1)
    for i in range(n, 0, -1):
        u = rev[i]
        sub2[u] = f2[u]
        sub5[u] = f5[u]
        for v in children[u]:
            sub2[u] += sub2[v]
            sub5[u] += sub5[v]
            
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = min(sub2[i], sub5[i])
        
    res = []
    for i in range(1, n + 1):
        res.append(str(ans[i]))
    print(" ".join(res))

if __name__ == "__main__":
    main()
```

### 1.27 小红的好 red 串（一）

**描述**

小红定义一个字符串为“好串”，当且仅当相邻两个字母不相同。

小红拿到了一个仅由 'r'、'e'、'd' 三种字符组成的字符串，她有一个魔法：将相邻的两个字母同时删除，并在其位置生成任意一个字母（'r'、'e'、'd' 三种中的一种）。例如，对于字符串 "dedd"，小红可以选择中间两个相邻字母 "ed"，将其变成 "r"，此时字符串变为 "drd"。小红希望将给定的字符串变成“好串”，她想知道自已最少需要多少次操作？

**输入描述**

一个长度不超过 200000 且仅由 'r'、'e'、'd' 三种字符组成的字符串。

**输出描述**

一个整数，代表操作的最小次数。

**示例 1**

> 输入
> 
>> rede
> 
> 输出
> 
>> 0
> 
> 说明
>
>> 本身即为好串，不需要任何操作。 

**示例 2** 

> 输入
> 
>> rrdd
> 
> 输出
> 
>> 1
> 
> 说明
>
>> 选择 "rd" 变成 "e" 即可。 

**示例 3**

> 输入
> 
>> rreedd
> 
> 输出
>
>> 2

**python**

```python
""" 
贪心
"""
def main():
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        return
        
    i = 0
    count = 0
    last = None
    while i < n:
        if last is None:
            count += 1
            last = s[i]
            i += 1
        else:
            if s[i] != last:
                count += 1
                last = s[i]
                i += 1
            else:
                if i + 1 < n:
                    count += 1
                    candidates = {'r', 'e', 'd'}
                    candidates.discard(last)
                    if i + 2 < n:
                        candidates.discard(s[i + 2])
                    c = candidates.pop()
                    last = c
                    i += 2
                else:
                    i += 1
    print(n - count)

if __name__ == "__main__":
    main()
```

### 1.28 进制转换

**描述**

dd 得到了一个数，但不确定这个数的进制，只知道可能是 2~16 进制的其中之一，所以她想你帮她算出所有可能的结果，并转成十进制后对 $10^9 + 7$ 进行取模，把所得到的答案从小到大排列，若存在相同的结果，只保留一个即可。

**输入描述**

一个数，表示得到的数字

保证不会出现 '0'~'9'，'A'~'F' 以外的字符，输入数字长度不超过 100000，且保证无前导零

**输出描述**

每行一个数，表示可能的结果

**示例 1**

> 输入
> 
>> 11
> 
> 输出
>
>> 3
>>
>> 4
>>
>> 5
>>
>> 6
>>
>> 7
>>
>> 8
>>
>> 9
>>
>> 10
>>
>> 11
>>
>> 12
>>
>> 13
>>
>> 14
>>
>> 15
>>
>> 16
>>
>> 17
> 
> 说明
>
>> 2 到 16 进制都有可能是答案。

**示例 2**

> 输入
> 
>> FF
> 
> 输出
> 
>> 255
> 
> 说明
>
>> 只有 16 进制可能是答案。

**python**

```python
""" 
字符串
"""
MOD = 10**9 + 7

def char_to_digit(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return 10 + ord(c) - ord('A')

def main():
    s = input().strip()
    result_set = set()
    
    for k in range(2, 17):
        valid = True
        num = 0
        for c in s:
            d = char_to_digit(c)
            if d >= k:
                valid = False
                break
            num = (num * k + d) % MOD
        if valid:
            result_set.add(num)
            
    sorted_results = sorted(result_set)
    for res in sorted_results:
        print(res)

if __name__ == "__main__":
    main()
```

### 1.29 小球投盒

**描述**

小红一共有 n 个盒子，标号为 1 到 n，小红向盒子里放入小球 m 次，每次进行以下两个操作中的一个：
1. 向编号为 x 的盒子里放入一个小球；
2. 向除了编号为 x 的其他 n - 1 盒子放入一个小球。

小红想知道，第几次操作之后，所有盒子里至少都有一个小球，如果一直无法达到这个目标，输出 -1。

**输入描述**

第一行两个整数 n 和 m，表示盒子的数量和操作的次数。

接下来 m 行，每行两个整数 $t_i$ 和 $x_i$，表示第 i 次操作的类型和 x 的值。

$ 1 \le n, m \le 10^5 $

$ 1 \le t_i \le 2 $

$ 1 \le x_i \le n $

**输出描述**

输出一个整数，表示第几次操作之后，所有盒子里至少都有一个小球，如果一直无法达到这个目标，输出 -1。

**示例 1**

> 输入
> 
>> 3 3
>> 
>> 1 1
>> 
>> 1 2
>> 
>> 1 3
> 
> 输出
> 
>> 3
> 
> 说明
>
>> 三次操作之后，所有盒子里都至少有一个小球。

**示例 2**

> 输入
> 
>> 3 4
>> 
>> 1 1
>> 
>> 2 2
>> 
>> 1 3
>> 
>> 1 2
> 
> 输出
> 
>> 4
> 
> 说明
> 
>> 第一次操作后，盒子 1 里有小球。
>> 
>> 第二次操作后，盒子 1、3 里有小球。
>> 
>> 第三次操作后，盒子 1、3 里有小球。
>> 
>> 第四次操作后，每个盒子里都有小球。

**python**

```python
""" 
模拟
"""
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    m = int(data[1])
    operations = []
    index = 2
    for i in range(m):
        t = int(data[index])
        x = int(data[index + 1])
        index += 2
        operations.append((t, x))
        
    INF = 10**9 + 10
    op1_first = [INF] * (n + 1)
    op2_first_time = INF
    op2_first_x = -1
    op2_second_time = INF
    
    for idx, (t, x) in enumerate(operations):
        op_index = idx + 1
        if t == 1:
            if op1_first[x] == INF:
                op1_first[x] = op_index
        else:
            if op2_first_time == INF:
                op2_first_time = op_index
                op2_first_x = x
            else:
                if op2_second_time == INF and x != op2_first_x:
                    op2_second_time = op_index
                    
    max_time = 0
    for i in range(1, n + 1):
        op2_cover = INF
        if op2_first_time != INF:
            if i != op2_first_x:
                op2_cover = op2_first_time
            else:
                op2_cover = op2_second_time
        cover_time = min(op1_first[i], op2_cover)
        if cover_time > max_time:
            max_time = cover_time
            
    print(max_time if max_time != INF else -1)

if __name__ == "__main__":
    main()
```

### 1.30 数字变换

**描述**

给出两个数字 a, b, a 每次可以乘上一个大于 1 的正整数得到新的 a, 我们将这个操作叫做一次它乘。现在请你计算, a 是否可以通过若干次它乘变为 b。若 a 可以通过若干次它乘变为 b, 请你计算最多可以经过多少次它乘。若 a 不可能变为 b, 输出 -1 即可。

**输入描述**

在一行中给出两个正整数 a, b

$1 \le a, b \le 10^9$

**输出描述**

在一行中输出自乘操作的次数或者 -1

**示例 1**

> 输入
> 
>> 2 16
> 
> 输出
> 
>> 3
> 
> 说明
> 
>> 2->4->8->16

**示例 2**

> 输入
> 
>> 3 5
> 
> 输出
> 
>> -1
> 
> 说明
>
>> 3 不可能变为 5

**python**

```python
""" 
质因数分解
"""
def main():
    a, b = map(int, input().split())
    if b % a != 0:
        print(-1)
        return
    k = b // a
    if k == 1:
        print(0)
        return
        
    count = 0
    temp = k
    i = 2
    while temp % i == 0:
            count += 1
            temp //= i
        i += 1
    if temp > 1:
        count += 1
        
    print(count)

if __name__ == "__main__":
    main()
```

### 1.31 二叉树（缺少图片）

**描述**

小强现在有 n 个节点,他想请你帮他计算出有多少种不同的二叉树满足节点个数为 n 且树的高度不超过 m 的方案.因为答案很大,所以答案需要模上 1e9+7 后输出。

树的高度: 定义为所有叶子到根路径上节点个数的最大值。

例如: 当 n=3, m=3 时,有如下 5 种方案:

**输入描述**

第一行输入两个正整数 n 和 m。

$1 \le m \le n \le 50$

**输出描述**

输出一个答案表示方案数。

**示例 1**

> 输入
> 
>> 3 3
> 
> 输出
>
>> 5

**示例 2**

> 输入
> 
>> 3 2
> 
> 输出
>
>> 1

**示例 3**

> 输入
> 
>> 4 3
> 
> 输出
>
>> 6

**python**

```python
""" 
动态规划
"""
MOD = 10**9 + 7

def main():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(m + 1):
        dp[0][j] = 1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            total = 0
            for k in range(i):
                total = (total + dp[k][j - 1] * dp[i - 1 - k][j - 1]) % MOD
            dp[i][j] = total
            
    print(dp[n][m])

if __name__ == "__main__":
    main()
```

### 1.32 魔塔

**描述**

最近小强很喜欢玩魔塔，勇者和魔塔的怪物都有三个属性：血量、攻击力和防御力。当勇者遭遇一个怪物时，战斗方式如下：
- 由勇者先手攻击，回合制，轮流对对方造成伤害。
- 伤害值为 max(伤害方的攻击力 - 对方的防御力, 1)。其中 max(a, b) 代表 a 和 b 中较大的数值。
- 当一方的血量降低到 0 以下时，战斗立即结束，另一方胜利。

现在魔塔中的怪物排成了一排，勇者需要按照顺序进行战斗，当勇者成功击败一只怪物后他可以获得奖励：从以下三项中选择一项。
1. 血量增加 1000。
2. 攻击力增加 10。
3. 防御力增加 10。

现在小强想知道，在最优策略下勇者最多能击败多少只怪物。

**输入描述**

第一行四个空格分隔的正整数 H, A, D, n，分别代表勇者的血量，攻击力，防御力，怪物的数量。

接下来 n 行每行三个空格分隔的正整数 $H_i, A_i, D_i$，用来描述第 i 只怪物的血量，攻击力，防御力。

$1 \leq n \leq 200$

$1 \leq H, A, D, H_i, A_i, D_i \leq 10^9$

**输出描述**

仅一行一个整数表示最大击败怪物数。

**示例 1**

> 输入
> 
>> 10 10 10 3
>> 
>> 6 11 9
>> 
>> 2 10000 10
>> 
>> 100 10000 10000
> 
> 输出
> 
>> 2
> 
> 说明
>
>> 击败第一只怪物勇者损耗五血量，接下来最优策略是选择提高 10 点攻击力，这样在对战第二只怪物时一次攻击击败第二只怪物，损耗血量为 0，接下来无论选择什么奖励均无法战胜第三只怪物，所以最多击败怪物数为 2 。

**python**

```python
"""
动态规划
"""
import sys

def simulate(h, a, d, h_m, a_m, d_m):
    damage1 = max(a - d_m, 1)
    damage2 = max(a_m - d, 1)
    rounds_hero = (h_m + damage1 - 1) // damage1
    if rounds_hero == 0:
        return h
    h_remaining = h - (rounds_hero - 1) * damage2
    if h_remaining <= 0:
        return -1
    return h_remaining

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    H = int(data[0])
    A = int(data[1])
    D = int(data[2])
    n = int(data[3])
    monsters = []
    index = 4
    for i in range(n):
        h_m = int(data[index])
        a_m = int(data[index+1])
        d_m = int(data[index+2])
        index += 3
        monsters.append((h_m, a_m, d_m))
        
    dp = [[H]]
    ans = 0
    for i in range(n):
        next_dp = [[-1] * (i+2) for _ in range(i+2)]
        found = False
        for x in range(i+1):
            for y in range(i+1 - x):
                if dp[x][y] == -1:
                    continue
                h0 = dp[x][y]
                a0 = A + y * 10
                d0 = D + (i - x - y) * 10
                h_m, a_m, d_m = monsters[i]
                h_remaining = simulate(h0, a0, d0, h_m, a_m, d_m)
                if h_remaining >= 0:
                    found = True
                    ans = i+1
                    if x+1 <= i+1 and y <= i+1:
                        next_dp[x+1][y] = max(next_dp[x+1][y], h_remaining + 1000)
                    if x <= i+1 and y+1 <= i+1:
                        next_dp[x][y+1] = max(next_dp[x][y+1], h_remaining)
                    if x <= i+1 and y <= i+1:
                        next_dp[x][y] = max(next_dp[x][y], h_remaining)
        if not found:
            break
        dp = next_dp
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.33 树上最短路（缺少图片）

**描述**

牛牛刚刚学了二叉树和最短路

他现在很好奇，对于一棵完全二叉树(对于有孩子的节点 i，其左孩子为 $2 \times i$，右孩子为 $2 \times i + 1$)，给定的两个点之间的最短路的长度是多少

我们认为相邻两点之间的距离为 1

**输入描述**

第一行输入一个整数 T，表示测试数据共有 T 组  
对于每组测试数据，输入两个整数表示所询问的节点的标号

**输出描述**

对于每组数据，输出一个整数表示答案

**补充说明**

对于 30% 的数据，$T \le 100$  
对于 100% 的数据，$1 \le T \le 10^5$，$1 \le$ 节点编号 $\le 10^9$

**示例 1**

> 输入
> 
>> 3  
>>
>> 1 2  
>>
>> 4 14  
>>
>> 8 5
> 
> 输出
>
>> 1
>>  
>> 5
>>  
>> 3
> 
> 说明
>
>> 

**python**

```python
""" 
二叉树
"""
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        steps = 0
        while a != b:
            if a > b:
                a //= 2
            else:
                b //= 2
            steps += 1
        results.append(str(steps))
    print("\n".join(results))

if __name__ == "__main__":
    main()
```

### 1.34 游游的字母串

**描述**

对于一个小写字母而言，游游可以通过一次操作把这个字母变成相邻的字母。'a' 和 'b' 相邻，'b' 和 'c' 相邻，以此类推。特殊的，'a' 和 'z' 也是相邻的。可以认为，小写字母的相邻规则为一个环。

游游拿到了一个仅包含小写字母的字符串，她想知道，使得所有字母都相等至少要多少次操作？

**输入描述**

一个仅包含小写字母，长度不超过 100000 的字符串。

**输出描述**

一个整数，代表最小的操作次数。

**示例 1**

> 输入
> 
>> yab
> 
> 输出
> 
>> 3
> 
> 说明
> 
>> 第一次操作，把 'y' 变成 'z'，字符串变成了 "zab"
>>
>> 第二次操作，把 'b' 变成 'a'，字符串变成了 "zaa"
>>
>> 第三次操作，把 'z' 变成 'a'，字符串变成了 "aaa"

**python**

```python
""" 
字符串
"""
def main():
    s = input().strip()
    n = len(s)
    min_ops = float('inf')
    
    for target in range(ord('a'), ord('z') + 1):
        total_ops = 0
        for char in s:
            diff = abs(ord(char) - target)
            total_ops += min(diff, 26 - diff)
        if total_ops < min_ops:
            min_ops = total_ops
            
    print(min_ops)

if __name__ == "__main__":
    main()
```

### 1.35 游游的三色树

**描述**

游游拿到了一棵树，其中每个节点被染成了红色（r）、绿色（g）或蓝色（b）。

游游想删掉一条边，使得剩下的两个连通块各恰好有三种颜色。  

游游想知道，有多少合法的边可以删除？  

注：树指不含重边和自环的无向连通图。

**输入描述**

第一行输入一个正整数 n，代表树的节点数量。

第二行输入一个长度为 n 的、仅包含 'r'、'g'、'b' 的字符串，第 i 个字符表示节点 i 的颜色。  

接下来的 n - 1 行，每行输入两个正整数 u 和 v，代表点 u  和点 v 有一条无向边连接。  

$6 \leq n \leq 10^5$  

$1 \leq u, v \leq n$

**输出描述**

合法的边的数量。

**示例 1**

> 输入
> 
>> 7  
>>
>> rgbrgbg
>>
>> 1 2
>>
>> 2 3
>>
>> 3 4
>>
>> 4 5
>>
>> 5 6
>>
>> 6 7
>
> 输出
> 
>> 1  
> 
> 说明
> 
>> 如上图，只有删掉 3-4 这条边满足剩下两个连通块都有 3 种颜色。

**python**

```python
""" 
二叉树
"""
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    colors = data[1].strip()
    graph = defaultdict(list)
    idx = 2
    for _ in range(n - 1):
        u = int(data[idx]) - 1  # 转0-indexed
        v = int(data[idx + 1]) - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    # 统计整棵树颜色总数
    total_r = colors.count('r')
    total_g = colors.count('g')
    total_b = colors.count('b')
    
    ans = 0
    sys.setrecursionlimit(200000)
    
    def dfs(u, parent):
        nonlocal ans
        # 当前子树颜色计数
        r = 1 if colors[u] == 'r' else 0
        g = 1 if colors[u] == 'g' else 0
        b = 1 if colors[u] == 'b' else 0
        
        for v in graph[u]:
            if v == parent:
                continue
            sub_r, sub_g, sub_b = dfs(v, u)
            r += sub_r
            g += sub_g
            b += sub_b
            
            # 检查删除边 (u, v) 是否合法
            # 子树: (sub_r, sub_g, sub_b)
            # 其余: (total_r - sub_r, total_g - sub_g, total_b - sub_b)
            if (sub_r > 0 and sub_g > 0 and sub_b > 0 and
                total_r - sub_r > 0 and total_g - sub_g > 0 and total_b - sub_b > 0):
                ans += 1
        
        return (r, g, b)
    
    dfs(0, -1)
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.36 活动安排

**描述**

给定 n 个活动，每个活动安排的时间为 $[a_i, b_i)$。求最多可以选择多少个活动，满足选择的活动时间两两之间没有重合。

**输入描述**

第一行输入一个整数 $n (1 \le n \le 2 \cdot 10^5)$，表示可选活动个数。

接下来的 n 行，每行输入两个整数 $a_i, b_i (0 \le a_i < b_i \le 10^9)$，表示第 i 个活动的时间。

**输出描述**

输出一行一个整数，表示最多可选择的活动数。

**示例 1**

> 输入
>
>> 3
>>
>> 1 4
>>
>> 1 3
>>
>> 3 5
> 
> 输出
>
>> 2

**python**

```python
"""
贪心
"""
def main():
    n = int(input().strip())
    activities = []
    for _ in range(n):
        a, b = map(int, input().split())
        activities.append((a, b))
    
    activities.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    for a, b in activities:
        if a >= last_end:
            count += 1
            last_end = b
    print(count)

if __name__ == "__main__":
    main()
```

### 1.37 牛牛的 Ackmann

**描述**

牛牛最近了解到了著名的阿克曼 (Ackmann) 函数，阿克曼函数是一个增长极其迅速的函数，另外一个著名的数据结构--并查集的最优复杂度便可以达到阿克曼函数的反函数级别。请你计算阿克曼函数的几个整数定义域的结果。

$$
Ackmann(m, n) =
\begin{cases}
n + 1, m = 0 \\
Ackmann(m - 1, 1), (m > 0 \& n = 0) \\
Ackmann(m - 1, Ackmann(m, n - 1)), (m > 0 \& n > 0)
\end{cases}
$$

**输入描述**

第一行输入两个正整数，分别是 n，m。（保证这个定义域是可计算的）

**输出描述**

输出 Ackmann (n, m)

**示例 1**

> 输入
> 
>> 10 0
> 
> 输出
>
>> 11

**python**

```python
""" 
递归 LRU
"""
import sys
sys.setrecursionlimit(10000)

from functools import lru_cache

@lru_cache(maxsize=None)
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    # 注意：输入是 n, m，但函数是 A(m, n)
    result = ackermann(m, n)
    print(result)

if __name__ == "__main__":
    main()
```

### 1.38 跳台阶

**描述**

一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

数据范围：$0 \le n \le 40$

要求：时间复杂度：O(n)，空间复杂度：O(1)

**输入描述**

本题输入仅一行，即一个整数 n

**输出描述**

输出跳上 n 级台阶有多少种跳法

**示例 1**

> 输入
> 
>> 2
> 
> 输出
> 
>> 2
> 
> 说明
>
>> 青蛙要跳上两级台阶有两种跳法，分别是：先跳一级，再跳一级或者直接跳两级。因此答案为 2

**示例 2**

> 输入
> 
>> 7
> 
> 输出
>
>> 21

**python**

```python
""" 
斐波那契数列
"""
n = int(input())

if n == 0 or n == 1:
    print(1)
else:
    prev2 = 1  # f(0)
    prev1 = 1  # f(1)
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    print(prev1)
```

### 1.39 超级圣诞树（缺少图片）

**描述**

今天是圣诞节，牛牛要打印一个漂亮的圣诞树送给想象中的女朋友，请你帮助他实现梦想。

**输入描述**

输入圣诞树的大小 n

$1 \leq n \leq 8$

**输出描述**

输出对应的圣诞树

**示例 1**

> 输入
>
>> 1
>
> 输出
>
>> \*  
>> \* \*  
>> \* \* \*  
>> \*  
>
> 说明
  
**示例 2**

> 输入
>
>> 2
>
> 输出
>
>> \*  
>> \* \*  
>> \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \*  
>> \*  
>
> 说明

**示例 3**

> 输入
>
>> 3
>
> 输出
>
>> \*  
>> \* \*  
>> \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \*  
>> \*  
>> \*  
>> \*  
>
> 说明
  
**示例 4**

> 输入
>
>> 4
>
> 输出
>
>> \*  
>> \* \*  
>> \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \*  
>> \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \*  
>> \* \* \* \*  
>> \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*  
>> \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*  
>> \*  
>> \*  
>> \*  
>> \*  
>
> 说明

**python**

```python
""" 
迭代
"""
n = int(input())

# 初始三角形（3行，5列）
grid = [
    "  *  ",
    " * * ",
    "* * *"
]

if n == 1:
    for line in grid:
        print(line)
    for _ in range(n):
        print("  *  ")
else:
    # 迭代构造分形
    for level in range(2, n + 1):
        height = len(grid)
        width = len(grid[0])
        new_width = width * 2 + 1
        new_grid = []
        
        # 上层：原图形居中
        offset = (new_width - width) // 2
        for line in grid:
            new_grid.append(' ' * offset + line + ' ' * offset)
        
        # 下层：左右各一个原图形
        for line in grid:
            new_grid.append(line + ' ' + line)
        
        grid = new_grid
    
    # 输出树冠
    for line in grid:
        print(line)
    
    # 输出树干：n 行，'*' 居中
    trunk = ' ' * (len(grid[0]) // 2) + '*'
    for _ in range(n):
        print(trunk)
```

### 1.40 小红的数组

**描述**

小红拿到了一个长度为 n 的数组，数组中的元素都是正整数。

小红想让你回答以下三个问题，取两个数乘积大于 k 的方案数、取两个数乘积等于 k 的方案数、取两个数乘积小于 k 的方案数。

注：两个数是不放回且同时取的。例如对于数组 [1, 2, 3, 4, 5] 而言，取 [1, 2] 和 [2, 1] 我们认为是同一种方案。

但是，如果有两个数相等，那么取相等但位置不同的数不认为是同一种取法。例如对于数组 [2, 2, 2, 3] 而言，有三种方案可以取到 [2, 2]。

**输入描述**

第一行输入两个正整数 n 和 k，用空格隔开。

第二行输入 n 个用空格隔开的正整数 $a_i$，用来表示数组。

数据范围：$1 \le n \le 300000, 1 \le a_i \le 10^9, 1 \le k \le 10^{18}$

**输出描述**

输出三个整数，用空格隔开。分别代表取两个数乘积大于 k 的方案数、等于 k 的方案数、小于 k 的方案数。

**示例 1**

> 输入
> 
>> 4 7  
>> 1 3 4 2  
>
> 输出
> 
>> 2 0 4
> 
> 说明
> 
>> 大于 7 的取数方案: [3, 4] 和 [4, 2]。小于 7 的取数方案: [1, 3]、[1, 4]、[1, 2]、[3, 2]

**示例 2**

> 输入
> 
>> 5 9   
>> 3 3 3 3 3  
>
> 输出
> 
>> 0 10 0

**python**

```python
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    total_pairs = n * (n - 1) // 2
    
    # 1. 统计等于 k 的对数
    freq = defaultdict(int)
    for x in a:
        freq[x] += 1
    
    equal = 0
    processed = set()
    for x in freq:
        if x in processed:
            continue
        if k % x == 0:
            y = k // x
            if y in freq:
                if x == y:
                    cnt = freq[x]
                    equal += cnt * (cnt - 1) // 2
                else:
                    equal += freq[x] * freq[y]
                    processed.add(y)
        processed.add(x)
    
    # 2. 统计小于 k 的对数（排序 + 双指针）
    a_sorted = sorted(a)
    less = 0
    j = n - 1
    for i in range(n):
        # 确保 j > i
        if j <= i:
            j = i + 1
        # 从右往左找最大的 j 使得 a[i] * a[j] < k
        while j > i and a_sorted[i] * a_sorted[j] >= k:
            j -= 1
        if j > i:
            less += j - i
        else:
            # 后续 i 更大，不可能有 j > i 满足，可提前终止
            break
    
    # 3. 计算大于 k 的对数
    greater = total_pairs - equal - less
    
    print(greater, equal, less)

if __name__ == "__main__":
    main()
```

### 1.41 添数博弈

**描述**

小 A 和小 B 创造了一个叫添数博弈的游戏，游戏规则如下：

首先在数池中添加两个整数 x, y，接下来，两个人轮流开始添数；添数的规则是在数池中任意选择两个数 x, y，令 m = |x - y|，若 m 不在数池中，则将 m 添加到数池中；若 m 已经在数池中，则游戏结束。

假设小 A 先选数，两人轮流操作添数，若有一方不能无法添数时，则该人就输了。

**输入描述**

输入的第一行给出测试用例的数量 $T (1 \leq T \leq 10)$；

随后 T 行，每行给出两个整数 $x, y (1 \leq x, y \leq 10^9)$

$x \neq y$

**输出描述**

对于每一个测试样例，输出获胜方的名字

**示例 1**

> 输入
> 
>> 2   
>> 4 1  
>> 5 2  
>
> 输出
> 
>> B   
>> A  

**python**

```python
""" 
组合游戏
"""
import math

t = int(input().strip())
results = []
for _ in range(t):
    x, y = map(int, input().split())
    d = math.gcd(x, y)
    M = max(x, y)
    N = M // d
    moves = N - 2
    if moves % 2 == 1:
        results.append("A")
    else:
        results.append("B")

for res in results:
    print(res)
```

### 1.42 吃糖果

**描述**

牛妹喜欢吃糖，现在有一排共 n 个糖果，第 i 个糖果具有一个甜度值 $a_i$。因为吃甜食太多了会得蛀牙，所以牛妹吃的糖果的甜度值总和不能超过 k。她可以以任意的顺序吃糖，请问她最多能吃多少个糖果？

**输入描述**

第一行给出两个正整数 $n, k (1 \leq n \leq 2 * 10^5, 1 \leq k \leq 10^9)$，意义如题面所示  
第二行有 n 个整数，分别代表每一个糖果的甜度 $a (1 \leq a_i \leq 10^9)$

**输出描述**

输出一行一个整数代表牛妹最多可以吃掉的糖果数。

**示例 1**

> 输入
> 
>> 3 5    
>> 2 7 2  
>
> 输出
> 
>> 2
> 
> 说明
> 
>> 吃掉第一个和第三个糖果，甜度值之和为 4，小于题目给定的 5。此时共吃掉两颗糖果，输出 2。

**python**

```python
""" 
贪心
"""

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    total = 0
    count = 0
    for num in a:
        if total + num <= k:
            total += num
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()
```

### 1.43 开心还是难过

**描述**

牛牛经常用 ":-)" 表示开心，用 ":-(" 表示难过； 

现在输入牛牛发出的一句话，请你判断牛牛是否开心？

**输入描述**

一行中给出字符串 str，代表牛牛发出的一句话。

$1 \le len(str) \le 100$  

字符串 str 包含：":-()?." 6 种字符，空格，大小写英文字母。

**输出描述**

若字符串中既没有 ":-)" 也没有 ":-("，则输出 "None"。

若字符串中 ":-)" 的数量大于 ":-(" 的数量，则输出 "Happy"。

若字符串中 ":-)" 的数量等于 ":-(" 的数量，则输出 "Just so so"。

若字符串中 ":-)" 的数量小于 ":-(" 的数量，则输出 "Sad"。

**示例 1**

> 输入
>
>> nowcoder:-)
>
> 输出  
>
>> Happy
> 
> 说明  
>
>> 有一个 :-) 因此输出 Happy

**示例 2**
 
> 输入  
>
>> I love China
> 
> 输出  
>
>> None
> 
> 说明  
>
>> 既没有 :-) 也没有 :-( 所以输出 None

**示例 3**

> 输入
> 
>> One :-( of :-) each.
> 
> 输出
> 
>> Just so so
>
> 说明
> 
>> 因为 :-( 和 :-) 的数量相等，所以输出 Just so so

**示例 4**

> 输入 
>> nowcoder :-(
>
> 输出
>
>> Sad
> 
> 说明
>
>> 字符串中 :-( 的数量多于 :-)，因此输出 Sad

**python**

```python
""" 
字符串
"""
import sys


def main():
    s = sys.stdin.read().strip()

    happy_count = s.count(":-)")
    sad_count = s.count(":-(")

    if happy_count == 0 and sad_count == 0:
        print("None")
    elif happy_count > sad_count:
        print("Happy")
    elif happy_count == sad_count:
        print("Just so so")
    else:
        print("Sad")


if __name__ == "__main__":
    main()


"""
def main():
    s = input().strip()
    count_happy = 0
    count_sad = 0
    n = len(s)
    for i in range(n - 2):
        if s[i] == ':' and s[i+1] == '-':
            if s[i+2] == ')':
                count_happy += 1
            elif s[i+2] == '(':
                count_sad += 1
                
    if count_happy == 0 and count_sad == 0:
        print("None")
    elif count_happy > count_sad:
        print("Happy")
    elif count_happy == count_sad:
        print("Just so so")
    else:
        print("Sad")

if __name__ == "__main__":
    main()
"""

```

### 1.44 数字游戏

**描述**

dd 在玩数字游戏，首先他拿到一个 x

当 x 不为零时进行如下操作

如果二进制 x 中有奇数个 1，则 x 二进制形式下最低位取反（即 0 变成 1，1 变成 0）

如果二进制 x 中有偶数个 1，则 x 二进制形式下非前导零最高位取反

询问对于一个 x，操作几次后变为零

**输入描述**

第一行一个正整数 ($1 \leq T \leq 1000000$)，表示询问组数

接下来 T 行，每行一个数 x（$0 \leq x \leq 1000000000$）表示询问的数字

由于本题数据量比较大，请选择较快的读入方式

**输出描述**

输出 T 行，每行是对应的答案

**示例 1**

> 输入
>
>> 3    
>> 0    
>> 1    
>> 5    
>
> 输出
> 
>> 0    
>> 1    
>> 2  

**python**

```python
""" 
递归
"""
import sys

sys.setrecursionlimit(1000000)

memo = {}
def f(x):
    if x == 0:
        return 0
    if x in memo:
        return memo[x]
    pop = bin(x).count('1') % 2
    k = x.bit_length() - 1
    if pop == 0:
        res = 1 + f(x - (1 << k))
    else:
        if x == 1:
            res = 1
        else:
            if x % 2 == 1:
                res = 2 + f(x - 1 - (1 << k))
            else:
                res = 2 + f(x + 1 - (1 << k))
    memo[x] = res
    return res

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out_lines = []
    for i in range(1, t + 1):
        x = int(data[i])
        out_lines.append(str(f(x)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
```

### 1.45 对称之美

**描述**

给出 n 个字符串，从第 1 个字符串一直到第 n 个字符串每个串取一个字母来构成一个新字符串，新字符串的第 i 个字母只能从第 i 行的字符串中选出，这样就得到了一个新的长度为 n 的字符串，请问这个字符串是否有可能为回文字符串？

**输入描述**

第一行一个数字 $t, 1 \leq t \leq 50$, 代表测试数据的组数

每组测试数据先给出一个数字 n，然后接下来 n 行每行一个只由小写字母组成的字符串 $s_i$

$1 \leq n \leq 100, 1 \leq |s_i| \leq 50$

**输出描述**

在一行中输出 "Yes" or "No"

**示例 1**

> 输入
> 
>> 2    
>> 1    
>> a    
>> 3    
>> a    
>> b    
>> c    
>
> 输出
> 
>> Yes   
>> No  

**python**

```python
""" 
字符串
"""
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    strings = []
    for i in range(n):
        s = input().strip()
        strings.append(s)
    
    left = 0
    right = n - 1
    possible = True
    while left < right:
        s1 = strings[left]
        s2 = strings[right]
        found_common = False
        for char1 in s1:
            for char2 in s2:
                if char1 == char2:
                    found_common = True
                    break
            if found_common:
                break
        if not found_common:
            possible = False
            break
        left += 1
        right -= 1
        
    results.append("Yes" if possible else "No")

for res in results:
    print(res)
```

### 1.46 异或和之和

**描述**

给一个数组，数组内有 n 个正整数。

求这些数任取 3 个数异或运算后求和的值。

也就是说，取一共 $C_n^3$ 个三元组，计算这些三元组内部异或，之后求和。（具体操作可以见样例描述）

由于该值可能过大，输出其对 $10^9 + 7$ 取模的值。

**输入描述**

第一行一个正整数 n。（$3 \leq n \leq 200000$）

接下来有 n 个正整数 $a_i$ 。（$1 \leq a_i \leq 10^{18}$）

**输出描述**

任取三个数、三元组内部异或后求和对 1000000007 取模的值。

**示例 1**

> 输入
> 
>> 4   
>> 3 4 5 6 
>
> 输出
> 
>> 10
> 
> 说明
>
>> 共有 4 个三元组：{3, 4, 5}、{3, 4, 6}、{3, 5, 6}、{4, 5, 6}  
>> 3 XOR 4 XOR 5 = 2  
>> 3 XOR 4 XOR 6 = 1  
>> 3 XOR 5 XOR 6 = 0  
>> 4 XOR 5 XOR 6 = 7  
>> 相加为 10。

**python**

```python
mod = 10**9 + 7

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    ans = 0
    for k in range(0, 61):
        c = 0
        for num in a:
            if (num >> k) & 1:
                c += 1
        cnt = 0
        if c >= 1 and n - c >= 2:
            cnt += c * ((n - c) * (n - c - 1) // 2)
        if c >= 3:
            cnt += c * (c - 1) * (c - 2) // 6
        ans = (ans + cnt * (1 << k)) % mod
        
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.47 四个选项

**描述**

众所周知，高考数学中有一个题目是给出 12 个单项选择，每一个选择的答案是 A，B，C，D 中的一个。

网上盛传答案存在某种规律，使得蒙对的可能性大大增加。于是今年老师想让你安排这 12 个题的答案。但是他有一些条件，首先四个选项的数量必须分别为 na，nb，nc，nd。其次有 m 个额外条件，分别给出两个数字 x，y，代表第 x 个题和第 y 个题的答案相同。 现在你的老师想知道，有多少种可行的方案安排答案。

**输入描述**

第一行五个非负整数 na，nb，nc，nd，m，保证 na+nb+nc+nd=12, $0 \le m \le 1000$。

接下来 m 行每行两个整数 $x, y (1 \le x, y \le 12)$ 代表第 x 个题和第 y 个题答案必须一样。

**输出描述**

仅一行一个整数，代表可行的方案数。

**示例 1**

> 输入
> 
>> 3 3 3 3 0
> 
> 输出
> 
>> 369600

**python**

```python
""" 
动态规划
"""
def main():
    import sys
    data = sys.stdin.read().split()
    na = int(data[0])
    nb = int(data[1])
    nc = int(data[2])
    nd = int(data[3])
    m = int(data[4])
    
    n = 12
    parent = list(range(n+1))
    size = [1] * (n+1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if size[rx] < size[ry]:
            parent[rx] = ry
            size[ry] += size[rx]
        else:
            parent[ry] = rx
            size[rx] += size[ry]
            
    index = 5
    for _ in range(m):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        union(x, y)
        
    comp_sizes = []
    visited = [False] * (n+1)
    for i in range(1, n+1):
        r = find(i)
        if not visited[r]:
            visited[r] = True
            comp_sizes.append(size[r])
            
    k = len(comp_sizes)
    
    dp = [[[0] * (nc+1) for _ in range(nb+1)] for _ in range(na+1)]
    dp[0][0][0] = 1
    
    total = 0
    for s in comp_sizes:
        new_dp = [[[0] * (nc+1) for _ in range(nb+1)] for _ in range(na+1)]
        for a in range(na+1):
            for b in range(nb+1):
                for c in range(nc+1):
                    if dp[a][b][c] == 0:
                        continue
                    if a + s <= na:
                        new_dp[a+s][b][c] += dp[a][b][c]
                    if b + s <= nb:
                        new_dp[a][b+s][c] += dp[a][b][c]
                    if c + s <= nc:
                        new_dp[a][b][c+s] += dp[a][b][c]
                    if total + s - a - b - c <= nd:
                        new_dp[a][b][c] += dp[a][b][c]
        total += s
        dp = new_dp
        
    print(dp[na][nb][nc])

if __name__ == "__main__":
    main()
```

### 1.48 [ZJOI2010] 数字计数

**描述**

给定两个正整数 a 和 b，求在 [a, b] 中的所有整数中，每个数码 (digit) 各出现了多少次。

**输入描述**

输入文件中仅包含一行两个整数 a、b，含义如上所述。

**输出描述**

输出文件中包含一行 10 个整数，分别表示 0-9 在 [a, b] 中出现了多少次。

**补充说明**

对于 30% 的数据，保证 $a \leq b \leq 10^6$；

对于 100% 的数据，保证 $1 \leq a \leq b \leq 10^{12}$。

**示例 1**

> 输入
> 
>> 1 99
> 
> 输出
> 
>> 9 20 20 20 20 20 20 20 20 20

**python**
                    
```python
"""
字符串
"""
def count_digit(n, d):
    if n <= 0:
        return 0
    base = 1
    ans = 0
    while base <= n:
        high = n // (base * 10)
        low = n % base
        cur = (n // base) % 10
        if d != 0:
            if cur > d:
                ans += (high + 1) * base
            elif cur == d:
                ans += high * base + low + 1
            else:
                ans += high * base
        else:
            if high != 0:
                if cur > 0:
                    ans += high * base
        else:
            if high != 0:
                if cur > 0:
                    ans += high * base
                else:
                    ans += (high - 1) * base + low + 1
        base *= 10
    return ans

def main():
    a, b = map(int, input().split())
    res = []
    for d in range(0, 10):
        cnt_b = count_digit(b, d)
        cnt_a_minus = count_digit(a - 1, d)
        res.append(str(cnt_b - cnt_a_minus))
    print(' '.join(res))

if __name__ == "__main__":
    main()
```

### 1.49 和零在一起

**描述**

小强有一个长度为 n 的 01 字符串 str，他想将字符串划分为几部分，且每部分都有且只有一个 0。小强只会去验证划分方案的正确性，但是小强他不知道对于这个字符串一共有多少总划分的方案，请你告诉小强总的方案数，答案可能很大请对 $10^9 + 7$ 取模。

**输入描述**

第一行为一个 n，表示 01 字符串的长度。

第二行为一个字符串 str。

$1 \le n \le 10^5$

**输出描述**

输出为一行，表示答案。

**示例 1**

> 输入
> 
>> 5   
>> 01010  
>
> 输出
> 
>> 4
> 
> 说明
> 
>> (01)(01)(0)   
>> (0)(101)(0)  
>> (01)(0)(10)  
>> (0)(10)(10)，一共有 4 种划分方案

**python**

```python
""" 
字符串
"""
MOD = 10**9 + 7

def main():
    n = int(input().strip())
    s = input().strip()
    
    positions = []
    for i, char in enumerate(s):
        if char == '0':
            positions.append(i)
            
    k = len(positions)
    if k == 0:
        print(0)
        return
        
    ans = 1
    for i in range(1, k):
        diff = positions[i] - positions[i-1]
        ans = (ans * diff) % MOD
        
    print(ans)

if __name__ == "__main__":
    main()
```

### 1.50 dd 爱科学 1.0

**描述**

大科学家 dd 最近在研究转基因白菜，白菜的基因序列由一串大写英文字母构成，dd 经过严谨的推理证明发现，只有当白菜的基因序列呈按位非递减形式时，这株白菜的高附加值将达到最高，于是优秀的 dd 开始着手修改白菜的基因序列，dd 每次修改基因序列的任意位需要的代价是 1，dd 想知道，修改白菜的基因序列使其高附加值达到最高，所需要的最小代价的是多少。

**输入描述**

第一行一个正整数 $n (1 \le n \le 1000000)$

第二行一个长度为 n 的字符串，表示所给白菜的基因序列

保证给出字符串中有且仅有大写英文字母

**输出描述**

输出一行，表示最小代价

**示例 1**

> 输入
> 
>> 5   
>> ACEBF  
>
> 输出
> 
>> 1
> 
> 说明
> 
>> 改成 ACEEF 或者 ACEFF，都只用改动一个字符，所需代价最小为 1

**python**

```python
""" 
字符串
"""
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1].strip()
    
    f = [0] * 26
    max_f = [0] * 26
    
    for c in s:
        idx = ord(c) - ord('A')
        new_val = max_f[idx] + 1
        if new_val > f[idx]:
            f[idx] = new_val
            for i in range(idx, 26):
                if max_f[i] < new_val:
                    max_f[i] = new_val
                else:
                    break
                    
    result = n - max_f[25]
    print(result)

if __name__ == "__main__":
    main()
```