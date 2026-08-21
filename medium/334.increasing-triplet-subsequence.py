# @leet start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        I am first thinking of storing the values on 3 variables
        num1, num2, num3
        num1 should aways be the smaller value on the list

        i just need to check if i can find 3 ordened values anywhere on the list
        and they do not need to appear next to eachother
        """

        smaller = nums[0]
        middle = None
        bigger = None

        for number in nums:
            if bigger is not None:
                break

            elif number < smaller:
                smaller = number

            elif middle is not None and (number > middle and middle > smaller):
                bigger = number

            elif number > smaller:
                middle = number

        return bigger is not None

    # o(n) time complexity
    # o(1) memory


# @leet end
