class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # removing at the end is much faster
        popped.reverse()

        s = []
        for p in pushed:
            # add one element and try to remove as many as possible
            s.append(p)
            while s and s[-1] == popped[-1]:
                s.pop()
                popped.pop()

        return not popped
