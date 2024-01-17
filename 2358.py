class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # students should be sorted by their grades:
        # smaller groups have worse grades
        # start with groups of one student, then two students, then three ...
        groups = 0
        done   = 0 # students grouped so far
        while done < len(grades):
            remaining = len(grades) - done
            if remaining <= groups:
                break

            groups += 1
            done   += groups

        return groups
