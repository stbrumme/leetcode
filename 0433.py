class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def canMutate(a, b):
            return 1 == sum(i != j for i, j in zip(a, b))

        todo  = set([ startGene ])
        known = todo.copy()
        steps = 0
        while todo:
            next = set()

            for t in todo:
                if t == endGene:
                    return steps
                
                for b in bank:
                    if b not in known and canMutate(t, b):
                        next .add(b)
                        known.add(b)
                        
            todo = next
            steps += 1

        return -1