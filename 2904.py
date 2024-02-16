class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # brute force
        # a sliding window might be faster
        size    = len(s)
        invalid = "9" * size
        result  = invalid

        # too few 1s
        if s.count("1") < k:
            return ""

        for left in range(size):
            # must start (and end) with "1"
            if s[left] != "1":
                continue

            for right in range(left + k - 1, size): # need at least k digits
                length = right - left + 1
                if length > len(result):
                    break # current result is already shorter

                if s[right] != "1":
                    continue

                current = s[left : right + 1]
                ones    = current.count("1")
                if ones > k: # too many 1s
                    break
                if ones < k: # too few  1s
                    continue

                # ones == k
                if   length <  len(result): # shorter than before
                    result = current
                else: # length == len(result)
                    result = min(result, current)

        return result if result != invalid else ""
