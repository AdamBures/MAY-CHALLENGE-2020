class Solution(object):
    def singleNonDuplicate(self, a: List[int]) -> int:
        if len(a) == 1:
            return a[0]
        lo, hi = 0, len(a)-1
        while (hi - lo) >= 2:
            mid = (lo + hi) // 2
            if a[mid] == a[mid+1]:
                if mid % 2 == 0:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif a[mid-1] == a[mid]:
                if mid % 2 == 1:
                    lo = mid + 1
                else:
                    hi = mid - 2
            else:
                return a[mid]
        if lo == hi or lo == 0:
            return a[lo]
        else:
            return lo if a[lo-1] != a[lo] else a[hi]
