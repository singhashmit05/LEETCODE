class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # for i in range(n):
        #     count=0
        #     for j in range(n):
        #         if nums[j]==nums[i]:
        #             count+=1
        #     if count>(n/2):
        #        return nums[i]
        el=None
        count=0
        for i in range(len(nums)):
            if count==0:
                count=1
                el=nums[i]
            elif nums[i]==el:
                count+=1
            else:
                count-=1
        count1=0
        for i in range(len(nums)):
            if nums[i]==el:
               count1+=1
            if count1 > (len(nums)/2):
                return el
        return -1

        