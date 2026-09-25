# @leet start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_most = self.binary_search(nums, target, True)
        right_most = self.binary_search(nums, target, False)
        return [left_most, right_most]

    def binary_search(self, nums: list[int], target: int, left_bias: bool) -> int:
        low = 0
        high = len(nums) - 1
        idx = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                idx = mid
                if left_bias:
                    high = mid - 1
                else:
                    low = mid + 1
        return idx


# @leet end
