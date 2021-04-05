def main():

    user_matrix_1= [[1,2,1],[2,6,1],[1,1,4]]
    user_matrix_2 = [[1, -1, -2], [2, -3,-5], [-1, 3, 5]]
    vector_B = []
    #print('please enter  the size of matrix A\n')
    #size_matrix = int(input())
    #value_to_matrix(user_matrix,size_matrix,size_matrix)
    #print('please enter vector B values\n')
    #value_to_matrix(vector_B,size_matrix, 1)

    user_test_lowerupper = LowerUpper(user_matrix_1)
    print(MultiplyMatrix(user_test_lowerupper[0],user_test_lowerupper[1]))
    user_test_lowerupper = LowerUpper(user_matrix_2)
    print(MultiplyMatrix(user_test_lowerupper[0], user_test_lowerupper[1]))


def org_pivot(matrix,B):
    pivot_value = matrix[0][0]
    pivot_row_value = 0;
    for i in range(len(matrix)):
        if matrix[i][0]>pivot_value:
            pivot_row = matrix[i]
            temp_row = matrix[pivot_row_value]

def value_to_matrix(matrix,row, column):
    for i in range(row):
        row_values = []
        for j in range(column):
            print('please enter a values\nrow {0},column {1}'.format(i,j))
            row_values.append(int(input()))
        matrix.append(row_values)

def createImat(size):
    newMat=[]
    for i in range(size):
        newMat.append([])
        for j in range(size):
            if i == j:
                newMat[i].append(1)
            else:
                newMat[i].append(0)

    return newMat


def MultiplyMatrix(a,b):
    size = len(a)
    sum = 0
    new_mat = []
    for r in range(size):
        new_mat.append([])
        for c in range(size):
            for k in range(size):
                sum += (a[r][k]*b[k][c])
            new_mat[r].append(sum)
            sum=0
    return new_mat


def mat_add(A,B):
    new_mat=[]
    if len(A) == len(B):
        size=len(A)
        for r in range(size):
            new_mat.append([])
            for c in range(size):
                sum = A[r][c]+B[r][c]
                new_mat[r].append(sum)
    return new_mat



def LowerUpper(mat):
    size = len(mat)
    lower=createImat(size)
    for c in range(size):
        elem = createImat(size)
        pivot = mat[c][c]
        for r in range(c+1, size):
            elem[r][c] = (-1)*(mat[r][c] / pivot)
            lower[r][c]= (-1)*elem[r][c]
        mat = MultiplyMatrix(elem, mat) #for upper matrix

    return[lower,mat]

def findInverse(mat):
    size = len(mat)

    inverMat = createImat(size)
    for col in range(size):
        pivot = mat[col][col]
        tempElem = createImat(size)
        for row in range(size):
            if row != col:
                tempElem[row][col] = (-1) * (mat[row][col] / pivot)
        mat = MultiplyMatrix(tempElem, mat)
        inverMat = MultiplyMatrix(tempElem, inverMat)

    # check diagonal numbers
    for i in range(size):
        pivot = mat[i][i]
        if pivot != 1:
            for col in range(size):
                inverMat[i][col] /= float(pivot)
            mat[i][i] = 1
    return inverMat


def twoontwoDet(mat):
    return (mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1])

def calcDet(mat):
    size=len(mat)
    if size == 2:
        return twoontwoDet(mat)
    if size == 1:
        return mat[1][1]
    else:
        det=1
        upperMat=LowerUpper(mat)[1]
        for i in range(size):
            det*=upperMat[i][i]
        return det

main()
