class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = []
        
        for i in range(len(nums)-1) :
          
          if((target-nums[i]) in nums):

            if(nums.count(target-nums[i]) == 2):
               return [l for l, x in enumerate(nums) if x == (target-nums[i])]

            if ( nums.index(target-nums[i]) != i): 
              ids.append(i)
              ids.append(nums.index(target-nums[i]))
              return ids  