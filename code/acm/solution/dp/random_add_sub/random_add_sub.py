""" 
@brief DFS
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    m = int(data[0])
    nums = list(map(int, data[1].split()))
    n = len(nums)

    def dfs(index, current):
        if index == n:
            return abs(current - m)
        add = dfs(index+1, current + nums[index])
        sub = dfs(index+1, current - nums[index])

        return min(add, sub)
    
    result = dfs(1, nums[0])

    print(result)

if __name__ == "__main__":
    main()