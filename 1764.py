class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # quick heuristic using prefix sum
        prefix = [ 0 ]
        for n in nums:
            prefix.append(prefix[-1] + n)

        sums = []
        for g in groups:
            sums.append(sum(g))

        def deeper(gi, ni): # group index, nums index
            if gi == len(groups):
                return True
            if ni >= len(nums):
                return False

            # check first character
            if groups[gi][0] != nums[ni]:
                return deeper(gi, ni + 1)
            last = ni + len(groups[gi]) - 1
            # check last character
            if last >= len(nums):
                return False
            if groups[gi][-1] != nums[last]:
                return deeper(gi, ni + 1)
            # check sum
            if sums[gi] != prefix[last + 1] - prefix[ni]:
                return deeper(gi, ni + 1)

            # now compare the arrays
            if nums[ni : last + 1] == groups[gi]:
                return deeper(gi + 1, last + 1)
            else:
                return deeper(gi, ni + 1)

        return deeper(0, 0)
