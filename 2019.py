class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        result = 0

        @cache
        def deeper(left, right):
            # must be a number
            if left == right:
                return set([ int(s[left]) ])

            # 2 points
            wrong = set()
            for i in range(left, right + 1):
                # split at each operation
                if s[i] in "+*":
                    # compute both sides
                    one = deeper(left, i - 1)
                    two = deeper(i + 1, right)

                    # create all combinations
                    for o in one:
                        for t in two:
                            if s[i] == "+":
                                value = o + t
                            else:
                                value = o * t

                            # never above 1000
                            if value <= 1000:
                                wrong.add(value)

            return wrong

        correct = eval(s) # 5 points
        wrong   = deeper(0, len(s) - 1)
        for a in answers:
            if a == correct:
                result += 5
            elif a in wrong:
                result += 2

        return result
