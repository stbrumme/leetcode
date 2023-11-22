class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = []
        for a, b in zip(reward1, reward2):
            heappush(diffs, ( -(a - b), a, b )) # max-heap, negate sign

        one = two = 0
        # mouse 1 eats relatively expensive cheese
        for _ in range(k):
            d, a, b = heappop(diffs)
            one += a

        # mouse 2 eats anything else
        while diffs:
            d, a, b = heappop(diffs)
            two += b

        return one + two
