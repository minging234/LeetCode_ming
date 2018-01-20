""" Minimum Index Sum of Two Lists """

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans =[]
        menu = {}
        ism = float('inf')
        for i in range(len(list1)):
            menu[list1[i]] = i
        
        for j in range(len(list2)):
            if list2[j] in menu: 
                ids = menu[list2[j]] + j
                if ids < ism:
                    ism = ids
                    ans = [list2[j]]
                elif ids == ism:
                    ans.append(list2[j])
        
        return ans
                
                