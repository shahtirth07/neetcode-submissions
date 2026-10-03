class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        biggest_small = -heapq.heappop(self.small)
        heapq.heappush(self.big, biggest_small)

        if len(self.big) > len(self.small):
            smallest_large = heapq.heappop(self.big)
            heapq.heappush(self.small, -smallest_large)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        return (-self.small[0] + self.big[0]) / 2
        