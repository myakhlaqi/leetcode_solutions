/*
 * @lc app=leetcode id=498 lang=javascript
 *
 * [498] Diagonal Traverse
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
function findDiagonalOrder(mat){
    var n = mat.length;
    var m = mat[0].length;
    var ans = []
    var row, col;
    row = 0; col = 0;
    for (var d = 0; d < m + n - 1; d++) {
        var temp = [];
        if (d < n) {
            row = d;
            col = 0;
        } else {
            row = n - 1;
            col = d - row;
        }
        while (row >= 0 && col < m) {
            temp.push(mat[row][col]);
            row -= 1;
            col += 1;
        }
        if (d % 2 == 0)
            ans.push(...temp);
        else
            ans.push(...temp.reverse());

    }
    return ans;
};
// @lc code=end

