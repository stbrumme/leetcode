class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def addKey(keys, newKey):
            if newKey in [ ".", "#", "@" ]:
                return keys
            if "A" <= newKey <= "Z":    # skip locks
                return keys
            id = ord(newKey) - ord("a") # keys are lowercase
            return keys | (1 << id)

        def hasKey(keys, lock):
            # always allowed to go to empty cells or cells with a key
            if lock in [ ".", "@" ] or "a" <= lock <= "z":
                return True
            id = ord(lock) - ord("A") # locks are uppercase
            return (keys & (1 << id)) != 0

        allKeys = 0 # bitmask of all keys in the whole maze
        width   = len(grid[0])
        height  = len(grid)
        todo = [ ] # steps,x,y,keys
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "@":
                    todo.append(( 0, 0, x, y))
                # pick up any key
                allKeys = addKey(allKeys, grid[y][x])

        seen = set()
        while todo:
            # next cell
            steps, keys, x, y = heappop(todo)

            # avoid loops
            lookup  = (keys, x, y)
            if lookup in seen:
                continue
            seen.add(lookup)
            # (speed up)
            lesskeys = keys
            while lesskeys != 0:
                lesskeys &= lesskeys - 1
                seen.add((lesskeys, x, y))

            # use or pick up keys
            if not hasKey(keys, grid[y][x]):
                continue
            keys = addKey(keys, grid[y][x])
            if keys == allKeys:
                return steps

            # keep walking
            if x > 0          and grid[y][x - 1] != "#":
                todo.append(( steps + 1, keys, x - 1, y ))
            if x < width - 1  and grid[y][x + 1] != "#":
                todo.append(( steps + 1, keys, x + 1, y ))
            if y > 0          and grid[y - 1][x] != "#":
                todo.append(( steps + 1, keys, x, y - 1 ))
            if y < height - 1 and grid[y + 1][x] != "#":
                todo.append(( steps + 1, keys, x, y + 1 ))

        return -1
