# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, number in enumerate(nums):
            complete = target - number
            if complete in seen:
                return seen[complete], index
            seen[number] = index
        return [0, 1]
