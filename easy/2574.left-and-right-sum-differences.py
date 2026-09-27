# @leet start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix: list[int] = [0]
        for i in range(len(nums) - 1):
            prefix.append(prefix[i] + nums[i])

        suffix = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        result = []
        for i in range(len(prefix)):
            result.append(abs(suffix[i] - prefix[i]))

        return result


# @leet end
