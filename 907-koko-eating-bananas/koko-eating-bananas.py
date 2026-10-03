class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1;r=max(piles)
        while(l<r):
            m=(l+r)//2
            ho=0
            for pile in piles:
                ho+= (pile + m - 1) // m
            if ho> h:
                l = m + 1
            else:
                r = m
        return l
        