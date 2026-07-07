class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False

        tally={}

        for i in range(len(s)):
            chars=s[i]
            chart=t[i]

            tally[chars]=tally.get(chars,0)+1

            tally[chart] = tally.get(chart, 0) - 1

        for count in tally.values():
            if count != 0:
                return False

        return True


        