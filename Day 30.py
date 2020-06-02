class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, lambda p: p[0] * p[0] + p[1] * p[1])
