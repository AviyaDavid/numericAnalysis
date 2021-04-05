def main():
    #recieve matrix
    print('Please enter size for  matrix A :')
    sizeA = input()
    A= createImat(sizeA)
    for i in range(sizeA):
        for j in range(sizeA):
            print('Please enter value for A['+i+']['+j+']:')
            A[i][j]= input()
    B=[]
    for i in range(sizeA):
        print('Please enter value for B[' + i + ']:')
        B.append(input())

    # check if inverse= find inverse
    detA=calcDet(A)
    if detA is not 0:
        findInverse(A,detA)




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
    size= len(a)
    result=createImat(size) #create unit mat
    for i in range(size): #reset zeros in result mat
        result[i][i]=0
    for i in range(size): #iter on rows
        for j in range(size): #iter on columns
            for k in range(size):#iter on columns
                result[i][j]+=a[i][k]*b[k][i]
    return result



def twoontwoDet(mat):
    return (mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1])

def calcDet(mat):
    size=len(mat)
    if size is 2:
        return twoontwoDet(mat)
    if size is 1:
        return mat[1][1]
    else:
        det=1
        upperMat=upper(mat)
        for i in range(size):
            det*=upperMat[i][i]
        return det


def upper(mat):
    size = len(mat)
    elem=createImat(size)
    for i in range(size):
        pivot=mat[i][i]
        for j in range(i, size):
            elem[j][i]=-(mat[j][i]/pivot)
        mat= MultiplyMatrix(elem,mat)
    return mat

def findElem(mat):
    size = len(mat)
    elem = createImat(size)


def findInverse(mat,det):
    size=len(mat)
    #special case for 2x2 matrix
    if size is 2:
        temp=mat[0][0]
        mat[0][0]=mat[1][1]
        mat[1][1]=temp
        mat[0][1]*=(-1)
        mat[1][0] *= (-1)
        det=1.0/det
        for i in range(size):
            for j in range(size):
                mat[i][j]*=det
        return mat

    else:


def minorMatrix(mat):
    size= len(mat)
    minors=createImat(size)
    tempMat=createImat(size-1)
    for row in range(size):
        for col in range(size):
            i=0
            j=0
            while i<size:
                while j<size:
                    if i != row:
                        if j != col:
                            tempMat[i][j]
                            j+=1
                        if j==