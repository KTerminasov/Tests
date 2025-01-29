"""Given two strings s and t, return true if the two strings are anagrams
of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different."""


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        """1 способ.

        Сортировка строк и их сравнение.
        Временная сложность: O(nlogn + mlogm), где m и n - длины строк.
        """

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        return s_sorted == t_sorted

    def isAnagram2(self, s: str, t: str) -> bool:
        """2 способ.

        Подсчет количества уникальных повторений для каждой буквы английского алфавита.
        Временная сложность: O(n+m), где m и n - длины строк.
        Пространственная сложность: O(1), так как размер count всегда константен
        """

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


def main():
    solution = Solution()

    s, t = "racecar", "carrace"
    print(solution.isAnagram2(s, t))


if __name__ == "__main__":
    main()
