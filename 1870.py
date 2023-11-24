class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def time(speed):
            result = 0
            for d in dist:
                result = ceil(result) + d / speed
            return result

        left  = 1
        right = 10**7
        # impossible
        if time(right) > hour:
            return - 1

        while left != right:
            mid = (left + right) // 2
            if time(mid) > hour:
                left  = mid + 1
            else:
                right = mid

        return left
