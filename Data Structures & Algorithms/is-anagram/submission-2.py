class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        for char in t:
            if char not in char_counts:
                return False
            else:
                char_counts[char] -= 1
                if char_counts[char] < 0:
                    return False
        
        return True