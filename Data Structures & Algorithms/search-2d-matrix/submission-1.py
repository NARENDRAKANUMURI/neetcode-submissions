class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows-1
        while start<=end:
            row=(start+end)//2
            if target>matrix[row][-1]:
                start=row+1
            elif target<matrix[row][0]:
                end=row-1
            else:
                break
        if not (start<=end):
            return False
        row=(start+end)//2
        l,r=0,cols-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True
        return False



        

