# @leet start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum_average = float("-inf")
        left_window = 0
        right_window = 0
        current = 0

        while right_window <= len(nums) - 1:
            current += nums[right_window]
            if right_window >= k - 1:
                if current > maximum_average:
                    maximum_average = current
                current -= nums[left_window]
                left_window += 1
            right_window += 1

        return maximum_average / k


# @leet end
