class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l = 0
        currCapacity=0
        while l<r:
            
            height = min(heights[l], heights[r])
            width = r-l
            maxCapacity = max(height * width, currCapacity)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            currCapacity = maxCapacity
        
        return currCapacity
