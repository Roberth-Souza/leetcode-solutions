# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0
        current_water = 0

        while left < right:
            left_column = height[left]
            right_column = height[right]

            mini = min(left_column, right_column)

            current_water = (right - left) * mini
            best = max(current_water, best)

            if left_column < right_column:
                left += 1
            else:
                right -= 1
        return best


# @leet end
