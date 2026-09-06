# @leet start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = max(candies)
        return [True if e + extraCandies >= i else False for e in candies]


# @leet end
