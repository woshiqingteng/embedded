"""
@brief 分组讨论

思路：
    每位数除3取余，按取余结果分为0、1、2三组（1、2组倒序）
    数字除3取余，按结果：
        余数为1，删除1组最小数，不行删除2个2组最小数，不行返回-1
        余数为2，删除2组最小数，不行删除2个1组最小数，不行返回-1
    对0、1、2三组合并并进行倒序
"""

import sys

def multiple_of_three(s):
    digits = [int(c) for c in s]
    total = sum(digits)
    remainder = total % 3

    rem0 = [d for d in digits if d % 3 == 0]
    rem1 = sorted([d for d in digits if d % 3 == 1], reverse=True)
    rem2 = sorted([d for d in digits if d % 3 == 2], reverse=True)
    
    if remainder == 1:
        if rem1:
            rem1.pop()
        elif len(rem2) >= 2:
            rem2.pop()
            rem2.pop()
        else:
            return "-1"
    elif remainder == 2:
        if rem2:
            rem2.pop()
        elif len(rem1) >= 2:
            rem1.pop()
            rem1.pop()
        else:
            return "-1"
    
    tmp = rem0 + rem1 + rem2
    tmp.sort(reverse=True)
    result = "".join(str(d) for d in tmp)

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