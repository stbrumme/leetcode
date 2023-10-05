class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union-find
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        mails  = {} # all address
        users  = [] # all names (duplicates allowed)
        parent = [] # ID of each user, union-find to merge accounts
        for i, a in enumerate(accounts):
            parent.append(i)
            users .append(a.pop(0))
            for address in a:
                if address in mails:
                    union(parent[i], mails[address]) # existing
                else:
                    mails[address] = find(parent[i]) # new address

        result = defaultdict(set) # ID => merged addresses
        for i, a in enumerate(accounts):
            for address in a:
                result[find(i)].add(address)

        for r in result: # convert to desired format
            yield [ users[r] ] + sorted(result[r])
