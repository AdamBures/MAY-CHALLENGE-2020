class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] = counter[char] + 1
                
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
            
        return -1
