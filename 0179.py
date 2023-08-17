class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        all = []
        for n in nums:
            all.append(str(n))

        # basic sort is good enough for vast majority of cases
        all.sort(reverse = True)

        # fixed misplaced pairs
        again = True
        while again:
            again = False
            for i in range(1, len(all)):
                if all[i - 1] + all[i] < all[i] + all[i - 1]:
                    all[i - 1], all[i] = all[i], all[i - 1]
                    again = True

        while len(all) > 1 and all[0] == "0":
            del all[0]

        return "".join(all)
