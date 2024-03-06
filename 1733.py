class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # stupid 1-indexed input data: let's convert it to 0-based
        babylon = [ set([ x - 1 for x in l ]) for l in languages ]
        friends = [ [ a - 1, b - 1] for a, b in friendships ]

        people = set()
        for a, b in friends:
            # pairs who do not speak a common language
            if not (babylon[a] & babylon[b]):
                people.add(a)
                people.add(b)

        # already perfect communication
        if not people:
            return 0

        # languages spoken among pairs who do not understand each other (yet)
        speak = [ 0 ] * n
        for p in people:
            for b in babylon[p]:
                speak[b] += 1

        # find most common language
        common = speak.index(max(speak))
        # teach it to those who don't know it
        result = 0
        for p in people:
            if common not in babylon[p]:
                result += 1

        return result
