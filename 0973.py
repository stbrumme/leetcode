class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [ ( x*x + y*y, x, y ) for x, y in points ]
        heapify(minheap) # tuples are sorted by first element (= squared distance)

        for _ in range(k):
            d2, x, y = heappop(minheap)
            yield (x, y)
