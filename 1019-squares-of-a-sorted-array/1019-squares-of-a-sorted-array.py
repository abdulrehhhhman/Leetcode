class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        left=0
        right=n-1
        pos=n-1
        arr=[0]*n
        while left<=right:
            left_sq=nums[left]*nums[left]
            right_sq=nums[right]*nums[right]
            if left_sq > right_sq:
                arr[pos]=left_sq
                left+=1
            else:
                arr[pos]=right_sq
                right-=1
            pos-=1
        return arr      

            
            
        