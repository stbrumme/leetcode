class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats   .sort()
        students.sort()
        result = 0
        for i, j in zip(seats, students):
            result += abs(i - j)
        return result
