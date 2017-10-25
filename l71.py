class Solution(object):
    @classmethod
    def simplifyPath(cls,path):
        """
        :type path: str
        :rtype: str
        """
        plist = path.split('/')
        if len(plist)<1:
            return ''
        ouc = []
        ans =''

        for i in plist:
            if i == '.':
                pass
            elif i == '..':
                if len(ouc) > 0:
                    ouc.pop()
            elif i == '':
                pass
            else:
                ouc.append(i)
        for i in ouc:
            ans += '/'+i
        if ans == '':
            ans = '/'
        return ans




print(Solution.simplifyPath('/'))
