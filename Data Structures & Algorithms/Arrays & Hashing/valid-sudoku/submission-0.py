# Valid Sudoku
# -----------------------------------------------------------------------------
# Problem: Given a 9x9 board (digits '1'-'9' or '.' for empty), decide whether
#          the CURRENT filled cells are valid — no repeated digit within any
#          row, any column, or any 3x3 box. The board need not be solvable.
#
# Idea:    Track three groups of sets — one per row, one per column, one per
#          box — and make a single pass over all 81 cells. For each filled cell,
#          if its digit already appears in any of its three sets, the board is
#          invalid. Otherwise record it in all three and continue.
#
# Time:  O(1)   fixed 81 cells regardless of input
# Space: O(1)   fixed 27 sets (9 rows + 9 cols + 9 boxes)
#
# The box-index formula is the part worth remembering:
#     box_index = (r // 3) * 3 + (c // 3)
# r // 3 gives the box ROW (0-2), c // 3 gives the box COLUMN (0-2), and
# multiplying the row by 3 flattens that 3x3 grid of boxes into indices 0-8.
#
# Note: '.' cells are skipped — this validates what's filled in, it does NOT
#       check that the board is complete.
# -----------------------------------------------------------------------------
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
