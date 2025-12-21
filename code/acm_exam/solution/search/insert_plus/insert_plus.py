"""
@brief DFS

思路：
    DFS 对字符串从头递归，并更新和，递归到尾判定是否为质数
"""

import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def dfs(s, start, current):
    n = len(s)
    if start == n:
        return 1 if is_prime(current) else 0
    
    count = 0
    for end in range(start+1, n+1):
        num = int(s[start:end])
        count += dfs(s, end, current+num)
    
    return count

def main():
    s = input().strip()
    
    result = dfs(s, 0, 0)
    print(result)

if __name__ == "__main__":
    main()