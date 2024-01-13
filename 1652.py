class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        size  = len(code)
        delta = +1 if k > 0 else -1
        for i in range(size):
            have = 0
            # if k == 0 then no iterations
            for j in range(1, abs(k) + 1):
                pos = (i + j * delta) % size
                have += code[pos]

            yield have
