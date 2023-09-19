class Solution:
    def lengthLongestPath(self, input: str) -> int:
        best = 0
        tabs = [ 0 ]
        for line in input.split("\n"):
            tabs = tabs[:line.count("\t") + 1]
            length = len(line) - line.count("\t") + tabs[-1]
            if line.count(".") > 0:
                best = max(best, length) # file
            else:
                tabs.append(length + 1)  # directory

        return best