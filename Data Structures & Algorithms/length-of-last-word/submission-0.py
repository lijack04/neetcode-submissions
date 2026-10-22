class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) -1, -1, -1):
            if count == 0 and not s[i].isalpha():
                continue 
            if s[i] == " ":
                break
            count += 1
                
        
        return count
