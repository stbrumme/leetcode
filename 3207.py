class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # pick the weakest and fight against it to get first point
        fight = min(enemyEnergies)
        if fight <= currentEnergy:
            currentEnergy -= fight
            # mark all enemies (except the weakest), farm their energy
            # and then fight against the weakest as often as possible
            return (currentEnergy + sum(enemyEnergies)) // fight
        else:
            # impossible, too little energy to fight even the weakest enemy
            return 0
