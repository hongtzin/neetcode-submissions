class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hor = {}
        ver = {}
        box = {}

        for i in range(len(board)):
            for r in range(len(board[i])):

                if i not in hor:
                    hor[i] = set()
                if r not in ver:
                    ver[r] = set()

                if board[i][r] == ".":
                    continue 

                    
                if board[i][r] in hor[i]:
                    return False
                    # pass
                else:
                    hor[i].add(board[i][r])

                if board[i][r] in ver[r]:
                    return False
                    # pass
                else:
                    ver[r].add(board[i][r])

                boxtuple = ((i + 3)//3, (r + 3)//3)

                if boxtuple not in box:
                    box[boxtuple] = set()
                
                if board[i][r] in box[boxtuple]:
                    return False
                box[boxtuple].add(board[i][r])


        print(hor)
        print()
        print(ver)
        print()
        print(box)
        return True