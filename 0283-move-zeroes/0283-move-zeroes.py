class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        low =0
        high=0
        
        n=len(nums)

        for high in range(n):
            if nums[high]!=0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1

            
       
        