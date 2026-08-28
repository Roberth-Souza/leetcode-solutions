# @leet start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        This is a 2 pointers problem, but i don't remember how to do this hehe
        The first pointer is left, and iterates normally in the list , i guess
        i should +1 in it , and -1 on the right one so it go backwards. The
        right pointer should only move when it's hovering a 0, the left pointer should
        aways move, i should stop when left > right i think
        """

        # --- My first attempt: correct, but O(n^2) ---
        # Rotates each zero to the end with pop+append. `pop(left)` shifts every
        # remaining element one slot left, so a list full of zeros costs n shifts.
        #
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[right] == 0:
        #         right -= 1
        #     if nums[left] == 0:
        #         nums.append(nums.pop(left))
        #     if nums[left] != 0:
        #         left += 1

        # --- Canonical two pointers: O(n) time, O(1) space ---
        # Pass 1: pack every non-zero to the front, keeping relative order.
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Pass 2: everything from `write` on is leftover garbage -> zero it.
        for i in range(write, len(nums)):
            nums[i] = 0


# @leet end
