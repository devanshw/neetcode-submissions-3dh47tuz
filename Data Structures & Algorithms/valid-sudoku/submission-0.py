class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowsets = [] 
        for _ in range(9):
            rowsets.append(set())
        
        colsets = [] 
        for _ in range(9):
            colsets.append(set())

        # 3 sub lists in a list, each sub list has 3 sets
        sqsets = []
        for _ in range(3):
            sublist = []
            for _ in range(3):
                sublist.append(set())
            sqsets.append(sublist)
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                #check if seen in row, set or sq
                if (num in rowsets[i]) or (num in colsets[j]) or (num in sqsets[i//3][j//3]):
                    return False
                rowsets[i].add(num)
                colsets[j].add(num)
                sqsets[i//3][j//3].add(num)
        
        return True

                
                



        


'''
9 sets for 9 rows
9 sets for 9 cols
9 sets for 9 sqs 
'''