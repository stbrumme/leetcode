class Solution:
    def within(self, left, right, pos):
        return left <= pos and pos <= right

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        longest = defaultdict(int)

        for i in intervals:
            left  = i[0]
            right = i[1]
            longest[left] = max(longest[left], right)

        again = True
        while again:
            start = sorted(longest.keys())

            again = False

            for a in range(len(start)):
                for b in range(a+1, len(longest)):
                    left  = start[a]
                    right = longest[left]
                    next  = start[b]
                    if not self.within(left, right, next):
                        break

                    if longest[next] > right:
                        longest[left] = longest[next]

                    del longest[next]
                    b -= 1
                    again = True
                if again:
                    break

        result = []
        for i in longest:
            result.append([ i, longest[i] ])
        return result
