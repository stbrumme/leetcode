class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = {}
        count["a"] = 1
        count["e"] = 1
        count["i"] = 1
        count["o"] = 1
        count["u"] = 1

        for _ in range(1, n):
            next = {}
            next["a"] = count["e"] + count["i"] + count["u"]
            next["e"] = count["a"] + count["i"]
            next["i"] = count["e"] + count["o"]
            next["o"] = count["i"]
            next["u"] = count["i"] + count["o"]
            count = next

        return sum(count.values()) % 1_000_000_007
