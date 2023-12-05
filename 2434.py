class Solution:
    def robotWithString(self, s: str) -> str:
        result = ""

        # incoming characters
        wait = defaultdict(int)
        for c in s:
            wait[c] += 1
        wait["zz"] = 1 # stop marker

        t = []
        for c in s:
            # first operation
            t.append(c)
            wait[c] -= 1
            if wait[c] == 0:
                del wait[c]

            # copy to result if no smaller characters are still left in s
            while t and t[-1] <= min(wait):
                result += t.pop()

        return result
