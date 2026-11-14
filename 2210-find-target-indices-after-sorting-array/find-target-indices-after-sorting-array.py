class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        def first():
            l = 0
            h = len(nums) - 1
            f = -1
            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    f = m
                    h = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    h = m - 1
            return f
        def last():
            l = 0
            h = len(nums) - 1
            g = -1
            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                   g = m
                   l = m + 1
                elif nums[m] < target:
                   l = m + 1
                else:
                   h = m - 1
            return g
        f=first()
        g=last()
        if f == -1:
            return []
        return list(range(f, g+1))
        
    
        
            
        
            
       

  




    