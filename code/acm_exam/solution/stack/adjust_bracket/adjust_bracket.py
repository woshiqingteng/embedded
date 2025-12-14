"""
@brief 栈

左括号：入栈
右括号：栈为空，计数+1；栈不为空，弹出栈顶，如果不匹配，计数+1
栈中剩余左括号没有匹配，计数+len(stack)
"""
import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = [data[i].strip() for i in range(1, n+1)]

    # stack
    def adjust(s):
        stack = []
        count = 0
        match = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in match:
                stack.append(char)
            else:
                if not stack:
                    count += 1
                    continue
                top = stack.pop()
                if match[top] != char:
                    count += 1
            
        count += len(stack)

        return count

    # output
    for string in s:
        print(adjust(string))

if __name__ == "__main__":
    main()