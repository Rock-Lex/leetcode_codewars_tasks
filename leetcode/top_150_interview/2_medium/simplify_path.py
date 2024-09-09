"""
Type: Medium
71. Simplify Path
https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List
from icecream import ic


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        output = []

        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if output:
                    output.pop(-1)
            else:
                output.append(path[i])

        path = "/".join(output)

        return "/" + path


class LongSolution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        buffer = ""
        dot_counter = 0

        for i in range(0, len(path) - 1):
            if path[i] == "/":
                dot_counter = 0
                if len(buffer) > 0:
                    stack.append(buffer)
                    buffer = ""
                if path[i + 1] == "/":
                    continue
            elif path[i] == "." and buffer == "":
                dot_counter += 1
                if path[i + 1] != ".":
                    if path[i + 1] != "/":
                        buffer += "." * dot_counter
                        dot_counter = 0
                    elif dot_counter == 2:
                        if len(stack) > 0:
                            stack.pop()
                        dot_counter = 0
                    elif dot_counter > 2:
                        stack.append("." * dot_counter)
                        dot_counter = 0
            else:
                buffer += path[i]
            if i == len(path) - 2:
                if path[i + 1] == ".":
                    dot_counter += 1
                    if buffer != "":
                        buffer += "."
                    elif dot_counter == 2:
                        if len(stack) > 0:
                            stack.pop()
                        dot_counter = 0
                    elif dot_counter > 2:
                        stack.append("." * dot_counter)
                        dot_counter = 0
                elif path[i + 1] != "/":
                    buffer += path[i + 1]

        answer = ""
        for el in stack:
            answer += f"/{el}"
        if len(buffer) > 0: answer += f"/{buffer}"
        if answer == "": answer = "/"
        return answer


path = "/..hidden"
sol = Solution()
ic(sol.simplifyPath(path))