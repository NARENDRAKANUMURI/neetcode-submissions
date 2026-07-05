class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def dfs(start,curr,total):
            if total==target:
                result.append(curr.copy())
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,curr,total+candidates[i])
                curr.pop()
        dfs(0,[],0)
        return result