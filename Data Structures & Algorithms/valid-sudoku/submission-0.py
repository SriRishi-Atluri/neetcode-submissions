class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        # Check all of the rows
        for i in range(n):
            rowSet = set()
            for j in range(m): 
                val = board[i][j]
                if val == ".": 
                    continue 
                if val in rowSet: 
                    return False 
                rowSet.add(val)

        # Check all of the coloumns 
        for j in range(m): 
            colSet = set()
            for i in range(n): 
                val = board[i][j]

                if val == ".": 
                    continue 

                if val in colSet:
                    return False 

                colSet.add(val)

        # Check each 3x3 cell 
        for boxRow in range(0,9,3): 
            for boxCol in range(0,9,3): 
                gridSet = set()  # start a fresh set for this 3x3 box

                for rowOffset in range(3): 
                    for colOffset in range(3): 
                        val = board[boxRow + rowOffset][boxCol + colOffset]  # compute each cell inside the current box
                        if val == ".": 
                            continue  # skip empty cells

                        if val in gridSet:
                            return False 

                        gridSet.add(val)

        return True