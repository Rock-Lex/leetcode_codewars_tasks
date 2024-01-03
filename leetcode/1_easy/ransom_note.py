"""
Type: Easy
383. Ransom Note
https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
"""
from collections import Counter


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True


class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False


class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        letters = {}
        for elRansomNote, elMagazine in zip(ransomNote, magazine):
            num_in_letters = letters.get(elRansomNote)
            if num_in_letters is None:
                if elRansomNote in magazine:
                    num_el_in_magazine = magazine.count(elRansomNote)
                    letters[elRansomNote] = num_el_in_magazine - 1
                else:
                    return False
            else:
                if num_in_letters == 0:
                    return False
                else:
                    letters[elRansomNote] = num_in_letters - 1
        return True


if __name__ == '__main__':
    sol = Solution1()

    print(sol.canConstruct("aa", "ab"))