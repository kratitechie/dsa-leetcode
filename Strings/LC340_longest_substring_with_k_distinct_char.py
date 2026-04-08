def longestSubstringKDistinct(s, k):
    window = {}
    l = 0
    max_len = 0

    for r in range(len(s)):
        # expand
        window[s[r]] = window.get(s[r], 0) + 1

        # shrink if invalid
        while len(window) > k:
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            l += 1

        # update answer
        max_len = max(max_len, r - l + 1)

    return max_len