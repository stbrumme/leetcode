class Solution:
    def grayCode(self, n: int) -> List[int]:
        # https://en.wikipedia.org/wiki/Gray_code
        result = [ 0, 1 ]
        size = 1
        while size < n:
            mask = 2 ** size
            size += 1
            next = result
            for i in reversed(result):
                next.append(i + mask)

            result = next

        return result
