""" 
@brief 栈
"""

def main():
    # input
    s = input().strip()
    
    stack = []
    max_len = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if not stack:
                break
            stack.pop()
            if not stack:
                max_len = i + 1
    
    print(max_len)

if __name__ == "__main__":
    main()