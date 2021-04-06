import copy #for deep copy of matrix
def main():
    #user_matrix = [[[0.913 ,0.659], [0.457,0.330]],[[0, 2, -1.41],[-1.41, 2, 0], [1, -1.41, 1] ],[[1,2,3],[4,5,6],[7,8,9]]]
    # user_matrix_2 = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]
    #vector_B = [[[0.254], [0.127]],[[1], [2], [3]],[[1],[2],[3]]]

    user_matrix=[]
    vector_B=[]

    print('please enter  the size of matrix A\n')

    while True: #loop for checking user input
        size_matrix = input()
        if float(size_matrix) % 1 == 0 and float(size_matrix)>1 :
            size_matrix = float(size_matrix)
            break
        print('error!,please enter integer number >= 2')
    size_matrix = int(size_matrix)

    value_to_matrix(user_matrix,size_matrix,size_matrix)
    print('please enter vector B values\n')
    value_to_matrix(vector_B,size_matrix, 1)


    org_pivot(user_matrix, vector_B)  # organize to prevent instability

    # check if inverse= find inverse
    detA = calcDet(user_matrix)
    if detA != 0:
        inverA = findInverse(user_matrix)
        X = MultiplyMatrix(inverA, vector_B)
    else:  # if irreversible do LU
        LU = LowerUpper(user_matrix)
        X = MultiplyMatrix(LU[1], MultiplyMatrix(findInverse(LU[0]), vector_B[i]))
    print('x={}'.format(X) )

    # user_test_lowerupper = LowerUpper(user_matrix_1)


# print(MultiplyMatrix(user_test_lowerupper[0], user_test_lowerupper[1]))
# user_test_lowerupper = LowerUpper(user_matrix_2)
# print(MultiplyMatrix(user_test_lowerupper[0], user_test_lowerupper[1]))

def org_pivot(matrix, B):
    size = len(matrix)
    for col in range(size):
        maxRow = maxincol(matrix, col)
        if maxRow > col:
            xchngRows(matrix, col, maxRow)
            xchngRows(B, col, maxRow)


def maxincol(mat, col):
    max = col
    for row in range(col, len(mat)):
        if abs(mat[row][col]) > abs(mat[max][col]):
            max = row
    return max


def xchngRows(matrix, col, maxrow):
    tempr = matrix[col]
    matrix[col] = matrix[maxrow]
    matrix[maxrow] = tempr



def value_to_matrix(matrix, row, column):
    for i in range(row):
        row_values = []
        for j in range(column):
            print('please enter a values\nrow {0},column {1}'.format(i, j))
            row_values.append(float(input()))
        matrix.append(row_values)


def createImat(size):
    newMat = []
    for i in range(size):
        newMat.append([])
        for j in range(size):
            if i == j:
                newMat[i].append(1)
            else:
                newMat[i].append(0)

    return newMat


def MultiplyMatrix(a, b):
    col_size_b = len(b[0])
    row_size_a = len(a)
    sum = 0
    new_mat = []
    for r in range(row_size_a):
        new_mat.append([])
        for c in range(col_size_b):
            for k in range(row_size_a):
                sum += (a[r][k] * b[k][c])
            new_mat[r].append(sum)
            sum = 0
    return new_mat


def mat_add(A, B):
    new_mat = []
    if len(A) == len(B):
        size = len(A)
        for r in range(size):
            new_mat.append([])
            for c in range(size):
                sum = A[r][c] + B[r][c]
                new_mat[r].append(sum)
    return new_mat

def LowerUpper(mat):
    size = len(mat)
    upper=copy.deepcopy(mat)
    lower = createImat(size)
    for c in range(size):
        elem = createImat(size)
        pivot = upper[c][c]
        for r in range(c + 1, size):
            elem[r][c] = (-1) * (upper[r][c] / pivot)
            lower[r][c] = (-1) * elem[r][c]
        upper = MultiplyMatrix(elem, upper)  # for upper matrix

    return [lower, upper]


def findInverse(mat):
    size = len(mat)
    matCopy=copy.deepcopy(mat)
    inverMat = createImat(size)
    for col in range(size):
        pivot = matCopy[col][col]
        tempElem = createImat(size)
        for row in range(size):
            if row != col:
                tempElem[row][col] = (-1) * (matCopy[row][col] / pivot)
        matCopy = MultiplyMatrix(tempElem, matCopy)
        inverMat = MultiplyMatrix(tempElem, inverMat)

    # check diagonal numbers
    for i in range(size):
        pivot = matCopy[i][i]
        if pivot != 1:
            for col in range(size):
                inverMat[i][col] /= float(pivot)
            matCopy[i][i] = 1
    return inverMat


def twoontwoDet(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


def calcDet(mat):
    size = len(mat)
    if size == 2:
        return twoontwoDet(mat)
    if size == 1:
        return mat[1][1]
    else:
        det = 1
        upperMat = LowerUpper(mat)[1]
        for i in range(size):
            det *= upperMat[i][i]
        return det
main()