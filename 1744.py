class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # prefix sum
        prefix = []
        total  = 0
        for c in candiesCount:
            total += c
            prefix.append(total)

        for type, day, cap in queries:
            # least number of days needed to eat all lower ranked candies
            # eat as many candies as possible, respecting the cap
            low  = 0 if type == 0 else prefix[type - 1] // cap

            # highest number of days to eat all lower ranked candies plus the current candy type
            # eat just one candy daily
            high = prefix[type]

            yield low <= day < high
