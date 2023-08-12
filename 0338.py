class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            bits = 0

            # speed trick
            if i & 1:
                result.append(result[:1])
                continue

            value = i
            while value > 0:
                bits = bits + 1
                value = value & (value - 1)
            result.append(bits)

        return result
