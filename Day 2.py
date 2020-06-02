class Solution(object):
    def numJewelsInStones(self, J, S):
        hashSet=[0]*52
        for i in S:
            if ord(i)>=97:
                hashSet[ord(i)-ord('a')]+=1
            else:
                hashSet[ord(i)-ord('A')+26]+=1
        res=0
        for j in J:
            if ord(j)>=97:
                res+=hashSet[ord(j)-ord('a')]
            else:
                res+=hashSet[ord(j)-ord('A')+26]
        return res
