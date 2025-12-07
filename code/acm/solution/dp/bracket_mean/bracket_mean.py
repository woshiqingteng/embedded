"""
@brief DP
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = [data[i].strip() for i in range(1, n+1)]
    
    def solve(str):
        n = len(str)
        dp = [0.0] * (n + 2)
        for i in range(n - 1, -1, -1):
            new_dp = [0.0] * (n + 2)
            for j in range(i + 1):
                char = str[i]
                if char == '(':
                    new_dp[j] = dp[j + 1]
                elif char == ')':
                    new_dp[j] = (1.0 + dp[j - 1]) if j > 0 else dp[j]
                else:  # char == '?'
                    opt1 = dp[j + 1]
                    opt2 = (1.0 + dp[j - 1]) if j > 0 else dp[j]
                    new_dp[j] = 0.5 * opt1 + 0.5 * opt2
            dp = new_dp
        result = dp[0]        
        print(f"{result:.6f}")
    
    for i in range(n):
        solve(s[i])

if __name__ == "__main__":
    main()