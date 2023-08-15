lass Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.pop()

        size = 0
        while size < len(bits):
            size += 1 + bits[size]

        return size == len(bits)
