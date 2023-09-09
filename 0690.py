class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        all = { e.id : e for e in employees }

        @cache
        def deeper(i):
            return all[i].importance + sum(deeper(j) for j in all[i].subordinates)

        return deeper(id)
