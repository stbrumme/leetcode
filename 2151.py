class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        result = 0
        size   = len(statements)

        # constants
        bad    = 0
        good   = 1
        either = 2

        def deeper(known):
            length = len(known)
            person = length - 1

            # check whether most recent assumption matches all related statements
            for other in range(length):
                # reveal contradictions
                if known[person] == good and statements[person][other] not in ( known[other],  either ):
                    return
                if known[other ] == good and statements[other][person] not in ( known[person], either ):
                    return

            # good people
            citizens = known.count(good)

            nonlocal result
            if length < size:
                # next person
                if result - citizens < size - length: # only if possible to improve
                    deeper(known + [ good ])
                    deeper(known + [ bad  ])
            else:
                result = max(result, citizens)

        deeper([])
        return result
