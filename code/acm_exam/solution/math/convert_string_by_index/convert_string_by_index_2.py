""" 
@brief 手动计算
"""

def count_one(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def main():
    s = input().strip()
    
    result = []
    for i, c in enumerate(s):
        count = count_one(i)
        if count % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c)
    
    print("".join(result))

if __name__ == "__main__":
    main()