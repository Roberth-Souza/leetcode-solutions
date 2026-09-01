# @leet start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This seems a lot like twoSum, but the array is sorted, and we also need to add plus 1
        to the indexes before returning...

        """

        left = 0
        right = len(numbers) - 1
        while left < right:
            resultado = numbers[left] + numbers[right]
            if resultado == target:
                break
            if resultado < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]


# @leet end
