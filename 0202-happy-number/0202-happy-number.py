class Solution:
    def sum(self,s:int)->int:
        total=0
        while s>0:
            d=s%10
            total+=d*d
            s=s//10
        return total
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        while fast!=1:
            slow=self.sum(slow)
            fast=self.sum(self.sum(fast))
            if slow==fast and slow!=1:
                return False
        return True


        