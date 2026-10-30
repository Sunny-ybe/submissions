class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] *n for _ in range(n)]

        def issafe(r,c):
            #upper left
            i = r-1
            j = c-1
            while i>= 0 and j>= 0:
                    if board[i][j] == "Q":
                        return False
                    i,j = i-1, j-1

            #upper right
            i =r-1
            j = c+1
            while i>= 0 and j<n:
                    if board[i][j] == "Q":
                        return False
                    i,j = i-1, j+1
            
            #vertical
            i = r-1
            j = c
            while i>= 0:
                    if board[i][j] == "Q":
                        return False
                    i = i-1
            return True
        
        def backtrack(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return
            
            for j in range(n):
                if issafe(i,j):
                    board[i][j] = "Q"
                    backtrack(i+1)
                    board[i][j] ="."
        backtrack(0)
        return res

                
        

                

           
            



                



            


        

            

        
        