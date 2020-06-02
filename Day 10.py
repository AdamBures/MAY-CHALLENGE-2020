class Solution:
    def findJudge(self, N, trust):
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i
        return -1
