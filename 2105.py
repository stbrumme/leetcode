class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refills = 0

        left  = 0               # Alice's position
        right = len(plants) - 1 # Bob's   position
        alice = capacityA       # Alice's water
        bob   = capacityB       # Bob's   water

        while left < right:
            # Alice
            if alice < plants[left]:
                refills += 1
                alice    = capacityA
            alice -= plants[left]
            left += 1

            # Bob
            if bob < plants[right]:
                refills += 1
                bob      = capacityB
            bob -= plants[right]
            right -= 1

        # meet at the same plant
        if left == right:
            if max(alice, bob) < plants[left]:
                refills += 1

        return refills
