class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        # two digits: both must be identical => divisible by 11
        for n in range(11, 99 + 1, 11):
            if low <= n <= high:
                result += 1
        if high < 1000:
            return result

        # create every two-digit number, group by its sum
        two = defaultdict(list)
        for i in range(10):
            for j in range(10):
                two[i + j].append(i * 10 + j)

        # create every combination of those two digits
        for same in two:
            for a in two[same]:
                if a * 100 > high:
                    break
                if a > 9: # no leading zero
                    for b in two[same]:
                        x = a * 100 + b
                        if low <= x <= high:
                            result += 1

        return result
