# @leet start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
Solved by using binary search, i guess it's an o(log n)

AI comeup with this solution after i solved it :

guess_lower, guess_higher = 1, n

# this stops when the interval of guess_lower/guess_higher is empty
while guess_lower <= guess_higher:
    number = (guess_lower + guess_higher) // 2
    result = guess(number)
    if result == 0:
        break
    elif result == 1:
        guess_lower = number + 1   # exclui number
    else:
        guess_higher = number - 1  # exclui number

my code works only because of the leetcode constraint, but there is a bug:

my code updtates the limit ( num higher & num lower ) to the number that
just failed, this should not happen, if the number is lower i should search from num + 1
if it's higher from num - 1; my code has a infinite loop potential, if higher - lower == 1

higher = 4
lower = 3
7 // 2 =
3
lower = 3
higher = 4

repeat ....
i also did not see that n = num higher, wich means i did not have to use the 2 ** 32 at all

"""


class Solution:
    def guessNumber(self, n: int) -> int:
        guess_lower = 1
        guess_higher = 2**32
        number = (guess_lower + guess_higher) // 2
        result = guess(number)
        while result != 0:
            if result == -1:
                guess_higher = number
                number = (guess_lower + guess_higher) // 2
                result = guess(number)
            else:
                guess_lower = number
                number = (guess_lower + guess_higher) // 2
                result = guess(number)
        return number


# @leet end
