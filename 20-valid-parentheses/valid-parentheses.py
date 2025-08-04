class Solution:
    def isValid(self, s: str) -> bool:
        stack_=list()
        mapping={')' : '(',']' : '[','}' : '{'}
        for char in s:
            if char not in mapping:
                stack_.append(char)
            else:
                if not stack_ or stack_[-1]!= mapping[char]:
                    return False 
                stack_.pop()
        return not stack_