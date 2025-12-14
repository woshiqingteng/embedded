"""
@brief merge sort
"""

import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)//2
    left, a = merge_sort(arr[:mid])
    right, b = merge_sort(arr[mid:])

    i = j = 0
    c = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            c += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, a + b + c

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))

    _, count = merge_sort(arr)
    
    print(count)

if __name__ == "__main__":
    main()