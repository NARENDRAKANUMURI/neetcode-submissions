class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            text1,text2=text2,text1
        m=len(text1)
        n=len(text2)
        nextRow=[0]*(n+1)
        for i in range(m-1,-1,-1):
            curr=[0]*(n+1)
            for j in range(n-1,-1,-1):
                if text1[i]==text2[j]:
                    curr[j]=1+nextRow[j+1]
                else:
                    curr[j]=max(nextRow[j],curr[j+1])
            nextRow=curr
        return nextRow[0]