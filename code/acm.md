# ACM

## 2 exam

### 2.1 小红的密码锁

- [小红的密码锁](https://blog.csdn.net/weixin_49496731/article/details/127215276)

输入两个四位数的整数，表示密码锁的状态，只能逆时针拨动（9->8->...->0->9）密码锁的每一位数字，要求至少拨动多少次，能够使状态1变成状态2
例：
输入：9999 8888
输出：4
解析：每一位波动一次，总共四次可由状态1变为状态2

```python
# 读取输入
s1, s2 = input().split()

total = 0
for i in range(4):
    a = int(s1[i])
    b = int(s2[i])
    # 逆时针拨动次数
    total += (a - b + 10) % 10

print(total)
```

### 2.2 统计能整除数字的位数

一个正整数n,判断n是否可以被n中的每个数整除，求可被整除的个数；

eg: n= 7300 输出0, （7,3,0,0，都不可被7300整除）n=125, 输出2 （1和5可被125整除）。

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

### 2.3 

贪心

一个由有n个大小写字母组成的字符串，每操作一次可使大小写字母翻转，eg:A->a或a->A。问经过K次操作，使得，字符串中的大写字母最多，并返回大写字母的个数。

eg:
n=1 k=3  字符串：A   返回 0
n=5 k=3  字符串：arBrg  返回 4 

```python
def main():
    # 读取输入：第一行是 n 和 k，第二行是字符串
    n, k = map(int, input().split())
    s = input().strip()
    
    # 统计大写字母数量（使用内置函数 isupper()）
    U = sum(1 for char in s if char.isupper())
    L = n - U  # 小写字母数量
    
    # 核心逻辑
    if k <= L:
        result = U + k  # 可翻转所有k个小写字母
    else:
        r = k - L  # 剩余操作次数
        if r % 2 == 0:
            result = n  # 剩余次数为偶数，全部保持大写
        else:
            result = n - 1  # 剩余次数为奇数，有一个变为小写
    
    print(result)

if __name__ == "__main__":
    main()
```

### 2.4


n门考试，求成绩的中位数，算数平均值，去极值后的算数平均值，所有结果要求向下取整。

```python
def main():
    # 读取输入
    n = int(input().strip())
    scores = list(map(int, input().split()))
    
    # 计算算术平均值并向下取整
    total_sum = sum(scores)
    mean_value = total_sum / n
    mean_floor = int(mean_value)  # 向下取整
    
    # 计算中位数并向下取整
    sorted_scores = sorted(scores)
    if n % 2 == 1:
        median_value = sorted_scores[n // 2]
    else:
        median_value = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    median_floor = int(median_value)  # 向下取整
    
    # 计算去极值后的算术平均值并向下取整
    if n <= 2:
        trimmed_floor = 0  # 处理n≤2的情况
    else:
        trimmed_scores = sorted_scores[1:-1]  # 去掉最低和最高分
        trimmed_mean = sum(trimmed_scores) / (n - 2)
        trimmed_floor = int(trimmed_mean)  # 向下取整
    
    # 输出结果（顺序为中位数、算术平均值、去极值平均值）
    print(median_floor)
    print(mean_floor)
    print(trimmed_floor)

if __name__ == "__main__":
    main()
```

### 2.5

贪心

一个长度为n的数组，可以分为k个不相交的非空子序列，使得子序列的极差之和最大，返回最大的极差值

eg：
n=5,k=3,[1,2,3,4,5] 可拆为{1,5}{2,4}{3} 返回6
n=5,k=3,[2,2,2,2,2] 返回0

```python
import sys

def main():
    # 读取输入
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # 排序数组
    arr_sorted = sorted(arr)
    
    # 计算最大极差和
    m = min(k, n // 2)  # 最多可形成的有效子序列对数量
    total = 0
    for i in range(m):
        total += arr_sorted[n-1-i] - arr_sorted[i]
    
    print(total)

if __name__ == "__main__":
    main()
```

### 2.6

双指针、滑动窗口

两个人玩游戏，
1.如果a这次的游戏分数大于上次，b这次的游戏分数小于上次，则a嘲笑b。
2.如果a这次的游戏分数大于上次，b这次的游戏分数也大于上次，若a两次游戏的分差>b两次游戏的分差，则a嘲笑b
3.只有a两次游戏的分差=b两次游戏的分差，a，b互不嘲笑
求a.b最长互不嘲笑的子数组长度

a=[1,3,4,5,6,0]
b=[-1,1,4,2,5,1]
返回2，只有{1，3} {-1,1}a和b互不嘲笑

```python
import sys

def main():
    data = sys.stdin.read().splitlines()
    a = list(map(int, data[0].split()))
    b = list(map(int, data[1].split()))
    n = len(a)
    
    max_len = 1  # 最短的子数组长度至少为1（单次游戏）
    left = 0
    
    for right in range(1, n):  # right从1开始，因为需要比较right和right-1
        # 检查当前right和right-1这两轮游戏是否导致嘲笑
        a_diff = a[right] - a[right-1]
        b_diff = b[right] - b[right-1]
        
        # 条件1: A增B减
        condition1 = (a_diff > 0 and b_diff < 0)
        # 条件2: A增B增且A分差>B分差
        condition2 = (a_diff > 0 and b_diff > 0 and a_diff > b_diff)
        
        # 如果当前窗口的右边界新加入的元素导致了嘲笑条件
        if condition1 or condition2:
            # 需要移动左指针，直到窗口内没有嘲笑事件
            # 最简单的方式是将left移动到right-1，因为嘲笑只发生在(right-1, right)这一对之间
            # 但为了代码清晰，我们让left直接跳到right，新的窗口从right开始
            left = right  # 注意：这样max_len至少能记录单次游戏的长度1
        else:
            # 如果没有发生嘲笑，更新最大长度
            current_length = right - left + 1
            if current_length > max_len:
                max_len = current_length
    
    print(max_len)

if __name__ == "__main__":
    main()
```

### 2.7

栈

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

### 2.8

给定多组输入，每组两个数字，前面的代表分子，后面的代表分母，对形成的分数进行排序

```python
import sys
from fractions import Fraction  # 使用Fraction避免浮点数精度问题

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    # 解析输入：第一行是分数对的数量n，后面每行是一个分数对（分子 分母）
    n = int(data[0])
    fractions = []
    
    for i in range(1, n + 1):
        numerator, denominator = map(int, data[i].split())
        fractions.append((numerator, denominator))
    
    # 使用Fraction进行精确排序，避免浮点数精度问题
    sorted_fractions = sorted(fractions, key=lambda x: Fraction(x[0], x[1]))
    
    # 输出排序结果
    for num, den in sorted_fractions:
        print(f"{num} {den}")

if __name__ == "__main__":
    main()
```

### 2.9

对答案：牛牛期末考试全部为选择题，且只有A、B两个选项，牛牛做题时直接蒙的答案，现在考试结束，牛牛拿到答案后，想知道如果之前蒙的答案全部相反，能不能获得更高的分数,不能获得更高分输出"Oh,Yes",可以则输出"Oh,No",一样则输出"O.O"。输入第一行为有N组输入，第二行为第一组选择题个数，第三行为牛牛蒙的答案，第四行为正确答案,以此类推。

例：
2
2
AA
AB
3
ABA
BBB
对应输出：
O.O
Oh,No

```python
def main():
    n = int(input().strip())
    results = []
    for _ in range(n):
        num_questions = int(input().strip())
        cow_answer = input().strip()
        correct_answer = input().strip()
        
        # 计算原始得分（牛牛当前答案的正确题数）
        original_score = sum(1 for i in range(num_questions) if cow_answer[i] == correct_answer[i])
        
        # 生成相反答案（A变B，B变A）
        opposite_answer = ''.join('B' if char == 'A' else 'A' for char in cow_answer)
        
        # 计算相反答案的得分
        opposite_score = sum(1 for i in range(num_questions) if opposite_answer[i] == correct_answer[i])
        
        # 根据规则输出结果
        if original_score > opposite_score:
            results.append("Oh,Yes")
        elif original_score < opposite_score:
            results.append("Oh,No")
        else:
            results.append("O.O")
    
    # 输出所有结果
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```

### 2.10

已知一个由数字组成的序列，可以对该序列进行任意切割，如果切割后的数字和为质数，则记录该质数，要求输出所有质数的个数。

例：123（不切和为123；切为1、23，和为24；切为12 、3，和为15；切为1、2、3，和为6），没有质数输出0

```python
import math
import sys

def is_prime(n):
    """判断一个数是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # 读取输入字符串
    s = sys.stdin.readline().strip()
    n = len(s)
    if n == 0:
        print(0)
        return
    
    total_ways = 1 << (n - 1)  # 切割方式总数：2^(n-1)
    prime_set = set()  # 存储不同的质数和
    
    # 遍历所有切割方式（用位掩码表示）
    for mask in range(total_ways):
        current_sum = 0
        start_index = 0
        # 遍历每个字符位置
        for i in range(n):
            # 如果在当前位置i之后切割（掩码对应位为1）或已是最后一个字符
            if i < n - 1:
                if mask & (1 << i):  # 检查掩码第i位是否为1
                    num_segment = s[start_index:i+1]
                    if num_segment:  # 避免空字符串
                        current_sum += int(num_segment)
                    start_index = i + 1
            else:  # 处理最后一个字符
                num_segment = s[start_index:i+1]
                if num_segment:
                    current_sum += int(num_segment)
        
        # 检查当前切割方式的数字和是否为质数
        if is_prime(current_sum):
            prime_set.add(current_sum)
    
    print(len(prime_set))

if __name__ == "__main__":
    main()
```

### 2.11

位运算

有整数X、Y、A、B，其中X<=Y
X、Y位取与得到A，
X、Y位取或得到B。
输入：A、B
输出：（X,Y）的对数
示例：输入A=4, B=7，输出2
注：（4,7）（5,6）

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

### 2.12

- 可以对数组 a 中的每个元素任意进行+1 、-1 或不执行操作，求可以得到相同整数的最大个数
输入：整数 n ，数组 a(n)
输出：相同整数的最大个数
示例：输入 1 2 3 ；输出 3   

```python

```

### 2.13

- t组，每组输入一个长度为n的数组ai，从中任选三个数，若存在一种选取方式使三个数无法构成三角形，输出Yes，否则输出No
输入：
2   //t
6   //数组长度n
3 4 5 6 6 6
5   //数组长度n
1 1 5 5 5
输出：
No
Yes

```python

```



- ref
    
    - [?有效的括号字符串](https://leetcode.cn/problems/valid-parenthesis-string/description/)
    - [不可能三角](https://www.nowcoder.com/discuss/750016145939247104?sourceSSR=post)
    - [acmer子串代价](https://www.codeleading.com/article/37046020529/)
    - [质数和相加/拆解](https://www.nowcoder.com/practice/c96d6acc025541ffb79c579688f8d003?tpId=167&tqId=34053&ru=/exam/oj)
- [01串切割](https://blog.csdn.net/ouyang_peng/article/details/150503091)
    - [好串](https://www.nowcoder.com/discuss/660859777223819264)
    - [路径总和](https://leetcode.cn/problems/path-sum-ii/description/)
    - [牛牛吃饭期望]()
    - [牛牛打枪]()
        - 牛牛打枪，假设子弹数量不限。刚开始枪没有安装子弹，一个弹夹有m个子弹，安装弹夹需要a分钟，安装1个子弹b分钟，开一枪需要1分钟，求牛牛开n枪，最小多少分钟

- 字符串的权值。一个字符串的权值定义为a-b,其中a定位为字符串中存在偶数个字符的个数，b定义为字符串中存在奇数个字符的个数。如eggff,偶数个字符g,f,那么a=2,奇数个字符只有e,所以b=1,字符串的权值为2-1=1.输入一个字符串，可以任何位置分割，求所有子字符权值和的最大值。

- 一个长度为n，值为0的数组，每次输入三个数l,r,v，对序列[l~r]，如果下标是v的倍数，则该下标对应的值＋1，操作次数为q次,输出操作完的数组
例
5 2
1 4 1
1 5 2
第一次操作[1 1 1 1 0]（1~4是1的倍数）
第二次操作[1 2 1 2 0]（2和4是2的倍数）
输出 [1 2 1 2 0]

- 骰子：有一个N面的骰子，小红希望掷出X,Y(X不等于Y),第二行输入骰子每面的数字，求理论掷出X和Y需要的总次数，保留小数点后一位。
例：2 1 2
1 2
输出为4.0（掷出1的概率为二分之一，掷出2的概率为二分之一，理论上4次可包含掷出1、2的情况）
例2：
输入 ：
5 1 2
1 2 2 2 3
输出：
8.3

- 输入一个大小为n的数组，分成互不交叉的k个子序列，输出所有子序列的极差求和的最大值
例：
输入
5 3
1 2 3 4 5
输出6
{1 5}{2 4}{3}=4+2+0=6

- n名学生参与测试，对所有学生按照如下要求进行重新排序分组：
1.每组人数不超过三人
2.三人组要求最高成绩与最低成绩差值小于10
3.两人组要求最高成绩与最低成绩差值小于20
4.一人组不做要求
输出n个学生最少分多少组。

输入：
第一行n
第二行n个数代表n个学生的成绩

- 已知一个长度为n的序列由1~n中的数字组成，保证序列中每个元素各不相同，该序列中的数字可以进行如下操作：
1.与相邻的数字交换位置，自身和相邻数字同时消耗一次交换机会
已知每个数字最多有两次交换机会，输入最终得到的字典序最大的序列

输入：
第一行n
第二行n个数代表初始序列
输出：
字典序最大的序列号

例：
输入：
8
3 7 2 1 5 6 4 8
输出：
7 3 5 6 2 1 8 4


- 存在一个数组，该数组中元素为从1到n的整数，互不重复，已知该数据的长度n和在缺少某个元素时的数组剩余元素的异或和，希望得到该数组缺失的元素。
输入：第一行为用例个数，之后第一行为第一个用例，包含两个数n,k，n表示整数，k表示为当前异或和，
输出为缺失的整数
例如：
输入：1
      5 2
输出：3
解释：1^2^4^5 = 2，故缺少元素3

- 计算a*b大小的砖砌成的横X块,竖Y块构成的墙面，从左上角到右下角的对角线以及右上角到左下角的对角线一共穿越了多少次砖的边界
输入：a,b,x,y
输出：sum(左对角线经过每条砖缝与+右对角线经过每条砖缝)

- 计算一个数字串能被三整除的最大字符串（值最大第一，若多个串相等，取长的字符串）
输入：“10000666”
输出：“0000666”

- 一个数组中取数的【1：n】，要求使取到所有数的和为奇数，且取到每个数均为奇数（若ai是偶数那么取ai-1），特别说明：每个元素要么取奇数要么不取，输出取到的总和的最大值
输入：[1，2，3，4]
 3 3 1 
输出：7
输入：【1，3，3，4，5】
输出【5 3 3 3 1 】 =15

- 字符串包含{,},?.小红有魔法，把？变成{或}的概率分别是50%。求组成括号对的期望E
输入：包含{，}，？的字符串
输出：期望E

- 参数k，从左到右遍历数组，若ai mod k > ai+1 mod k,则交换ai 和 ai+1的位置。将对k属于【0，m】的每一个数对数组进行遍历，输出最终的数组。
输入 n,m(分别是数组大小和遍历次数)
输出： 最终的数组

- 池化操作，假设给一个8*8的矩阵，将矩阵分成四个2*2的矩阵，选出每个矩阵中第二大的数，
将这些数排成一个4*4的矩阵，反复操作，直到将一个N*N的矩阵简化为1*1.
输入
4
-6 -8 7 4
-5 -5 14 11
11 11 -1 -1
4 9  -2 -4
输出 9

- 最大合法数组长度：给定一个N个元素的数组，输出其中不包含0的子数组的最大长度
第一行输入一个N，表示数组长度，第二行输入N个数字，表示数组内容
6    //数组长度
1 2 3 0 4 5 0   //数组
输出 3 //不包含0的子数组有[1 2 3]和[4 5]，长度分别为3和2，输出3

- 输入一个字符串，使其自符串中出现连续的AcMer的代价最小；
字串变为AcMer的原则，现把当前字符变为和AcMer对应的大小写（其中每个字符变换大小写的代价都为5），然后再转换为对应的字符（其中每个字符转换的代价为5）

输入一个字符串，使字符串中出现子串AcMer的代价最小
可对字符串进行以下2种操作：
1、将其中一个字母转换为其对应大写或小写字母，代价为5。（例如a->A，D->d）
2、将其中一个字母转换为相同大小写的其他字母，代价为5。（例如A->D，d->e）
输入一个字符串 aaAAcderrrrr
输出最小代价 10     //将字串Acder中的d变为D得到AcDer（代价5），再将AcDer中的D变为M得到AcMer（代价5，一共10）

- 小红定义了好数：某一数值的二进制中的“1”的个数为偶数，则为好数，
小红拿到了n个元素的数组，希望输出其中好数的异或和，请你帮帮她。

- 给定一个数组，每次操作可以从数组中取任意个元素，对其同时减少2^k（k任选），最少进行多少次操作，可以将整个数组所有元素变为0

与这个题目类似：整数每次可以减2^k，k=0,1,2...
求该整数减到0需要几次
1    需要1次
3    需要2次
input:
2
1
2 ->0  1 0
3
1 2 3 -> 1 0 1 ->0 0 0 
001 
010 
011
output:
1
2

- 有n个木板，每个木板宽度是1，第i个木板的高度是ai，输入一行数，分别代表n个木板的高度，将这些木板任意顺序竖起来排列，请问可以截取的正方形边长最大是多少，如输入5，1，2，3，4，输出3

- 数字n，任意分割，也可以不分割，如123，可以分割成1和23，也可以分割成1，2，3，将分割后的数求和，请问n，任意分割后，有多少种和

- 发射火箭，地球半径为R，球心坐标为（0，0，0），发射点坐标为x,y,z，火箭三个坐标向的速度为vx，vy，vz，请问火箭飞出大气层的时刻，输入t组，每组一行，每行行输入分别为，y，z，vx，vy，vz，R，每行输出一个时刻

- 输入一个长度为n的01字符串，要求输出一个长度为n的数组，要求数组的每一个元素等于字符串从第1个元素开始到当前位置上不等于当前位置字符的累计计数。
例如：
输入：010101
输出： 0 1 1 2 2 3
解释：输出数组中，第一个元素为0：因为字符串第一个元素左边没有元素；第二个元素为1，因为字符串第二个元素为1，而第二个元素左边累计为0的字符数为1；第三个元素为1，因为字符串第三个元素为0，而第三个元素左边累计为1的元素个数为1；……

- 输入字符串“aaabaaa"和整数k（如k=3），
输出字符串中最多个数的好串，好串为不交叉子串

- 输入字符串“()?)??)”，？为左右括号的概率0.5，计算一共有多少对括号（）

- 输入n个整数的数组ai，再输入n个字母的字符串si，si只包含‘R’或'B'，si为'R'代表ai为红数，si为'B'代表ai为黑数，取一个红数与一个黑数相乘得到红黑数，问所有红黑数的和为多少？
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

- 有两个数组a和b，其中数组元素个数都为n，可以按照序列（i，j）对数组a[i]和a[j]同时加1，请问至少执行多少次操作，才能使得数组a和b完全相等，如果无法使得两个数组相等，则输出-1

输入：
第一行输入数组元素个数n；
第二行输入n个整数，表示数组a中各个元素的具体值；
第三行输入n个整数，表示数组b中各个元素的具体值；


输出：操作次数

例：
输入：
4
1 2 3 5
1 2 4 4
输出：
1 (注：(i=2，j - 3)，表示对数组a[2]和数组b[3]分别加1，使得数组a和b完全相等)

- "（'“）”组成的字符串，求最长的合法子序列长度
如：“（）”、“（）（）”、“（（））”、“（（）（））”均为合法子序列；“）（”、“（（”、“（（）”均为不合法子序列。

"（）”组成的字符串，求最长的合法前缀子序列

()())    4

- 输入两个字符串s和t，将t的后半段嫁接到s后面，输出嫁接后的s和剩余前半段的t。
输入：
第一行：字符串s:abd
第二行：字符串t:asdfgg
输出：
abdfgg
asd

- 一个字符串，求包括‘r''e'同时不包括’d'的子串数量。

- 给定a,b,c分别代表三角形的三条边，输入x,y,z三个数作为三角形边长，判断能否组成三角形，不能则输出“can not”；如果能，组成的三角形与abc组成的三角形相似，则输出“similar",否则，输出"can,but not similar".

- 给定2个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断经过几次调整字符串把它变成有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号
如：
如：
输入:2
（ {[ ] ]）-> 一次调整
   （ {[ ] ]} ->两次调整
输出: 1
          2

- 已知大写字母ASCII值'A'=65，给出一个字符串，求字符串中没有出现的字母ASCII和
ABBCDEF

- 两个人从起点和终点往中间走，求走过节点的和delta最小是多少 两个人相向而行, 在路上经过一些数字, 每个数字的位置有不同的价值,分别计算两个人分别走几步,最好总价值的差值的绝对值最小,输出最小绝对值和分别走几步

- 求最近公共父节点

- 有n个商店，第i个商店的产品数量为yi，价格为xi，如果购买给定数量m个产品；输出总价最小的数值。
输入
第一行为商店个数 n及购买个数m
接下来n 行输入，每行两个整数xi,yi.
输出
购买m个商品所需的最小金额。

- 购买n个商品，价格为xi，商家为促销提供了n个折扣ai，每个折扣只能使用一次，如何使用折扣使花费最少
输入：第一行输入商品和折扣数目n，
接下来n行输入，每行两个整数xi，ai
输出：购买商品的最小金额

- 小红定义函数f(x)为x二进制数的最小1对应的数，比如10(1010)对应的数为2,12(1100)对应的数为4。输入整数n，输出i/f(i)【1<=i<=n】的加和
输入：正整数n
输出：i/f(i)【1<=i<=n】的加和

- 小红有一个2x2的印章，要求不能相邻盖章（公共边或公共角均不可）以及重复盖章。现在小红忘记了自己的盖章顺序，给定一张盖完后的表格，帮助小红确认盖章是否规范
0代表未盖章的格子，1代表盖章后的格子
输入：第一行输入两个整数x,y，代表表格的行与列
接下来给出一张x行y列的表
输出：表格规范输出Yes，否则输出No
例1：输入：4 4
1 1 0 0
1 1 0 0
0 0 1 1
0 0 1 1
输出：No
解释：两个章存在相邻角
例2:输入：5 6
1 1 0 0 0 0
1 1 0 0 0 0
0 0 0 1 1 0
0 0 0 1 1 0
0 0 0 0 0 0
输出：Yes

- 最大合法数组长度：给定一个N个元素的数组，输出其中不包含0的子数组的最大长度。
例：5
1 0 2 3 0
输出为2，最长为([2,3])



- 将字符串转换为大写
输入一个全是小写的字符串，它的下标p从1开始，直到n，如果下标的二进制表示中1的数量为奇数，则把对应的字母转换为大写，否则不变
例：
输入：abcdefg
输出：ABcDefG
// 1 2 3 4 5 6 7
0000 0001 % 2=1
0000 0010 % 2 =0
0000 0011%2 = 1
000 0001 % 2 =1


- 输入四个正整数，求他们的最小公约数（大于1的？），如果没有则返回-1

- 输入一个数n，其后跟n行人名和游戏，表示这个人玩了哪些游戏，要求按人名和游戏名出现的先后顺序输出每个人玩的游戏
输入：
3
name1:game2
name2:game3
name1:game1
输出：
name1:game2 game1
name2:game3
//
数组存储人名 （维护人名出现的顺序）
struct{name ，game（数组）}

- 一个字符串s，截取连续k个相同的字母为子串，最多可以截多少个相同的子串？（子串之间不可重叠）
输入：第一行为字符串s，第二行为子串长度k
输出：最大个数
输入 
14 3
acccbcccaaabbb
输出
2
说明，2个ccc子串，一个aaa子串，1个bbb字串，ccc的数量最多，所以输出2

- 一个字符串，只包含0，1 第1次截取开始1个，字符串去除截取的子串，第2次截取2个，以此类推，但10次后，重新从1开始，
输出每次截取子串的十进制数

110100100011
  10100100011
      100100011
            100011
                    11 （不足5，退出）

- n个学生考试m门课，这些学生中，只要有一门课高于本门课的平均成绩，老师就要给这位学生发祝贺短信，求老师要给多少名学生发祝贺短信。
输入：第一行输入m,n分别表示课程数、学生人数；之后的m行n列，表示每个学生的成绩；
输出：给多少名学生发祝贺短信
3 3
1 2 3 =avg=2 
2 3 2
2 2 2

