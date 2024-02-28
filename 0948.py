class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = 0

        tokens.sort()
        score = 0
        left  = 0
        right = len(tokens) - 1
        while left <= right:
            # smallest token: face-up
            if tokens[left] <= power:
                power -= tokens[left]
                left  += 1
                score += 1
                result = max(result, score)
                continue

            # largest token: face-down
            if score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
                continue

            break # no token possible

        return result
