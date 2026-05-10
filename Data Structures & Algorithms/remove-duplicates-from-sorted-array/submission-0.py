class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        q=1
        for i in range(1, len(nums)):
            val = nums[i-1]
            if nums[i] != val:
                nums[q] = nums[i]
                q +=1

        return q