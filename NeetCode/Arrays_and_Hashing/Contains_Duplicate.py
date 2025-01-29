"""Given an integer array nums, return true if any value appears more than once
in the array, otherwise return false."""


class Solution:
    def hasDuplicate1(self, nums: list[int]) -> bool:
        """1 способ.
         
        Используется словарь с количеством повторений.
        Временная сложность: O(n).
        """
        countRepeat: dict = {}
        for i in nums:
            if i in countRepeat:
                countRepeat[i] += 1
            else:
                countRepeat[i] = 1

            if countRepeat[i] == 2:
                return True
        return False

    def hasDuplicate2(self, nums: list[int]) -> bool:
        """2 способ.

        Сравнивается количество уникальных элементов в множестве с общим
        количеством элементов.
        Временная сложность: O(n).
        """
        return len(set(nums)) < len(nums)


def main():     
    """Тестирование решения."""
    
    sol = Solution()
    print("Решение 1: ", sol.hasDuplicate2([1, 2, 3, 3]))
    print("Решение 2: ", sol.hasDuplicate2([1, 2, 3, 3]))


if __name__ == "__main__":
    main()
