# @leet start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # So the formula for mdc according to euclides is :
        # a, b = b, a % b ( while b != 0 )
        # first i will try to find the pattern

        # but to do this, i need the len(gcd) of both the str:
        l1 = len(str1)
        l2 = len(str2)

        if l1 < l2:
            minor_str, bigger_str = str1, str2
        else:
            minor_str, bigger_str = str2, str1

        while l2 != 0:
            l1, l2 = l2, l1 % l2

        # l1 it's the gcd
        # now i need to find the pattern

        pattern = minor_str[:l1]
        # the pattern should be the gcd of the minorstr
        # Now that we have the pattern, i just need to
        # check if the pattern repeat in both of the str

        if len(bigger_str) % len(pattern) == 0 and (
            pattern * (len(bigger_str) // len(pattern)) == bigger_str
            and pattern * (len(minor_str) // len(pattern)) == minor_str
        ):
            return pattern
        else:
            return ""


# @leet end
