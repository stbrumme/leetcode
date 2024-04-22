class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        result = 0

        one = two = -1 # positions of the most recent elements

        intervals.sort(key = lambda x : ( x[1], -x[0] ))
        for start, end in intervals:
            if one >= start:
                continue
            if two >= start:
                one = two
                two = end
                result += 1
            else:
                one = end - 1
                two = end
                result += 2

        return result
