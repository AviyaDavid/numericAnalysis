def main():

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


def findOpposite(mat):
