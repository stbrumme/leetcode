class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for where, what in enumerate(nums):
            self.pos[what].append(where)

    def pick(self, target: int) -> int:
        return choice(self.pos[target])
