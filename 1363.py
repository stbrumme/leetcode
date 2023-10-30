class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # count digits
        digitsum = 0
        freq     = [ 0 ] * 10
        for d in digits:
            freq[d]  += 1
            digitsum += d

        error = digitsum % 3
        # remove one digit
        for i in range(1, 10):
            if error != 0 and i % 3 == error and freq[i] > 0:
                freq[i] -= 1
                error    = 0
                break

        # need to remove two digits
        if error != 0:
            for i in range(1, 10):
                # any small digits which are not multiples of three
                while freq[i] > 0 and i % 3 != 0 and error != 0:
                    freq[i] -= 1
                    error   -= i % 3
                    if error < 0:
                        error += 3

        result = ""
        if error == 0:
            for i in range(9, 0, -1):
                result += str(i) * freq[i]
            if freq[0] > 1 and not result:
                return "0" # not multiple zeros
            result += "0" * freq[0]

        return result
