class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        size = len(message)

        thresholds = ( 0, 10, 100, 1000, 10000, 100000 )

        # True if message can be split in "count" parts
        def possible(count):
            suffix = 3 + len(str(count)) # len("</count>")
            done   = 0

            # hacky way to speed up the slow brute force
            # I'm too tired to come up with an adequate formula ...
            while 1200 < count < 10000:
                done  += 100 * (limit - (suffix + 4))
                count -= 100

            # slow brute force
            digits = 1
            for i in range(1, count + 1):
                if i in ( 10, 100, 1000, 10000 ):
                    digits += 1
                done += limit - (suffix + digits)
                if done >= size: # early exit
                    return True

            return False

        # basic binary search doesn't work for some inputs:
        # "abbababbbaaa aabaa a" can be split in 7,8,9 parts, but not 10, then again in 11,12,13,...
        # therefore perform multiple binary searches among all 1-digit, 2-digit, 3-digit, ... values
        for first, last in zip(thresholds, thresholds[1 : ]):
            best = first + bisect_left(range(first, last), True, key = possible)
            if best < last:
                # create output
                for i in range(1, best + 1):
                    suffix = "<" + str(i) + "/" + str(best) + ">"
                    output = limit - len(suffix)
                    yield message[ : output] + suffix
                    message = message[output : ]
                return

        # impossible
        return []
