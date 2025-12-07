""" 
@brief 贪心
"""

from collections import defaultdict

def main():
    nums = list(map(int, input().split()))

    count = defaultdict(int)
    
    for num in nums:
        count[num-1] += 1
        count[num] += 1
        count[num+1] += 1
    
    max_count = max(count.values())

    print(max_count)

if __name__ == "__main__":
    main()