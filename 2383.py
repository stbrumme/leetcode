class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        currentEnergy = initialEnergy
        currentXP     = initialExperience

        needEnergy = 0
        needXP     = 0
        for e, x in zip(energy, experience):
            if currentEnergy <= e:
                diff = e - currentEnergy + 1
                needEnergy    += diff
                currentEnergy += diff # same as currentEnergy = e + 1

            if currentXP <= x:
                diff = x - currentXP + 1
                needXP    += diff
                currentXP += diff # same as currentXP = x + 1

            currentEnergy -= e
            currentXP     += x

        return needEnergy + needXP
