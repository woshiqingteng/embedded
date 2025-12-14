"""
@brief eval
"""

def main():
    # input
    s = str(input().strip())
    n = len(s)

    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        try:
            result = eval(string)
            max_result = max(max_result, result)
        except:
            continue

    print(max_result)

if __name__ == "__main__":
    main()