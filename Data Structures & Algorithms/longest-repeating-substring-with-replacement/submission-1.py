class Solution:
    def characterReplacement(self,s,k):
        left = 0 
        maxfreq = 0
        maxseq = 0
        freq={}

        for right in range(0,len(s)):
            freq[s[right]] = freq.get(s[right] , 0) + 1
            maxfreq = max(freq[s[right]] , maxfreq)

            while(right - left + 1) - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
            maxseq = max(maxseq, right - left + 1)

        return maxseq