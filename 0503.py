lass Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)

        result = []
        for i in range(size):
            found = False
            for j in range(1, size):
                pos = (i + j) % size
                if nums[pos] > nums[i]:
                    result.append(nums[pos])
                    found = True
                    break

            if not found:
                result.append(-1)

        return result
