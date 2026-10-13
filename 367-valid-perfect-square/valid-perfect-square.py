class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        l=0;h=num//2
        while(l<=h):
            m=(l+h)//2
            if m*m==num:
                return True
            elif m*m>num:
                h=m-1
            else:
                l=m+1
        return False
        