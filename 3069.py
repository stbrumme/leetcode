class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        one = [ nums[0] ]
        two = [ nums[1] ]

        for n in nums[2 :]:
            if one[-1] > two[-1]:
                one.append(n)
            else:
                two.append(n)

        return one + two
