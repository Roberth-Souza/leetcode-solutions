# @leet start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        First: What did i understand of the problem :
        No element in the array can repeat the same amout of times
        if they do so, i need to return False

        the solution is to use a dictionary where the key is the number
        and the value is the count of this number. At the end we just use dict.values()
        which do not iterate in the hash map, and pass all those values to a set()

        The solution is to use 2 data structures as follow :
        """

        count = {}
        for e in arr:
            count[e] = (
                count.get(e, 0) + 1
            )  # the second parameter to the count is the default value
            # so if the dict does not have the key, 0 will be the default
            # if we would not use get() here, we would have a key error

        return (len(set(count.values()))) == len(count)


# WHAT WE LEARN HERE THE MATTERS THE MOST:
"""
I was afraid of doing 2 loops, but this is not a problem, 2 nested loops is
if 2 loops are not nested , the solution still is o(n)
"""

# @leet end
