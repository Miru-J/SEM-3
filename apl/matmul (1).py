def matrix_multiply(matrix1, matrix2):
    ''' 
    Function multiplies two given matrixes 
    parameters : matrix1 and matrix2 - provided matrixes 
                 rows_m1 , col_m1 - rows of matrix1 and columns of matrix1
                 rows_m2 , col_m2 - rows of matrix2 and columns of matrix2
                 c - final result matrix after multiplying matrix1 and 2
                 i, j ,k are just integer variables to run inside the loop
    return: the function returns the matrix c
    '''
    if not matrix1:
        raise ValueError("Matrix multiplication function not implemented")
    if not matrix2:
        raise ValueError("Matrix multiplication function not implemented")
    
    '''
    checking if the matrix is empty or not empty, if not not empty it procedes further
    '''
    rows_m1 = len(matrix1)    #length of the matrix gives how many number of rows are present 
    col_m1 = len(matrix1[0])   #length of each element in the matrix gives number of columns present
    rows_m2 = len(matrix2)
    col_m2 = len(matrix2[0])
   
    if col_m1 != rows_m2 :
        raise ValueError("Matrix multiplication function not implemented")
    #checking if the rows of matrix 2 are equal to columns of matrix 1 
    
    c = []
    #initializing the matrix c
    for i in range(rows_m1):
        rows = []
        for j in range(col_m2):
            rows.append(0)
        c.append(rows)
    
    #To initialize c, append same number zeros as rows and columns to the existing string. Avoiding storage error.   
    
    #implementation of logic 
    for i in range(rows_m1):
        for j in range(col_m2):
            for k in range(col_m1):
                c[i][j] += matrix1[i][k]*matrix2[k][j]
            
    return c
    