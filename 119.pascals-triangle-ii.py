#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    # Recursive solution O(rowIndex) space
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex - 1) 
        curr_row = [1]
        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i+1])
        curr_row.append(1)
        return curr_row

    
    # recursive with memorization
    def getRow2(self, rowIndex: int) -> List[int]:
        self.seen = dict()
        def helper(row,column):
            if column == 0 or row == column:
                return 1
            if (row,column) in self.seen:
                return self.seen[(row,column)]
            result = helper(row - 1 , column - 1) + helper(row -1 , column)
            self.seen[(row,column)] = result
            return result
        
        ans = []
        for i in range(rowIndex + 1):
            ans.append(helper(rowIndex,i))
        return ans
    
    # Iterative solution
    def getRow3(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(rowIndex+1):
            for j in range(i-1,0,-1):
                row[j] = row[j] + row[j-1]
            row.append(1)
            # print(row)
        return row
    # @lc code=end


