"""
Type: Easy
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
"""



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        is_started = False
        for char in reversed(s):
            if is_started:
                if char == " ":
                    break
                last_word_length += 1
            elif char != " ":
                is_started = True
                last_word_length += 1

        return last_word_length


if __name__ == '__main__':
    sol = Solution()
    sentence = "Hello word  "

    print(sol.lengthOfLastWord(sentence))