class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        ham = list(hamsters)
        if len(ham) == 1:
            return 0 if ham[0] == "." else -1

        # "." = empty
        # "H" = hamster
        # "D" = donut

        # left end
        if ham[0] == "H":
            if ham[1] == "H":
                return -1
            ham[1] = "D"

        # right end
        if ham[-1] == "H":
            if ham[-2] == "H":
                return -1
            ham[-2] = "D"

        # everything else
        for i in range(1, len(ham) - 1):
            # look for hamsters
            if ham[i] != "H":
                continue

            if ham[i - 1] == "D" or ham[i + 1] == "D":
                # already fed
                continue

            # try to place donut on right side
            if ham[i + 1] == ".":
                ham[i + 1] = "D"
                continue

            # must place on left side
            if ham[i - 1] == "H":
                return -1
            ham[i - 1] = "D"

        return sum(1 for h in ham if h == "D")
