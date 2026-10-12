class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l=0;h=x//2
        while(l<=h):
            m=(l+h)//2
            if m*m==x:
                return m
            elif m*m<x:
                l=m+1
            else:
                h=m-1
        return h

  