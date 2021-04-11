import copy  # for deep copy of matrix


def main():
    A = [[1, 1, 1], [2, 2, 1], [1, 3, 2]]
    B = [6, 9, 13]

    org_pivot(A, B)  # organize to prevent instability
    if len(A) < 4:  # if size is smaller than 4, solve by inverse
        inverseA = findInverse(A)
        X = MultiplyMatrix(inverseA, B)
    else:  # if bigger or equal 4, solve by LU
        LU = LowerUpper(A)  # find lower and upper
        lower = LU[0]
        upper = LU[1]
        X = MultiplyMatrix(findInverse(lower), MultiplyMatrix(findInverse(upper), B))  # find x vector
    print('x={}'.format(X))


def org_pivot(matrix, B):
    #  organize to prevent instability
    size = len(matrix)
    for col in range(size):
        maxRow = maxincol(matrix, col)
        if maxRow > col:
            xchngRows(matrix, col, maxRow)
            xchngRows(B, col, maxRow)


def maxincol(mat, col):
    # returns max value row
    max = col
    for row in range(col, len(mat)):
        if abs(mat[row][col]) > abs(mat[max][col]):
            max = row
    return max


def xchngRows(matrix, col, maxrow):
    # replace lines in matrix
    tempr = matrix[col]
    matrix[col] = matrix[maxrow]
    matrix[maxrow] = tempr


def createImat(size):
    # create unit matrix
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
    # multiplying matrices
    size = len(a)
    sum = 0
    if type(b[0]) is not int:
        new_mat = createImat(size)
        for r in range(size):
            for c in range(size):
                for k in range(size):
                    sum = sum + (a[r][k] * b[k][c])
                new_mat[r][c] = sum
                sum = 0
    else:
        new_mat = []
        for r in range(size):
            for c in range(size):
                sum = sum + (a[r][c] * b[c])
            new_mat.append(sum)
            sum = 0
    return new_mat


def LowerUpper(mat):
    # find lower and upper for mat
    size = len(mat)
    upper = copy.deepcopy(mat)
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
    # find inverse matrix for mat
    size = len(mat)
    matCopy = copy.deepcopy(mat)
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


main()
