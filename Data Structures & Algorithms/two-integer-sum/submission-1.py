class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            remaining=target-num
            if remaining in hashmap:
                return [hashmap[remaining],i]
            hashmap[num]=i