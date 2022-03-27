class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n))>1:
            count=0
            for i in str(n):
                count+=int(i)*int(i)
            n=count
        if n==1 or n==7:
            return True
        else:
            return False