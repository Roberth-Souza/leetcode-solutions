# @leet start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]

        output = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= right:
                output += 1
            right -= nums[i + 1]

        return output


# @leet end
