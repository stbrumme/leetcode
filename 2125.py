class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        for b in bank:
            devices = b.count("1")
            if devices > 0:
                result += devices * prev
                prev    = devices
        return result
