class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        final=[]
        for k in nums:            
            string = str(k)
            temp1,temp2 = [],[]
            ans = ""
            if string[0] == "-":
                for i in range(1,len(string)):
                    temp1.append(string[i])
                temp2 = temp1[::-1]
                ans = ans + "-"
            else:
                for i in range(0,len(string)):
                    temp1.append(string[i])
                temp2 = temp1[::-1]
            for i in temp2:
                ans = ans + i
            final.append(int(ans))
            final.append(k)
        #print(final)
        return len(set(final))
