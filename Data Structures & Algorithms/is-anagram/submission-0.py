class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result=sorted(s)
        result1=sorted(t)
        if result==result1:
            return True
        else:
            return False