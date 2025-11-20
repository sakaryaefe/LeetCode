class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) 
# sets are used for removing the duplicates in a list and & are finding the union
