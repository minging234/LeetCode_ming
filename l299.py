""" Bulls and Cows """

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sc = []
        gu = []
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                sc.append(secret[i])
                gu.append(guess[i])
        for i in sc:
            if i in gu:
                cow += 1
                gu.remove(i)
        return str(bull)+ "A" + str(cow) + "B"