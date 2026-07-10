class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False] * n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if j-i<=2 or dp[i+1][j-1]:
                        dp[i][j]=True

        result=[]
        part=[]
        
        def dfs(start):
            if start==n:
                result.append(part.copy())
                return

            for end in range(start,n):
                if dp[start][end]:
                    part.append(s[start:end+1])
                    dfs(end+1)
                    part.pop()
        dfs(0)
        return result
        