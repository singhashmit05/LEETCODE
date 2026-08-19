class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        high=0
        n=len(fruits)
        freq={}
        res=-1
        for high in range(n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq) > 2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            length = high-low +1
            res=max(res,length)
        return res
        