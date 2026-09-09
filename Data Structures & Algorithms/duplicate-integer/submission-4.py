class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set()
        for num in range(len(nums)):
            if nums[num] in lst:
                return True
            else:
                lst.add(nums[num])
            
        return False

