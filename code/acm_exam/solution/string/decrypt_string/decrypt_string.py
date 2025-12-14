"""
@brief 字符串
"""

def main():
    # input
    s = str(input().strip())
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for ch in s:
        if ch in vowels:
            result.append(ch)
        else:
            target = vowels[0]
            min_dist = abs(ord(ch) - ord(vowels[0]))
            for vowel in vowels[1:]:
                dist = abs(ord(ch) - ord(vowel))
                if dist < min_dist:
                    min_dist = dist
                    target = vowel
            # dist = [(abs(ord(ch) - ord(v)), v) for v in vowels]
            # target = min(dist)[1]
            # target = min(vowels, key=lambda v: (abs(ord(ch) - ord(v)), vowels.index(v)))
            result.append(ch + target + ch.upper())
    
    print(''.join(result))

if __name__ == "__main__":
    main()