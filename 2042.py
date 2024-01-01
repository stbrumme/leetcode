class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [ int(w) for w in s.split(" ") if w.isnumeric() ]
        return all(nums[i] > nums[i - 1] for i in range(1, len(nums)))
