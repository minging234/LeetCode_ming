

def isValid(s):
    stack = []

    for i in s:
        if i == ")":
            if stack.pop() != "(":
                return False
        elif i == "]":
            if stack.pop() != "[":
                return False
        elif i == "}":
            if stack.pop() != "{":
                return False
        else:
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False

s = ["{","}"]
print(isValid(s))


class Solution(object):
    def isValid(self, s):
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []