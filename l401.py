class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # hdic = {0:[],1:[],2:[],3:[],4:[]}
        # mdic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
        # for i in range(12):
        #     sumi = 0
        #     j = i
        #     while i != 0:
        #         if i & 1 == 1:
        #             sumi += 1
        #         i = i >> 1
        #     hdic[sumi].append(str(j))
        
        # for i in range(60):
        #     sumi = 0
        #     j = i
        #     while i != 0:
        #         if i & 1 == 1:
        #             sumi += 1
        #         i = i >> 1
        #     if j < 10:
        #         j = "0" + str(j)
        #     else:
        #         j = str(j)
        #     mdic[sumi].append(j)
        # print(hdic,mdic)

        hdic = {0: ['0'], 1: ['1', '2', '4', '8'], 2: ['3', '5', '6', '9', '10'], 3: ['7','11']}
        mdic = {0: ['00'], 1: ['01', '02', '04', '08', '16', '32'], 2: ['03', '05', '06', '09', '10', '12', '17','18', '20', '24', '33', '34', '36', '40', '48'], 3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50','52', '56'], 4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'], 5: ['31', '47', '55', '59']}
        total = []
        for i in range(num+1):
            if i in hdic and num-i in mdic:
                for p in hdic[i]:
                    for q in mdic[num-i]:
                        total.append(p+":"+ q)
        return total
    

        
s = Solution()
print(s.readBinaryWatch(1))


