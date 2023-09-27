class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        divisible = [ False ] * len(nums)
        for i, n in enumerate(nums):
            divisible[i] = n % p == 0

        all = set()
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if divisible[j]:
                    count += 1
                    if count > k:
                        break

                all.add(hash(tuple(nums[i:j+1])))
                # hoping that there are no hash collisions ...
                # otherwise just remove hash() and store the tuple which costs more memory

        return len(all)
