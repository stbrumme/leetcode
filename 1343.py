class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0

        need = threshold * k
        have = sum(arr[:k - 1])
        for i in range(k - 1, len(arr)):
            have += arr[i]
            if have >= need:
                result += 1
            have -= arr[i - k + 1]

        return result
