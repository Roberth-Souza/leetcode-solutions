# @leet start
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n == 1:
            return 1

        sumodd = n * n
        sumeven = n * (n + 1)

        while sumodd != 0:
            sumeven, sumodd = sumodd, (sumeven % sumodd)
        return sumeven


# @leet end
