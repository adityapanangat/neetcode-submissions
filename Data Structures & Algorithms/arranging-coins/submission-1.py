class Solution:
    def arrangeCoins(self, n: int) -> int:
        numRows = 0

        while n > 0:
            n -= (numRows + 1)
            numRows += 1

        if n == 0:
            return numRows
        
        else:
            return numRows - 1
        


        

