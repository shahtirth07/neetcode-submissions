class Solution:

    def __init__(self, w: List[int]):
        self.list = []
        total = 0
        for i in w:
            total+=i
            self.list.append(total)
        
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        left, right = 0, len(self.list) - 1
        while left < right:
            mid = (left + right) //2
            if self.list[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()