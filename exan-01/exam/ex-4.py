# Examples 
matrix1 = [ [1, 2, 3], [4, 5, 6], ]
matrix2 = [ [7, 8, 9], [10, 11, 12] ]

def add_matrices(matrix1, matrix2):
    final = []


    for i in range(len(matrix1)):
            temp_list = []
            for j in range(len(matrix1[i])):
                temp_list.append(matrix1[i][j] + matrix2[i][j])
            final.append(temp_list)
    
    print(final)
    return(final)

result = add_matrices(matrix1, matrix2)
#The result matrix will be: [[8, 10, 12],[14, 16, 18]]
