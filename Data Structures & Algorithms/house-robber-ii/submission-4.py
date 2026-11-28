class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def robLine(left,right):
            prev2=0
            prev1=0

            for i in range(left,right+1):
                current=max(prev1,prev2+nums[i])
                prev2=prev1
                prev1=current

            return prev1

        return max(robLine(0,len(nums)-2),robLine(1,len(nums)-1))