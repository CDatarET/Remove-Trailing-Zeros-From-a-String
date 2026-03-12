class Solution:
    def removeTrailingZeros(self, num):
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                return(num[0:i + 1])
