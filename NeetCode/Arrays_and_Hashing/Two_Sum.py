"""Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j
that satisfy the condition.

Return the answer with the smaller index first."""


class Solution:
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        """1 способ.
        
        Перебор с помощью вложенных циклов.
        Временная сложность: O(n^2)
        Пространственная сложность: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


sol = Solution()
nums = [5, 5]
target = 10

print(sol.twoSum1(nums, target))
