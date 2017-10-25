class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        stack1 = []
        for i in range(len(s)):
            stack1.append(s[i])

        stack2 = []
        for i in range(len(p)):
            stack2.append(p[i])

        while len(stack1) > 0 and len(stack2) > 0:
            char1 = stack1.pop()
            char2 = stack2.pop()
            if char2 == "*":
                char2 = self.getchar(stack2)
                if char2 == ".":
                    if len(stack2) >0:
                        char2 = stack2.pop()
                    else:
                        return True
                    if char2 == "." or char2 == "*":
                        m, n = self.tostring(stack1, stack2)
                        return self.isMatch(m,n)
                    elif self.jump(stack1, char1, char2) is False:
                        return False
                    else:
                        while self.jump(stack1, char1, char2) is not False:
                            stack1.pop()
                            stack1 = self.jump(stack1, char1, char2)
                            if stack1 is False:
                                return False
                            m, n = self.tostring(stack1, stack2)
                            if self.isMatch(m, n) is True:
                                return True
                        if self.jump(stack1, char1, char2) is False:
                            return False
                if char1 != char2:
                    stack1.append(char1)
                if char1 == char2 and len(stack1)>0:
                    stack1.pop()
                    stack2.append(char2)
                    stack2.append("*")
                    m, n = self.tostring(stack1, stack2)
                    if self.isMatch(m, n) is True:
                        return True

            elif char2 == ".":
                pass
            else:
                if char1 != char2:
                    return False

        if len(stack1) == len(stack2):
            return True
        else:
            return False

    def getchar(self,st):
        c = st.pop()
        if c == "*":
            c = self.getchar(st)
        return c

    def tostring(self, s, p):
        a = ""
        b = ""
        for i in range(len(s)):
            a = a + s[i]
        for j in range(len(p)):
            b = b + p[j]
        return a, b

    def jump(self, stack1, char1, char2):
        while char1 != char2 and len(stack1)>0:
            char1 = stack1.pop()
        if len(stack1) == 0:
            return False
        return stack1
