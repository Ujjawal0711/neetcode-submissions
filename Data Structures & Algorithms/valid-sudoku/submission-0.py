class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]    # rows[i] = set of digits seen in row i
        cols = [set() for _ in range(9)]    # cols[i] = set of digits seen in col i
        boxes = [set() for _ in range(9)]   # boxes[i] = set of digits seen in 3x3 box i

        for r in range(9):
            for c in range(9):              # single pass, all 81 cells
                val = board[r][c]
                if val == '.':               # skip empty cells -- not a completeness check
                    continue

                box_index = (r // 3) * 3 + (c // 3)   # maps cell -> which of the 9 boxes

                # check row, col, box simultaneously -- duplicate = invalid immediately
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                # no duplicate -- record val in all three sets, move to next cell
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True

# Time: O(1) -- fixed 81 cells regardless of input
# Space: O(1) -- fixed 27 sets (9 rows + 9 cols + 9 boxes)