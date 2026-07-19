class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstOccurance(nums,target):
            start,end=0,len(nums)-1
            result=-1
            while start<=end:
                mid=(start+end)//2
                if target>nums[mid]:
                    start=mid+1
                elif target<nums[mid]:
                    end=mid-1
                else:
                    result=mid
                    end=mid-1
            return result
        def secondOccurance(nums,target):
            start,end,result=0,len(nums)-1,-1
            while start<=end:
                mid=(start+end)//2
                if target>nums[mid]:
                    start=mid+1
                elif target<nums[mid]:
                    end=mid-1
                else:
                    result=mid
                    start=mid+1
            return result
        return [firstOccurance(nums,target),secondOccurance(nums,target)]
