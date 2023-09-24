class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        have = set()

        def deeper(code):
            result = ""
            for i in range(k):
                next = code[1:] + str(i)
                if next not in have:
                    have.add(next)
                    result += deeper(next)
                    result += str(i)
            return result

        initial = "0" * n
        return deeper(initial) + initial[1:]