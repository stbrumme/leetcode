class Solution:
    def minAnagramLength(self, s: str) -> int:
        size = len(s)

        # find factors of size
        candidates = [ 1 ]
        for factor in range(2, size):
            if factor * factor > size:
                break

            one, two = divmod(size, factor)
            if two == 0:
                candidates.append(factor)
                candidates.append(one)

        # chop into pieces, each must have the same histogram
        for result in sorted(candidates):
            # initial chunk
            need = sorted(s[ : result])

            # subsequent chunks
            if all(sorted(s[chunk : chunk + result]) == need for chunk in range(result, size, result)):
                return result

        # no chunks, just the whole string
        return size
