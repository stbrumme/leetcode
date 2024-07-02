class Solution:
    def minimumChairs(self, s: str) -> int:
        result = 0
        inside = 0
        for c in s:
            if c == "E":
                inside += 1
                result  = max(result, inside)
            else:
                inside -= 1

        return result
