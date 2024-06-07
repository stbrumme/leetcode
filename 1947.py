class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        result    = 0
        size      = len(students)
        questions = len(students[0])

        # convert arrays to bitmasks
        for i in range(size):
            mask = 0
            for s in students[i]:
                mask <<= 1
                mask  |= s
            students[i] = mask

            mask = 0
            for m in mentors[i]:
                mask <<= 1
                mask  |= m
            mentors[i] = mask

        for p in permutations(students):
            score = 0
            for s, m in zip(p, mentors):
                different = (s ^ m).bit_count()
                score += questions - different

            result = max(result, score)

        return result
