class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # if all characters matched
            if i == len(word):
                return True
            
            # check bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore 4 directions
            found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            # backtrack
            board[r][c] = temp
            return found

        # try from each cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
            
