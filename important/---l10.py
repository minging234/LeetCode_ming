""" regularmach """

class Solution(object):
    dic = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s,p) in self.dic:
            return self.dic[(s,p)]
        if p == s:
            self.dic[(s,p)] = True
            return True
        if len(p) < 2:
            if len(s) == 1 and p == '.':
                self.dic[(s,p)] = True
                return True
            else:
                self.dic[(s,p)] = False
                return False
        if p[1] == '*':
            if not s:
                self.dic[(s,p)] = self.isMatch(s,p[2:])
                return self.dic[(s,p)]
            if s[0] != p[0]:
                if p[0] != '.':
                    self.dic[(s,p)] = self.isMatch(s,p[2:])
                    return self.dic[(s,p)] 
                if p[0] == '.':
                    self.dic[(s,p)] = (self.isMatch(s[1:],p) or self.isMatch(s,p[2:]))
                    return self.dic[(s,p)]
            else:
                self.dic[(s,p)] = (self.isMatch(s[1:],p) or self.isMatch(s,p[2:]))
                return self.dic[(s,p)]
        else:
            if not s:
                self.dic[(s,p)] = False
                return False
            if s[0] != p[0]: 
                if p[0]!= '.':
                    self.dic[(s,p)] = False
                    return False
                if p[0] == '.':
                    self.dic[(s,p)] = self.isMatch(s[1:],p[1:])       
                    return self.dic[(s,p)]
            else:
                self.dic[(s,p)] = self.isMatch(s[1:],p[1:])
                return self.dic[(s,p)] 




s = Solution()
print(s.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c"))
