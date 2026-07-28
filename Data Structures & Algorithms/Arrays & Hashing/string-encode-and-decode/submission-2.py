# Encode and Decode Strings
# -----------------------------------------------------------------------------
# Problem: Design encode(list[str]) -> str and decode(str) -> list[str] so that
#          any list of strings survives the round trip. Strings may contain ANY
#          characters, including whatever you'd want to use as a separator.
#
# Idea:    Length-prefix encoding. Each string is written as
#              "<length>#<string>"
#          e.g. ["neet","code"] -> "4#neet4#code". To decode, read digits up to
#          the '#' to learn the length, then take exactly that many characters
#          — no scanning, no ambiguity.
#
# Time:  O(n)   n = total characters across all strings, for both encode/decode
# Space: O(n)   the output string / list
#
# Why not just join on a delimiter: any separator you pick ("#", ",", etc.) can
# legally appear INSIDE a string, so splitting on it would break the data
# apart at the wrong place. The length prefix sidesteps this — the '#' here is
# only ever read as "the digits stopped", and the length tells us exactly how
# far to jump, so a '#' inside the payload is consumed as ordinary content.
#
# Multi-digit lengths work because we read every digit up to the first '#',
# not just one character — so a 12-char string encodes as "12#..." correctly.
# -----------------------------------------------------------------------------
class Solution:
    def encode(self, strs):
        encoded_string = ""
        for s in strs:
            # length prefix + '#' marker + the string itself
            encoded_string+= str(len(s))+"#"+s
        return encoded_string

    def decode(self, s):
        i = 0
        decoded_strs = []
        while (i<len(s)):
            start = i
            while (s[i]!="#"):   # walk forward to the '#' -- digits in between
                i+=1
            length = int(s[start:i])   # extract length as int
            i += 1                     # step past the '#' onto the payload
            decoded_strs.append(s[i:i+length])   # take exactly `length` chars
            i+=length                  # jump to the start of the next chunk

        return decoded_strs
