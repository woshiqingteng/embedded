"""
@brief 数学
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = [data[i].strip() for i in range(1, n+1)]

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
    
    def build_result(count):
        result_chars = []
        for digit in range(9, -1, -1):
            result_chars.append(str(digit) * count[digit])
        return ''.join(result_chars)

    def solve(s):
        count = [0] * 10
        digits = [int(char) for char in s]
        total_sum = sum(digits)
        for d in digits:
            count[d] += 1
        
        remainder = total_sum % 3
        if remainder == 1:
            if not remove_one(count, [1, 4, 7]):
                if not remove_two(count, [2, 5, 8]):
                    return ""
        elif remainder == 2:
            if not remove_one(count, [2, 5, 8]):
                if not remove_two(count, [1, 4, 7]):
                    return ""

        result = build_result(count)

        if result and result[0] == '0':
            return "0"
        
        return result
    
    for i in range(n):
        print(solve(s[i]))

if __name__ == "__main__":
    main()