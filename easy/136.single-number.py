# @leet start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        This is a bit manipulation problem, but i dunno what that is
        so i will go for a hash map implementation first, than search
        bit manipulation after

        The plan is a dict where the key is the element, and the count the vallue
        """

        """
        hash = {}
        for e in nums:
            hash[e] = hash.get(e, 0) + 1

        for k, v in hash.items():
            if v == 1:
                return k
        
 ---------------------------

        a solution where we add a element to a set if it's the first time we see him
        else we remove him from the set:

        seen = set()
        for e in nums:
            if e in seen:
                seen.remove(e)
            else:
                seen.add(e)
        return seen.pop()   # only one left

        O(n)/O(n) time complexity
        O(n) space complexity

-------------------------------
        solved as this before knowing bit manipulation
        it got accepted but not with good time complexity
        i will search bit manipulation now.
        """

        a = 0
        for e in nums:
            a ^= e
        return a

        # This is o(1) space complexity !!!


# @leet end
