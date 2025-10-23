class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        kept = 0 
        n = len(nums)

        for i in range (n):
            if nums[i] != val:
                nums[kept] = nums[i]
                kept += 1 
        return kept 
                
            
