def main():
    # recieve matrix
    print('Please enter size for  matrix A :')
    sizeA = input()
    A = createImat(sizeA)
    for i in range(sizeA):
        for j in range(sizeA):
            print('Please enter value for A[' + i + '][' + j + ']:')
            A[i][j] = input()
    B = []
    for i in range(sizeA):
        print('Please enter value for B[' + i + ']:')
        B.append(input())

    # check if inverse= find inverse
    detA = calcDet(A)
    if detA is not 0:
        findInverse(A, detA)


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
    size = len(a)
    sum = 0
    new_mat = []
    for r in range(size):
        new_mat.append([])
        for c in range(size):
            for k in range(size):
                sum += (a[r][k] * b[k][c])
            new_mat[r].append(sum)
            sum = 0
    return new_mat


def twoontwoDet(mat):
    return (mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1])


def calcDet(mat):
    size = len(mat)
    if size is 2:
        return twoontwoDet(mat)
    if size is 1:
        return mat[1][1]
    else:
        det = 1
        upperMat = upper(mat)
        for i in range(size):
            det *= upperMat[i][i]
        return det


def upper(mat):
    size = len(mat)
    elem = createImat(size)
    for i in range(size):
        pivot = mat[i][i]
        for j in range(i, size):
            elem[j][i] = -(mat[j][i] / pivot)
        mat = MultiplyMatrix(elem, mat)
    return mat


def findInverse(mat, det):
    size = len(mat)
    # special case for 2x2 matrix
    if size is 2:
        temp = mat[0][0]
        mat[0][0] = mat[1][1]
        mat[1][1] = temp
        mat[0][1] *= (-1)
        mat[1][0] *= (-1)
        det = 1.0 / det
        for i in range(size):
            for j in range(size):
                mat[i][j] *= det
        return mat
    else:
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


def listElementryMarix(mat):
    size = len(mat)
    elemList = []
    for col in range(size):
        elem = createImat(size)
        pivot = mat[col][col]
        row = 0
        while row != size:
            if row != col:
                elem[row][col] = -(mat[row][col] / pivot)
            row += 1
        elemList.append(elem)
    return elemList
