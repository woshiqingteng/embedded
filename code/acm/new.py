import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    values = list(map(int, data[1].split()))
    u = [int(data[i].split()[0]) for i in range(2, 1+n)]
    v = [int(data[i].split()[1])for i in range(2, 1+n)]
    
    tree = [[] for _ in range(n)]
    for i in range(n-1):
        tree[u[i]-1].append(v[i]-1)
    
    def dfs(node, current):
        current += values[node]
        max_sum = current if current < m else float('-inf')
        for child in tree[node]:
            max_sum = max(max_sum, dfs(child, current))
        
        return max_sum
    
    result = dfs(0, 0)
    print(result if result != float('-inf') else 0)

if __name__ == "__main__":
    main()