class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        width  = len(dungeon[0])
        height = len(dungeon)

        hp = []
        for y in range(height):
            hp.append([ 999999999 ] * width)

        # travel in reverse, need 1 HP plus whatever the last room
        hp[height-1][width-1] = 1 - min(0, dungeon[height-1][width-1])

        todo = []
        if width > 1 or height > 1:
            todo = [ [ height-1, width-1] ]

        while todo:
            y, x = todo.pop()
            health = hp[y][x]

            if x > 0:
                need = max(1, health - dungeon[y][x-1])
                if hp[y][x-1] > need:
                    hp[y][x-1] = need
                    todo.append([ y, x-1 ])
            if y > 0:
                need = max(1, health - dungeon[y-1][x])
                if hp[y-1][x] > need:
                    hp[y-1][x] = need
                    todo.append([ y-1, x ])

        return hp[0][0]
