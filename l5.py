
s = 'babad'


def ispda(s):
    if s[::-1]== s:
        return True
    else:
        return False

def maxpda(s):
    outc = s[0]
    for i in range(len(s)):
        if s[i] not in s[i:]:
            continue
        else:
            j = len(s[i:])
            while j > 0:
                if s[i + j - 1] == s[i]:
                    iterm = s[i:i + j]
                    if iterm[::-1] == iterm:
                        if len(outc)<len(iterm):
                           outc = iterm
                        break
                j -= 1

    return outc

print(maxpda(s))


# an very interesting solution of this problem
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]


