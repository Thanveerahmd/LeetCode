class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
          if len(nums) == 0 or len(nums) == 1:
            return len(nums)

          loopcount = len(nums)
          i = 0

          while i+1 < loopcount:

              while nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                
                if i+1 == len(nums):
                    break

                if len(nums) == 0 or len(nums) == 1:
                  break

              loopcount = len(nums)
              i += 1

          return len(nums)