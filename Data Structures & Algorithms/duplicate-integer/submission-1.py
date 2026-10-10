class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i = i + 1
        return False