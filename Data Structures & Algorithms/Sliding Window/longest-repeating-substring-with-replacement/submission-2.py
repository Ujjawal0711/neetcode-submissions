# LC 424 · Longest Repeating Character Replacement
# -----------------------------------------------------------------------------
# Problem: Given a string s and integer k, you may replace up to k characters
#          with any other character. Return the length of the longest substring
#          made of a single repeated character that you can produce.
#
# Idea:    Sliding window over s, keeping a live frequency tally of the window.
#          A window is VALID if the characters that aren't the majority one can
#          all be covered by the k replacements — i.e.
#              window_length - maxfreq <= k
#          Expand with `right`; whenever that condition breaks, shrink from the
#          left until it holds again. The largest valid window is the answer.
#
# Time:  O(n)   each char enters and leaves the window at most once
# Space: O(1)   the freq map holds at most 26 letters
#
# The subtle bit is that `maxfreq` is deliberately never decremented — see the
# inline note below for why that's safe. It's the part of this problem most
# people (reasonably) assume is a bug.
# -----------------------------------------------------------------------------
class Solution:
    def characterReplacement(self, s, k):
        left = 0
        maxfreq = 0     # highest single-char count seen in window so far (never decremented)
        maxseq = 0      # answer: longest valid window length found
        freq = {}       # char -> count, live tally of chars currently in window

        for right in range(0, len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            # .get(s[right], 0) -> current count, or 0 if char unseen yet

            maxfreq = max(maxfreq, freq[s[right]])
            # maxfreq = count of whichever char is most common.
            # NOTE: intentionally never decremented during shrinking below --
            # it can go "stale" (too high) relative to the live window, but that's fine:
            # any maxseq recorded while maxfreq was accurate was genuinely achievable,
            # so a stale maxfreq only blocks unnecessary shrinks, never produces a wrong answer.

            # window_length - maxfreq = how many chars in the window are NOT the majority
            # char -- i.e., how many replacements this window would need.
            # If that exceeds k, we don't have enough budget -- window invalid, must shrink.
            while (right - left + 1) - maxfreq > k:
                freq[s[left]] -= 1   # char leaving the window loses one count
                left += 1            # shrink from the left, one step at a time

            # window is now guaranteed valid (fits within k replacements) -- record its length
            maxseq = max(maxseq, right - left + 1)

        return maxseq
