class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [ 0 ] * 40
        # brute force
        for i in range(1, n + 1):
            digitsum = 0
            ii = i
            while ii > 0:
                digitsum += ii % 10
                ii      //= 10
            count[digitsum] += 1

        high = max(count)
        return sum(1 if c == high else 0 for c in count)
