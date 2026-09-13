# @leet start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        for i in range(len(nums)):
            if not prefix:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] + prefix[i - 1])

        suffix = [0] * (len(nums))
        suffix[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] + suffix[i + 1]

        for i in range(len(prefix)):
            if prefix[i] == suffix[i]:
                return i
        return -1


# @leet end
