class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        result = +inf

        # infinite generator of palindromes
        def generate():
            # skip 0, otherwise yield 0

            for digits in count(1):
                # length of left half
                half = (digits + 1) // 2
                initial = 10 ** (half - 1)

                for i in range(initial, initial * 10):
                    # left and right half
                    one = str(i)
                    two = one[::-1]
                    if digits & 1:
                        yield int(one + two[1 :])
                    else:
                        yield int(one + two)

        total = sum(nums)
        size  = len(nums)

        nums.sort()
        median = nums[size // 2]

        # locate the average
        smaller     = []
        palindromes = generate()
        for i in palindromes:
            smaller.append(i)
            if i > median:
                break

        # compute cost of palindromes smaller than the average
        for i in smaller[::-1]:
            cost   = sum(abs(n - i) for n in nums)
            if cost > result:
                break
            result = cost

        # compute cost of palindromes larger than the average
        for i in chain(palindromes):
            cost   = sum(abs(n - i) for n in nums)
            if cost > result:
                break
            result = cost

        return result
