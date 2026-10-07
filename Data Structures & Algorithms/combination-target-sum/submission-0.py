class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, end, difference):
            if difference == 0:
                result.append(end.copy())
                return
            
            if difference < 0:
                return
            
            for i in range(start, len(nums)):
                end.append(nums[i])
                backtrack(i, end, difference-nums[i] )
                end.pop()
            
        backtrack(0, [], target)
        return result
        