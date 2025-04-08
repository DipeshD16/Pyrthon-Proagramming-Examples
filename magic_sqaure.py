def is_magic_square(matrix):
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        return False
    #calculate the target sum using the first row:    
    target = sum(matrix[0])
   
    #check sum for all rows:
    for row in matrix:
        if sum(row) != target:
            return False
   
    #check sum for all coloumns:
    for col in range(4):
        if sum(matrix[row][col] for row in range(4)) != target:
            return False

    #check main diagonal (top left to bottom-right)
    if sum(matrix[i][i] for i in range(4)) != target:
        return False
    #check for secondary diagonal
    if sum(matrix[i][3-i] for i in range(4)) !=target:
        return False
       
    return True

magic_sqaure = [
    [16, 3, 2, 13],
    [5, 10, 11 ,8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]]

if is_magic_square(magic_sqaure):
    print("Magic Sqaure")
else:
    print("Not a magic square.")