class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width  = len(image[0])

        replace = image[sr][sc]
        if replace == color:
            return image

        # instead of the 10000000000th breadth first search, let's try a depth first search
        todo = [ ( sc, sr ) ]
        while todo:
            x, y = todo.pop()

            if image[y][x] != replace:
                continue
            image[y][x] = color

            if x > 0:
                todo.append(( x - 1, y ))
            if x < width - 1:
                todo.append(( x + 1, y ))
            if y > 0:
                todo.append(( x, y - 1 ))
            if y < height - 1:
                todo.append(( x, y + 1 ))
            # there might be quite a few duplicates in todo
            # which can be avoided with a set instead of a list, but I don't really care ...

        return image
