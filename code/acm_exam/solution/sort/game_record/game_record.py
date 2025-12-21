""" 
@brief 字典

思路：
    字典集合去重
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(str, data[i].strip().split())) for i in range(1, n+1)]

    result = {}
    for name, game in a:
        if name in result:
            result[name].add(game)
        else:
            result[name] = set()
            result[name].add(game)

    for name in result:
        game = result[name]
        print(f"{name}: {" ".join(game)}")

if __name__ == "__main__":
    main()