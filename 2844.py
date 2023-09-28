class Solution:
    def minimumOperations(self, num: str) -> int:
        result = len(num) # deleting all digits makes num special

        # must end with 00, 25, 50 or 75

        # simplify counting
        num = num[::-1]

        zero = num.find("0")
        if zero >= 0:
            # delete everything but the zero
            result = min(result, len(num)-1)

            # look for 00
            zero2 = num.find("0", zero + 1)
            if zero2 >= 0:
                result = min(result, zero2 - 1)

            # look for 50
            five = num.find("5", zero + 1)
            if five >= 0:
                result = min(result, five - 1)

        five = num.find("5")
        if five >= 0:
            # look for 25
            two = num.find("2", five + 1)
            if two >= 0:
                result = min(result, two - 1)

            # look for 75
            seven = num.find("7", five + 1)
            if seven >= 0:
                result = min(result, seven - 1)

        return result
