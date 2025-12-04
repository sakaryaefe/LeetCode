class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _binary_search(l, r, nums, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1
        def _search(l, r, nums, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[l] <= nums[mid]:
                    if nums[l] <= target <= nums[mid]:
                        return _binary_search(l, mid, nums, target)
                    else:
                        return _search(mid + 1, r, nums, target)
                else:
                    if nums[mid + 1] <= target <= nums[r]:
                        return _binary_search(mid + 1, r, nums, target)
                    else:
                        return _search(l, mid, nums, target)
            return -1
        return _search(0, len(nums) - 1, nums, target)
      