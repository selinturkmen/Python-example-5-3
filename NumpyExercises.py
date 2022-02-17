import numpy as np

def initializer():
    x = np.array([[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 2],[1, 6, 1, 1]])
    return x

def larger_diagonals(A, B):
    A = np.array(A)
    B = np.array(B)
    x = A[0,0]
    y = A[-1,-1]    
    i = B[0,0]
    j = B[-1,-1]
    
    if ((x+y)/2)>((i+j)/2):
        return(A)
    else:
        return(B)
 
def add_columns(A):
    
    A = np.array(A)    
    colodd= A[::1,1::2]
    coleven= A[::,0:3:2]
    A = np.add(coleven, colodd)  
    return A

def rank_calculator(A):
    
    A = np.array([[9, 4, 15, 0, 18],
              [16, 19, 8, 10, 1]])

    fa = A.flatten()
    newA = sorted(fa)  
    x = {}
    for i in range(len(newA)):
        x[newA[i]] = i

    y = np.zeros(A.shape, dtype= int)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            y[i][j] = x[A[i][j]]
    inp = np.array([[9,4,15,0,18],
                          [16,19,8,10,1]])
            
    inp.ravel().argsort().argsort().reshape(inp.shape)
    
    return y

def create_checkerboard(n):
    y = np.zeros((n, n), dtype = int) 
    y[1::2, ::2] = 1
    y[::2, 1::2] = 1   
    return y

def main():

    a = np.array([[4,5,10], [6,7,2]])
    b = np.array([[8.4, 3.2, 6.5], [9.1, 7.4, 6.1]])
    print(a)
    print(b)

    
        
################################################################ 

if __name__ == '__main__':
    main()
