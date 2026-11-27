class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        char_set=set()
        left=0
        current_sum=0
        maximum_sum=0

        for right in range(len(nums)):
            while nums[right] in char_set:
                char_set.remove(nums[left])
                current_sum-=nums[left]
                left+=1
            char_set.add(nums[right])
            current_sum+=nums[right]

            if right-left+1>k:
                char_set.remove(nums[left])
                current_sum-=nums[left]
                left+=1

            if right-left+1==k:
                maximum_sum=max(maximum_sum,current_sum)

        return maximum_sum
