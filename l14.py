strs = ["aa","a"]

def longestCommonPrefix(strs):

    if not strs:
        return ""
    ans = ""
    j = 0

    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(len(strs)):
            if len(strs[j]) < i+1:
                return ans
            elif strs[j][i] != c:
                return ans
        j += 1
        ans += c
    return ans


print(longestCommonPrefix(strs))