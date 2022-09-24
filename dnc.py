import numpy as np

A = np.array([[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]])

B = np.array([[1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]])


C = np.array([[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]])

def split(matrix):

	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def DivideConquer(A,B):
    n = len(A)
    C = np.array([[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]])
    if n == 1:
        return A * B  
    else:
        a11,a12,a21,a22 = split(A)

        b11,b12,b21,b22 = split(B)

        c11,c12,c21,c22 = split(C)

        c11 = DivideConquer(a11, b11) + DivideConquer(a12,b21)
        c12 = DivideConquer(a11, b12) + DivideConquer(a11,b22)       
        c21 =  DivideConquer(a21, b11) + DivideConquer(a22,b21)
        c22 =  DivideConquer(a21, b12) + DivideConquer(a22,b22)
        
        C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
        
        return C
        

print(DivideConquer(A,B))