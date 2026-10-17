class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l=0;h=len(letters)-1;a=letters[0]
        while(l<=h):
            m=(l+h)//2
            if letters[m]>target:
                a=letters[m]
                h=m-1
            else:
                l=m+1
        return a
        