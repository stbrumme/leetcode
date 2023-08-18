class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        # see C++ std::random_shuffle
        result = self.nums.copy()
        size = len(result)
        for i in range(size - 1, 0, -1):
            pos = randint(0, i)
            result[i], result[pos] = result[pos], result[i]

        return result
