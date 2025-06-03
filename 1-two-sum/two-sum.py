class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevList = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevList:   
                return [prevList[diff], i]
            prevList[n] = i
        return
        