class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        current_max_product=nums[0]
        current_min_product=nums[0]
        answer=nums[0]
        for i in range(1,n):
            num=nums[i]
            temp_max=max(num,num*current_max_product,num*current_min_product)
            temp_min=min(num,num*current_max_product,num*current_min_product)

            current_max_product=temp_max
            current_min_product=temp_min
            answer=max(answer,current_max_product)
        return answer