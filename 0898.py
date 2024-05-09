class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all  = set()

        todo = set() # all ORed values up to the current position
        for a in arr:
            # extend with current value
            next = set(a | t for t in todo)
            next.add(a)

            all |= next
            todo = next

        return len(all)
