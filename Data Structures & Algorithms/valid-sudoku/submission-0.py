class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        h = 3 

        for i in range(n) : 
            ligne = []
            for c in board[i] :
                if c != '.' : 
                    ligne.append(c)
            if len(ligne) != len(set(ligne)) : 
                return False
            colone = [] 
            for j in range(n) : 
                if board[j][i] != '.' :
                    colone.append(board[j][i])
            if len(colone) != len(set(colone)):
                return False 
        

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                carre = []
                for i in range(br, br+3):
                    for j in range(bc, bc+3):
                        if board[i][j] != '.':
                            carre.append(board[i][j])   # <-- [i][j], pas [j][i] !
                if len(carre) != len(set(carre)):        # <-- indenté sous for bc
                    return False

        return True
                
            

