import copy  # for deep copy of matrix
import sys


def main():
    A = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    B = [2, 6, 5]

    org_pivot(A, B)  # organize to prevent instability
    print('pivoting...')
    if dominant_diagonal(A) is not True:
        sys.exit("Doesn't have dominant diagonal, can't solve!")

    print("choose method: \n1.Jacobi\n2.Gaus-Zaidel")
    choice = input()
    #if choice == 1:
     #   jacobi(A, B)
    #else:
      #  gaus_zaidel(A, B)
    jacobi(A, B)
    gaus_zaidel(A, B)

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


def dominant_diagonal(mat):
    flag = True
    size = len(mat)
    for r in range(size):
        pivot = abs(mat[r][r])
        sum = 0
        for c in range(size):
            if c != r:
                sum += abs(mat[r][c])
        if pivot < sum:
            flag = False
    return flag


def jacobi(A, B):
    print('####Jacobi####\n')
    iter = 0
    size = len(A)
    r = [1, 1, 1]  # initialize to get in loop
    next_rot = [0, 0, 0]
    print('{} \n'.format(next_rot))
    while eps(r, next_rot) is False:
        iter += 1
        r = copy.deepcopy(next_rot)
        for r in range(size):
            sum = B[r]
            for c in range(size):
                if c != r:
                    sum += (-1) * A[r][c] * r[c]
            next_rot[r] = sum / A[r][r]
        print('{} \n'.format(next_rot))
    print('The Result was found after {} iterations'.format(iter))


def gaus_zaidel(A, B):
    print('####Gaus-Zaidel####\n')
    iter = 0
    size = len(A)
    r = [1, 1, 1]  # intialize to get in loop
    next_rot = [0, 0, 0]
    print('{} \n'.format(next_rot))
    while eps(r, next_rot) is False:
        iter += 1
        r = copy.deepcopy(next_rot)
        for r in range(size):
            sum = B[r]
            for c in range(size):
                if c != r:
                    if c < r:
                        sum += (-1) * (A[r][c] * next_rot[c])
                    else:
                        sum += (-1) * (A[r][c] * r[c])
            next_rot[r] = sum / A[r][r]
        print('{} \n'.format(next_rot))
    print('The Result was found after {} iterations'.format(iter))


def eps(r, next_r):
    flag = True
    for i in range(r):
        if next_r[i] - r[i] > 0.0001:
            flag = False
            break
    return flag


main()
