class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        buttons = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}
        
        def backtrack(i, comb):
            if len(comb) == len(digits):
                answer.append(comb)
                return
            
            for letter in buttons[digits[i]]:
                backtrack(i + 1, comb + letter)
        
        if digits:
            backtrack(0, "")
        
        return answer