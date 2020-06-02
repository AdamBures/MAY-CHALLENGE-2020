class Solution:
    def maxSubarraySumCircular(self, A: 'List[int]') -> 'int':
        t1=A[:]
        t2=A[:]
        c=0
        for i in range(1,len(A)):
            if t1[i-1]>0:     #find max one without circular
                t1[i]+=t1[i-1]
                c=1
            if t2[i-1]<0:     #find min one without circular
                t2[i]+=t2[i-1]
        if c==0:
            return max(A)
        return max(max(t1),(sum(A)-min(t2)))
