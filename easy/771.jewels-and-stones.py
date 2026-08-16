# @leet start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for e in stones:
            if e in set(jewels):
                count += 1
        return count


# @leet end
