def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    if not t:
        return False
    if s[0] == t[0]:
        return isSubsequence(s[1:], t[1:])
    return isSubsequence(s, t[1:])


if __name__ == '__main__':
    print(isSubsequence("abc", "ahbgdc"))
