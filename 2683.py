class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # try 0 and 1 as values for derived[-1]
        for start in ( 0, 1 ):
            x = start
            for d in derived:
                x ^= d

            if x == start:
                return True

        return False
