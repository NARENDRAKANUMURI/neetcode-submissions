class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_position=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert_position]=nums[i]
                insert_position+=1
        for i in range(insert_position,len(nums)):
            nums[i]=0
        return nums
        