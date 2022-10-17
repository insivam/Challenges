class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answers = []
        for c in range(len(s)):
            answer = ""
            for i in s[c:]:
                if i in answer:
                    break
                answer += i
            answers.append(len(answer))
        
        return max(answers, 0)