class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l=1;h=max(nums)
        while(l<h):
            s=0
            m=(l+h)//2
            for num in nums:
                s += (num + m - 1) // m
            if(s <= threshold):
                 h=m
            else:
                l=m+1  
        return l  
           
          
           
       