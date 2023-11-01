class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # distinct meals
        meals = set()
        for o in orders:
            meals.add(o[2])

        all = {}
        for o in orders:
            table = int(o[1])
            food  = o[2]
            if table not in all:
                all[table] = {}
                for m in meals:
                    all[table][m] = 0
            all[table][food] += 1

        yield [ "Table" ] + sorted(meals)
        for a in sorted(all):
            row = [ str(a) ]
            for m in sorted(meals):
                row.append(str(all[a][m]))
            yield row
