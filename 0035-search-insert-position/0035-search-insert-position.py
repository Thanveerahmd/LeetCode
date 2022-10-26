class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       low = 0
       high = len(nums) - 1
       mid = 0

       while low <= high:

            mid = (high + low) // 2

            # If target is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1

            # If target is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1

            # means xtarget is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
       return low