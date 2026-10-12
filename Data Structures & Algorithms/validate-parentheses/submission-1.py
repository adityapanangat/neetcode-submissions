class Solution:
    def isValid(self, s: str) -> bool:
        openingChars = "({["
        matches = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for char in s:
            if char in openingChars:
                stack.append(char)
            
            else:
                if stack == [] or char != matches[stack.pop()]:
                    return False
        
        return len(stack) == 0

        