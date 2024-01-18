class Solution:
    def reformatNumber(self, number: str) -> str:
        # clean up
        number = number.replace(" ", "")
        number = number.replace("-", "")

        # groups of three
        result = ""
        while len(number) > 4:
            result += number[: 3] + "-"
            number  = number[3 :]

        if len(number) < 4:
            # two or three digits
            return result + number
        else:
            # twice two digits
            return result + number[:2] + "-" + number[2:]
