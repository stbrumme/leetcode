class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        result = 0

        one = defaultdict(int)
        two = defaultdict(int)

        for x in arr:
            # triple
            k = x
            ij = target - k
            if ij in two:
                result += two[ij]

            # pair
            j = x
            for j in one:
                two[k + j] += one[j]

            # single
            i = x
            one[i] += 1

        return result % (10**9 + 7)
