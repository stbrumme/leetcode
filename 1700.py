class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pick = 0 # last time someone got a matching sandwich
        while True:
            if pick >= len(students):
                break
            pick += 1

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                pick = 0
            else:
                s = students.pop(0)
                students.append(s)

        return len(students)
