class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        result = 0

        # split into groups with identical offense
        groups = defaultdict(list)
        for attack, defense in properties:
            groups[attack].append(defense)

        high = 0 # maximum defense of stronger attackers
        for attack in sorted(groups, reverse = True): # best attackers first
            stronger = high

            for defense in groups[attack]:
                if defense < high:
                    # worse defense and offense
                    result  += 1
                else:
                    # good defense, maybe better than anything we've seen yet
                    stronger = max(stronger, defense)

            high = stronger

        return result
