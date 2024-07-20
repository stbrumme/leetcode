class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        result = 0
        height = len(mat)
        width  = len(mat[0])

        ones = [ 0 ] * width
        for row in mat:
            # consecutive ones (horizontal)
            for x, cell in enumerate(row):
                ones[x] += cell
                ones[x] *= cell # reset if 0, keep if 1

            low = []
            sub = [ 0 ] * width
            for x, count in enumerate(ones):
                # keep track of lowest number and its index
                while low and ones[low[-1]] >= count:
                    low.pop()

                if low:
                    start  = low[-1]
                    length = x - start
                    sub[x] = sub[start] + count * length
                else:
                    sub[x] = count * (x + 1)

                low.append(x)

            result += sum(sub)

        return result
