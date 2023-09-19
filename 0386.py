class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def deeper(start):
            for i in range(start, start + 10):
                if 0 < i <= n:
                    yield i
                    yield from deeper(i * 10)

        yield from deeper(0)
