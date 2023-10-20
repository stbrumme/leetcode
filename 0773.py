class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # BFS, just factorial(6) = 720 combinations
        seen  = {}
        todo  = [ ( 1,2,3,4,5,0 ) ]
        steps = 0
        while todo:
            next = []
            for key in todo:
                a,b,c,d,e,f = key
                if key in seen:
                    continue
                seen[key] = steps

                a,b,c,d,e,f = key
                if a == 0:
                    next.append(( d,b,c,a,e,f ))
                    next.append(( b,a,c,d,e,f ))
                if b == 0:
                    next.append(( b,a,c,d,e,f ))
                    next.append(( a,c,b,d,e,f ))
                    next.append(( a,e,c,d,b,f ))
                if c == 0:
                    next.append(( a,b,f,d,e,c ))
                    next.append(( a,c,b,d,e,f ))
                if d == 0:
                    next.append(( d,b,c,a,e,f ))
                    next.append(( a,b,c,e,d,f ))
                if e == 0:
                    next.append(( a,b,c,e,d,f ))
                    next.append(( a,b,c,d,f,e ))
                    next.append(( a,e,c,d,b,f ))
                if f == 0:
                    next.append(( a,b,f,d,e,c ))
                    next.append(( a,b,c,d,f,e ))

            steps += 1
            todo   = next

        a,b,c = board[0]
        d,e,f = board[1]
        return seen.get(( a,b,c,d,e,f ), -1)
