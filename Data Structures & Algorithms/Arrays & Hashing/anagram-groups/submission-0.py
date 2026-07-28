# Group Anagrams
# -----------------------------------------------------------------------------
# Problem: Given a list of strings, group the ones that are anagrams of each
#          other (same letters, any order).
#
# Idea:    Two words are anagrams IFF they have the same letter counts. So build
#          a 26-slot count array for each word and use it (as a tuple, since
#          lists aren't hashable) as the dictionary key. All anagrams land in the
#          same bucket.
#
# Time:  O(n * k)   n = number of words, k = length of the longest word
# Space: O(n * k)   for the hashmap holding every word
# -----------------------------------------------------------------------------
class Solution:
    def groupAnagrams(self, strs):

        map = {}                        # key: letter-count signature -> value: list of words

        for word in strs:               # visit every word in the input
            count = [0] * 26            # fresh count array, one slot per letter a..z

            for ch in word:             # tally each character of this word
                # ord(ch) - 97 maps 'a'->0, 'b'->1, ... 'z'->25 (97 == ord('a'))
                count[ord(ch) - 97] += 1

            key = tuple(count)          # tuple is hashable, so it can be a dict key

            if key not in map:          # first word with this signature -> start a bucket
                map[key] = []
            map[key].append(word)       # drop the word into its anagram bucket

        return list(map.values())       # each value is one group of anagrams
