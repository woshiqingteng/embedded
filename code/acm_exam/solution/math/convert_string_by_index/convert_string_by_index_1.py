""" 
@brief 内置函数计算
"""

def main():
    s = input().strip()
    
    result = []
    for i, c in enumerate(s):
        count = bin(i).count('1')
        if count % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c)
    
    print("".join(result))

if __name__ == "__main__":
    main()