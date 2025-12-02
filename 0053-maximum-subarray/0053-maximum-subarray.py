class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # either add to current sum OR start new subarray
            current_sum = max(nums[i], current_sum + nums[i])
            
            # update global max
            max_sum = max(max_sum, current_sum)

        return max_sum
      
  
  #brute force 
  
# class Solution(object):
#     def maxSubArray(self, nums):
#         ans= -1021809389123801298
#         for i in range(len(nums)):
#             cur_sum=0
#             for j in range(i,len(nums)):
#                 cur_sum+=nums[j]
#                 ans=max(cur_sum,ans)
#         return ans        

