class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0;h=len(nums)-1
        while(l<h):
            m=(l+h)//2
            if m%2==1:
                if nums[m]==nums[m-1]:
                    l=m+1
                else:
                    h=m
            else:
                if nums[m]==nums[m+1]:
                    l=m+2
                else:
                    h=m
        return nums[l]
        