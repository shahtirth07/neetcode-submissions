class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[q] = nums[i]
                q +=1

        return q