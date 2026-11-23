class Solution:
    def longestPalindrome(self, s: str) -> str:

        T = "#" + "#".join(s) + "#"

        P = [0] * len(T)

        center = 0
        right = 0

        maxLen = 0
        centerIndex = 0

        for i in range(len(T)):

            mirror = 2 * center - i

            if i < right:
                P[i] = min(right - i, P[mirror])

            while (
                i + P[i] + 1 < len(T)
                and i - P[i] - 1 >= 0
                and T[i + P[i] + 1] == T[i - P[i] - 1]
            ):
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i

        start = (centerIndex - maxLen) // 2

        return s[start:start + maxLen]