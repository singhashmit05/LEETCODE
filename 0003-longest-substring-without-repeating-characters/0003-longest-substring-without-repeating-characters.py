class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        freq={}
        res=-1
        if len(s)==0:
            return 0
        for  high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            k=high-low+1
            
            while (len(freq) < k):
                freq[s[low]] -=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                k= high-low+1
            length = high-low+1
            res=max(res,length)
        return res











        