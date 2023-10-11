class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # not the most efficient approach ...
        give = [ 0 ] * children

        # give each one dollar
        for i in range(children):
            give[i]  = 1
            money   -= 1

        # rule 2 violated
        if money < 0:
            return -1

        # give 7 dollars as often as possible (one was already given => now they have 8 dollars)
        for i in range(children):
            if money < 8 - 1:
                break
            money   -= 8 - 1
            give[i] += 8 - 1

        # given anything left to the last child
        give[-1] += money   # obey  rule 1
        if (give[-1] == 4): # check rule 3
            give[-1] -= 1
            give[-2] += 1

        return sum([ 1 for g in give if g == 8 ])
