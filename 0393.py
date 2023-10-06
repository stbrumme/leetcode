class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        for d in data:
            print(bin(d))

        pos = 0
        while pos < len(data):
            current = data[pos]
            pos += 1

            # ASCII
            mask = 1 << 7
            if current < mask:
                continue

            # multiple bytes per character
            need = 0
            # number of set high bits
            mask |= mask >> 1
            while current >= mask:
                need += 1
                mask |= mask >> 1
                if need > 3:
                    return False

            if need == 0:
                return False

            # collect 0b01...... bytes
            for _ in range(need):
                if pos == len(data):
                    return False

                current = data[pos]
                pos += 1

                # between 0b10...... and 0b11......
                if not ((1 << 7) <= current < (3 << 6)):
                    return False

        return True
