""" 
@brief 贪心

思路：
    初始化字典，对数组中每个数的 +1、-1、不操作进行计数，统计最大值
"""

def main():
    a = list(map(int, input().split()))

    count = {}
    for x in a:
        count[x-1] = count.get(x-1, 0) + 1
        count[x] = count.get(x, 0) + 1
        count[x+1] = count.get(x+1, 0) + 1
    
    max_count = max(count.values())

    print(max_count)

if __name__ == "__main__":
    main()