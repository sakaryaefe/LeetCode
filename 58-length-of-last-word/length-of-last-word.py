class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        words = s.strip().split()
        for _ in words:
            if not words:
                break
        return len(words[-1])   