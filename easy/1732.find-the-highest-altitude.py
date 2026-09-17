# @leet start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current_sum = 0
        best_sum = 0
        for i in range(len(gain)):
            current_sum += gain[i]
            if best_sum < current_sum:
                best_sum = current_sum

        return best_sum


# @leet end
