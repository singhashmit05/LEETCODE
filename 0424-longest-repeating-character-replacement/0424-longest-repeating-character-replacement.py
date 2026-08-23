class Solution:
    # def find(self,a):
    #     maxcnt=-1
    #     for i in range(256):
    #         maxcnt=max(maxcnt,a[i])
    #     return maxcnt
    def characterReplacement(self, s: str, k: int) -> int:
        # maxc=self.find(f)
        low=0
        high=0
        res=-1
        freq={}
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            maxc = max(freq.values())
            length=high-low+1
            diff= length - maxc

            while (diff > k):
                freq[s[low]]-=1
                low+=1
                maxc=max(freq.values())
                length=high-low+1
                diff= length - maxc
            length=high-low+1
            res=max(res,length)
        return res

        