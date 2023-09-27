class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def subs(s):
            parts = s.split(".")
            for i in range(len(parts)):
                yield ".".join(parts[i:])

        all = defaultdict(int)
        for c in cpdomains:
            visits, domain = c.split(" ")
            for s in subs(domain):
                all[s] += int(visits)

        for a in all:
            yield str(all[a]) + " " + a
