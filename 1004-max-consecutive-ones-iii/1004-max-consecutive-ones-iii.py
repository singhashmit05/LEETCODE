class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        res=-1
        freq={}
        for high in range(len(nums)):
            freq[nums[high]]=freq.get(nums[high],0)+1
            zero_count=freq.get(0,0)
            length = high - low + 1
            # diff = length - zero_count 
            while ( zero_count > k ):
                if nums[low]==0:
                    zero_count -=1
                freq[nums[low]]-=1
                low+=1
                length=high-low+1
                # diff= length - zero_count
            length = high - low + 1
            res = max(res,length)
        return res


        