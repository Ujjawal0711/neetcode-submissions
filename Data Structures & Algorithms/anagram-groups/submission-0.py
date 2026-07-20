class Solution:
    def groupAnagrams(self, strs):

        map={}                     #Hashmap to hold the tuple values 

        for word in strs:          #Outer for loop for words in strs
            count=[0]*26           #This is the array it converts each word into a array according to the word

            for ch in word:        #Inner for loop for each word
                count[ord(ch)-97]+=1   #ASCII converison converts Ch to ASCII and fills the array with 1 if ch there

            key=tuple(count)

            if key not in map:
                map[key]=[]
            map[key].append(word)

        return list(map.values())