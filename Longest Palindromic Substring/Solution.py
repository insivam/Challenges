class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = s[0]
        for c in range(len(s)):
            palindrome = s[c:]
            for last in range(len(palindrome), -1, -1):
                palindrome = palindrome[:last]
                if "".join(reversed(palindrome)) == palindrome and len(palindrome) > len(answer):
                    answer = palindrome
        return answer