class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # let's say the middle digit belongs to left half
        right = intLength // 2
        left  = intLength - right

        # one-based queries
        zero = int("9" * (left - 1)) if left > 1 else 0
        for q in queries:
            result = str(zero + q)

            if len(result) == left:
                # apped right half
                result += result[: right][::-1]
                yield int(result)
                continue

            # invalid query
            yield -1
