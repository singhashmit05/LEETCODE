class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # row=[]
        # ans=1
        # row.append(ans)
        # # print(ans)
        # for i in range(1,numRows):
        #     ans*=numRows-i
        #     ans/=i
        #     row.append(ans)
        # return [row]

        # # print(ans)
        result=[]
        for i in range(numRows):
            ans=1
            row=[]
            row.append(ans)
            for k in range(1,i+1):
                ans=ans*(i-k+1)//k
                row.append(ans)
            result.append(row)
        return result
        