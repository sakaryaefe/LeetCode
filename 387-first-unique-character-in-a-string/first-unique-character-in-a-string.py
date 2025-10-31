class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterToCount = collections.Counter(s)

        for idx, letter in enumerate(s):
            if letterToCount[letter] == 1:
                return idx
        
        return -1