"""
Type: Easy
290. Word Pattern
https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
"""

class ShortSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return map(pattern.find, pattern) == map(words.index, words)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        vocabulary = {}
        index = 0
        for word in words:
            if word not in vocabulary:
                if pattern[index] in vocabulary.values():
                    return False
                vocabulary[word] = pattern[index]
            elif word in vocabulary and vocabulary[word] != pattern[index]:
                return False
            index += 1
        return True


class LowLevelSolution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        vocabulary = {}
        pattern_index = 0
        word_cache = ""
        for index, char in enumerate(s):
            if pattern_index >= len(pattern): return False
            if char != " ":
                word_cache += char
                if index != len(s) - 1:
                    continue
            if word_cache not in vocabulary:
                if pattern[pattern_index] in vocabulary.values():
                    return False
                vocabulary[word_cache] = pattern[pattern_index]
            elif word_cache in vocabulary and vocabulary[word_cache] != pattern[pattern_index]:
                return False
            word_cache = ""
            pattern_index += 1
        if pattern_index != len(pattern): return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"

    sol = ShortSolution()
    print(sol.wordPattern(pattern, s))