class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        answer = 0
        for c, i in enumerate(s):
            if i == "(":
                stack.append(c)
            else:
                stack.pop()
                if not stack:
                    stack.append(c)
                else:
                     answer = max(answer, c-stack[-1])
        return answer
