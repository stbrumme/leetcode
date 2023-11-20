class Solution:
    def fillCups(self, amount: List[int]) -> int:
        result = 0
        while sum(amount) > 0:
            amount.sort()

            if amount[0] == 0:
                # fill amount[2], try to fill amount[1] as well
                result += amount[2]
                break

            # fill the two cups we need to most
            twothree   = amount[1] - amount[0] + 1
            amount[1] -= twothree
            amount[2] -= twothree
            result    += twothree

        return result
