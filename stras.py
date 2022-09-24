import numpy as np
import time

def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print(time.clock()), "seconds process time"

t0 = time.time()
procedure()
print(time.time()) -t0, "seconds wall time"

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

def strassens(A,B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        #PARTITION
        a11, a12, a21, a22 = split(A)
        b11, b12, b21, b22 = split(B)
        #CALCULATE THE SUM
        s1 = b12 - b22 
        s2 = a11 + a12
        s3 = a21 + a22 
        s4 = b21 - b11 
        s5 = a11 + a22 
        s6 = b11 + b22
        s7 = a12 - a22 
        s8 = b21 + b22
        s9 = a11 - a21 
        s10 = b11 + b12

        # CALCULATE THE PRODUCT MATRICES
        P1 = strassens(a11, s1)
        P2 = strassens(s2, b22)
        P3 = strassens(s3, b11)
        P4 = strassens(a22, s4)
        P5 = strassens(s5, s6)
        P6 = strassens(s7, s8)
        P7 = strassens(s9, s10)

        # CALCULATE THE FINAL PRODUCT SUB MATRICES
        c11 = P4 + P5 + P6 - P2
        c12 = P1 + P2
        c21 = P3 + P4
        c22 = P1 + P5 - P3 - P7

        C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

        return C
print(strassens(A,B))