class Solution:
    def encode(self, strs):
        encoded_string = ""
        for s in strs:
            encoded_string+= str(len(s))+"#"+s     
        return encoded_string

    def decode(self, s):
        i = 0
        decoded_strs = []
        while (i<len(s)):
            start = i
            while (s[i]!="#"):
                i+=1
            length = int(s[start:i])   # extract length as int
            i += 1
            decoded_strs.append(s[i:i+length])
            i+=length
                        
        return decoded_strs