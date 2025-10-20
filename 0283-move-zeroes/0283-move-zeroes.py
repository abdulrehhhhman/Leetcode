class Solution(object):
    def moveZeroes(self, nums):
        arr_pos=0
        for i in nums:
            if i!=0:
                nums[arr_pos]=i
                arr_pos +=1
        while arr_pos<len(nums):
            nums[arr_pos]=0 
            arr_pos +=1   
        return nums        

        