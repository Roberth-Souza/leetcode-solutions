# @leet start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result = 0
        for e in hours:
            if e >= target:
                result += 1
        return result


# @leet end
