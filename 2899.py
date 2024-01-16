class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        stack = []
        k = 0
        for w in words:
            if w == "prev":
                k += 1
                yield stack[-k] if k <= len(stack) else -1
            else:
                k = 0
                stack.append(int(w))
