class Solution:
    def originalDigits(self, s: str) -> str:
        # unique characters when processing in sequence
        # zero  z
        # one            o
        # two    w
        # three     r
        # four    u
        # five       f
        # six      x
        # seven       v
        # eight        t
        # nine          i
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        zero  = freq["z"]
        freq["e"] -= zero
        freq["r"] -= zero
        freq["o"] -= zero

        two   = freq["w"]
        freq["t"] -= two
        freq["o"] -= two

        four  = freq["u"]
        freq["f"] -= four
        freq["o"] -= four
        freq["r"] -= four

        six   = freq["x"]
        freq["s"] -= six
        freq["i"] -= six

        three = freq["r"]
        freq["t"] -= three
        freq["h"] -= three
        freq["e"] -= 2 * three

        five  = freq["f"]
        freq["i"] -= five
        freq["v"] -= five
        freq["e"] -= five

        seven = freq["v"]
        freq["s"] -= seven
        freq["e"] -= 2 * seven
        freq["n"] -= seven

        eight = freq["t"]
        freq["e"] -= eight
        freq["i"] -= eight
        freq["g"] -= eight
        freq["h"] -= eight

        nine = freq["i"]
        freq["n"] -= 2 * nine
        freq["e"] -= nine

        one = freq["o"]
        freq["n"] -= one
        freq["e"] -= one

        # freq[...] = 0 by now

        result  = ""
        result += "0" * zero
        result += "1" * one
        result += "2" * two
        result += "3" * three
        result += "4" * four
        result += "5" * five
        result += "6" * six
        result += "7" * seven
        result += "8" * eight
        result += "9" * nine
        return result
