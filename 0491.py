class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        todo = [ [ nums[0] ] ]
        for n in nums[1:]:
            next = todo + [ [ n ] ]
            for t in todo:
                longer = t + [ n ]
                if n >= t[-1] and longer not in next:
                    next.append(longer)
            todo = next

        return [ t for t in todo if len(t) >= 2 ]