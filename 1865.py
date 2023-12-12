class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = sorted(nums1)
        self.nums2 = nums2

        self.n2 = defaultdict(int)
        for n in nums2:
            self.n2[n] += 1

    def add(self, index: int, val: int) -> None:
        self.n2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.n2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for one in self.nums1:
            if one > tot:
                break
            two = tot - one
            if two in self.n2:
                result += self.n2[two]
        return result
