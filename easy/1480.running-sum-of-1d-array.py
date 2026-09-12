# @leet start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if not prefix:
                prefix.append(nums[0])
            else:
                prefix.append(nums[i] + prefix[i - 1])
        return prefix


# @leet end
