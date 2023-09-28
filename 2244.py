class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        result = 0
        for f in freq:
            # examples of tasks completed per round:
            # 1 => impossible, 2 => 2, 3 => 3, 4 => 2+2, 5 => 3+2,
            # 6 => 3+3, 7 => 3+2+2, 8 => 3+3+2, 9 => 3+3+3, ...
            if freq[f] == 1:
                return -1
            result += ceil(freq[f] / 3)

        return result
