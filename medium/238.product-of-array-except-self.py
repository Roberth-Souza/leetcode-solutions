# @leet start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        for i in range(len(nums)):
            prefix.append(nums[i] * prefix[i])

        suffix = [0] * len(nums)
        suffix.append(1)

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i + 1])

        return result


# @leet end
