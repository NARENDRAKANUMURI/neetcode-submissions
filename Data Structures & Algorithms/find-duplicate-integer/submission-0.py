class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        for i in range(n):
            if nums[i] in seen:
                return nums[i]
                break
            else:
                seen.add(nums[i])