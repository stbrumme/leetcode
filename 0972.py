class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(x):
            integer  = x
            fraction = "0"
            repeat   = "0"

            if "." in x:
                integer, fraction = x.split(".")
                if "(" in fraction:
                    fraction, repeat = fraction.split("(")
                    repeat = repeat[ : -1] # remove ")"

            full = integer + "." + fraction + repeat * 20
            return float(full)

        return abs(parse(s) - parse(t)) < 0.0000000000000000001
