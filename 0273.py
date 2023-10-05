class Solution:
    def numberToWords(self, num: int) -> str:
        def one(n):
            names = [ "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" ]
            return names[n]

        def two(n):
            if n < 10:
                return one(n)

            if n < 20:
                teens = [ "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                          "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen" ]
                return teens[n - 10]

            tens = [ "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]
            return tens[n // 10] + " " + one(n % 10)

        def three(n):
            if n < 100:
                return two(n)

            return one(n // 100) + " Hundred " + two(n % 100)


        if num == 0:
            return "Zero"

        illion = [ "", " Thousand ", " Million ", " Billion ", " Trillion ", " Gazillion " ]
        result = ""
        while num > 0:
            if num % 1000 > 0:
                result = three(num % 1000) + illion[0] + result
            num //= 1000
            illion.pop(0)

        return result.replace("  ", " ").strip(" ")
