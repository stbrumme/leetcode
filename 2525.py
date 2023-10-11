class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky  = length >= 10**4
        bulky |= width  >= 10**4
        bulky |= height >= 10**4
        bulky |= (length * width * height) >= 10**9

        heavy  = mass >= 100

        if heavy and bulky:
            return "Both"
        if (not heavy) and (not bulky):
            return "Neither"
        if bulky and not heavy:
            return "Bulky"
        #if heavy and not bulky:
        return "Heavy"
