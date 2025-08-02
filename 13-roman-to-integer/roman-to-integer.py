class Solution:
    roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

    def romanToInt(self, s: str) -> int:
        num=0
        for i in range(len(s)):
            if i+1<len(s) and self.roman[s[i]]<self.roman[s[i+1]]:
                num-=self.roman[s[i]]    #some logic 
            else:
                num+=self.roman[s[i]]     #some logic
        return num
