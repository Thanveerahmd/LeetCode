class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
          if len(nums) == 0 or val not in nums:
             return len(nums)

          while val in nums:
            nums.remove(val)

          return len(nums)