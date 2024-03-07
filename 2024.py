class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0

        # truly maximized confusion is achieved by using weird bit operations
        # to solve this problem:
        # bin(ord("T")) = 0b1010100
        # bin(ord("F")) = 0b1000110
        # => let's abuse the lowest two bits of the ASCII code of "T" and "F"

        # sliding windows for the win
        left = 0
        have = [ -k, 99999, -k ] # only index 0 and 2 are needed
        for right in range(len(answerKey)):
            have[ord(answerKey[right]) & 2] += 1

            # avoid too much confusion
            while min(have) > 0:
                have[ord(answerKey[left]) & 2] -= 1
                left += 1

            result = max(result, right - left) # I should add 1, but defer that operation to the end

        return result + 1
