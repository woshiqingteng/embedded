""" 
@brief 字典
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    name = [str(data[i].strip().split()[0]) for i in range(1, n+1)]
    game = [str(data[i].strip().split()[1]) for i in range(1, n+1)]
    
    result = {}
    for i in range(n):
        if name[i] in result:
            result[name[i]].add(game[i])
        else:
            result[name[i]] = set()
            result[name[i]].add(game[i])

    # output
    for name in result.keys():
        game = result[name]
        print(f"{name}: {', '.join(game)}")

if __name__ == "__main__":
    main()