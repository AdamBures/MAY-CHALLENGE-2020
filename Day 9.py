class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        x,i=0,1
        while x<num:
            x+=i
            i+=2
        return x==num
