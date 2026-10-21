class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums) - 1
        # res = nums[0]
        minimum = nums[0]
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                minimum = nums[i]
        return minimum