class Solution:
    def reverseBits(self, n: int) -> int:
        temp1 = '{:032b}'.format(n)
        #print(temp1)
        temp2 = temp1
        temp1 = temp2[::-1]
        #print(temp1)
        return int(temp1, 2)
        #print(temp1,temp2)
