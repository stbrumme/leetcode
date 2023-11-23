class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        waiting    = [ 0 ] * (delay  - 1) + [ 1 ]
        forgetting = [ 0 ] * (forget - 1) + [ 1 ]
        active     = 0
        modulo     = 1_000_000_007

        for _ in range(1, n):
            active += waiting   .pop(0) # new people can spread the secret
            active -= forgetting.pop(0) # they forget about it

            active %= modulo            # we could get away without this (and only modulo at the end)

            waiting   .append(active)   # each person tells the secret someone new
            forgetting.append(active)   # and they will forget it in a while

        return (active + sum(waiting)) % modulo
