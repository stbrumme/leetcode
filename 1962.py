class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # always apply the operation to the largest pile => max-heap
        todo = [ -p for p in piles ] # create max-heap using a min-heap with negated values
        heapify(todo)
        for _ in range(k):
            top  = -todo[0]
            top -= top // 2
            heappushpop(todo, -top)

        return -sum(todo)
