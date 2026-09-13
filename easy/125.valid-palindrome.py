# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left <= right:
            a: str = s[left].lower()
            b: str = s[right].lower()
            if not a.isalnum():
                left += 1
                continue
            if not b.isalnum():
                right -= 1
                continue

            if a != b:
                return False
            left += 1
            right -= 1

        return True


# @leet end
