class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        dic = { "(" : ")", "[" : "]", "{" : "}"}
        for i in s:
            if i in dic.keys():
                temp.append(i)
            else:
                if temp == [] or i != dic[temp[-1]]:
                    return False
                temp.pop()
        
        if temp != []:
            return False
        return True