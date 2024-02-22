class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # assign a ID to each required skill
        need = {}
        for r in req_skills:
            need[r] = len(need)
        all = (1 << len(need)) - 1 # bitmask of all skills

        # bitmasks of revelant skills of each person
        masks = []
        for p in people:
            current = 0
            for s in p:
                if s in need:
                    current |= 1 << need[s]
            masks.append(current)

        have = { 0: [] } # zero peeple, zero skills
        for i, m in enumerate(masks):
            if m == 0: # no relevant skill
                continue

            next = have.copy()
            for h in have:
                if (h & all) == all: # already complete
                    continue

                more = (h | m) & all
                if more == h: # no new skill
                    continue

                # add person to team
                team = have[h] + [ i ]
                # new team with the skillset - or a smaller team
                if more not in next or len(next[more]) > len(team):
                    next[more] = team

            have = next

        return have[all]
