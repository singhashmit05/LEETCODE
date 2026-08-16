class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        el1=None
        el2=None
        for i in range(len(nums)):
            if count1==0 and nums[i]!=el2:
                count1+=1
                el1=nums[i]
            elif count2==0 and nums[i]!=el1:
                count2+=1
                el2=nums[i]
            elif el1==nums[i]:
                count1+=1
            elif el2==nums[i]:
                count2+=1
            else:
                count1-=1
                count2-=1
                
        cnt1=0
        cnt2=0
        for i in range(len(nums)):
            if el1==nums[i]:
                cnt1+=1
            if el2==nums[i]:
                cnt2+=1
        min=len(nums)//3+1
        result=[]
        if cnt1 >=min:
            result.append(el1)
        if cnt2>=min:
            result.append(el2)
        return result



        