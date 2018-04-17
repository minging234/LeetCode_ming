""" 150. Evaluate Reverse Polish Notation """

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numbers = []
        for i in tokens:
            if i == '+':
                n2 = numbers.pop()
                n1 = numbers.pop()
                numbers.append(n1 + n2)
            elif i == '-':
                n2 = numbers.pop()
                n1 = numbers.pop()
                numbers.append(n1 - n2)
            elif i == '*':
                n2 = numbers.pop()
                n1 = numbers.pop()
                numbers.append(n1 * n2)
            elif i == '/':
                n2 = numbers.pop()
                n1 = numbers.pop()
                if n1*n2 <0 and n1%n2 !=0:
                    numbers.append(n1/n2+1)
                else:
                    numbers.append(n1 / n2)
            else:
                numbers.append(int(i))
        return numbers[0]

