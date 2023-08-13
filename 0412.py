class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            add = ""
            if i % 3 == 0:
                add += "Fizz"
            if i % 5 == 0:
                add += "Buzz"
            if add == "":
                add = str(i)
            result.append(add)
        return result
