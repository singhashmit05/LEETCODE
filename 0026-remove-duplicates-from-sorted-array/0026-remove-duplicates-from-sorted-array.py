class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         low=0
         high=1
         
         for high in range(1,len(nums)):
             if nums[high]==nums[high-1]:
                high+=1
             else:
                nums[low+1]=nums[high]
                low+=1
                high+=1
                
         return (low+1)       
 

        