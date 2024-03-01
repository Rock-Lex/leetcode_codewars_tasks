"""
Type: Medium
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_words = words[-1]
        for el in reversed(words[:-1]):
            reverse_words += " " + el
        return reverse_words


class Solution2:
    def reverseWords(self, s: str) -> str:
        word_started = False
        word_cache = " "
        reverse_words = ""

        for char in s[::-1]:
            if char != " ":
                word_started = True
                word_cache = char + word_cache
            else:
                if word_started:
                    word_started = False
                    reverse_words += word_cache
                    word_cache = " "

        if word_cache != " ":
            reverse_words += word_cache

        return reverse_words[:-1]


if __name__ == '__main__':
    s = "the sky is blue"
    sol = Solution2()
    print(sol.reverseWords(s) + "-")