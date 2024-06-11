class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Python can handle large integers

        # from negabinary to decimal
        def decimal(arr):
            value = 0
            power = 1 # -2 ^ 0
            for a in reversed(arr):
                if a == 1:
                    value += power
                power *= -2
            return value

        # add in decimal system
        value = decimal(arr1) + decimal(arr2)

        # edge case
        if value == 0:
            return [ 0 ]

        # form decimal to negabinary
        result = []
        while value != 0:
            value, remainder = divmod(value, -2)
            if remainder == -1:
                # carry
                value    += 1
                result.append(1)
            else:
                result.append(remainder)

        return reversed(result)
