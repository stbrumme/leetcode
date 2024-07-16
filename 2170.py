class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        size = len(nums)

        # count numbers at odd and even positions
        freq = [ defaultdict(int), defaultdict(int) ]
        for i, n in enumerate(nums):
            freq[i & 1][n] += 1

        even = sorted( [ ( count, value ) for value, count in freq[0].items() ], reverse = True )
        odd  = sorted( [ ( count, value ) for value, count in freq[1].items() ], reverse = True )

        # avoid edge cases
        while len(even) < 2:
            even += [ ( 0, 0 ) ]
        while len(odd)  < 2:
            odd  += [ ( 0, 0 ) ]

        # keep the most frequent odd and even numbers, change everything else
        keepEven = even[0][0]
        keepOdd  = odd[0][0]

        # but if they share the same value, keep the most most most frequent and the second most frequent ;-)
        if even[0][1] == odd[0][1]:
            if keepEven + odd[1][0] > keepOdd + even[1][0]:
                keepOdd  = odd[1][0]
            else:
                keepEven = even[1][0]

        return size - (keepEven + keepOdd)
