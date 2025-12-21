"""
@brief 计数

思路：
    每位数计数
    数字除3取余，按结果：
        余数为1，删除1组最小数，不行删除2个2组最小数，不行返回-1
        余数为2，删除2组最小数，不行删除2个1组最小数，不行返回-1
    计数结果倒序输出
"""

import sys

def multiple_of_three(s):
    digit = [int(c) for c in s]
    remainder = sum(digit) % 3
    count = [digit.count(i) for i in range(10)]

    def remove_one(count, candidates):
        for digit in candidates:
            if count[digit] > 0:
                count[digit] -= 1
                return True
        return False

    def remove_two(count, candidates):
        removed = 0
        for digit in candidates:
            while count[digit] > 0 and removed < 2:
                count[digit] -= 1
                removed += 1
            if removed == 2:
                return True
        return False

    if remainder == 1:
        if not remove_one(count, [1, 4, 7]):
            if not remove_two(count, [2, 5, 8]):
                return "-1"
    elif remainder == 2:
        if not remove_one(count, [2, 5, 8]):
            if not remove_two(count, [1, 4, 7]):
                return "-1"

    result = "".join([str(i) * count[i] for i in range(9, -1, -1)])
    
    if not result:
        return "-1"
    elif result[0] == "0":
        return "0"

    return result

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [data[i].strip() for i in range(1, n+1)]

    for s in a:
        result = multiple_of_three(s)
        print(result)

if __name__ == "__main__":
    main()