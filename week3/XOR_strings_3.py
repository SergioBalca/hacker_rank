def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        """Modified line"""
        if s[i] == t[i]:
            """Modified line"""
            res += '0'
        else:
            """Modified line"""
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))
