class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # take only cards from the left side
        result = sum(cardPoints[:k])
        left   = k - 1
        right  = len(cardPoints) - 1
        have   = result
        while left >= 0:
            have  -= cardPoints[left]
            have  += cardPoints[right]
            result = max(result, have)

            left  -= 1
            right -= 1

        return result
