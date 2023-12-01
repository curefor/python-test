# 学校：长春工业大学
# 学生：李东洋
# 开发时间: 2023/9/13 23:06
#用高斯消去法解方程组
'''x1+x2+x3=6
      4x2-x3=5
   2x1-2x2+x3=1'''
'''代码如下'''
'''import numpy as np
A=np.array([[1,1,1,6],[0,4,-1,5],[2,-2,1,1]])
print(f'利用高斯消去法解线性方程组\n{A}')
def Gauss_elimination(A):#消元化为上三角
    for col in range(len(A)-1):
        for row in range(col+1,len(A)):#需要进行多少次消元
            r = A[row][col]/A[col][col]
            j=0
        for value in A[col]:
            i=row
            A[i][j]=A[i][j]-value*r
            if j<len(A):j=j+1

"""回带"""
ans=[]
A=list(A)
A.reverse()
for sol in range(len(A)):
    if sol == 0:
        ans.append(A[0][-1]/A[0][-2])
    else:
        known =0
        for x in range(sol):
            known=known+ans[x]*A[sol][-2-x]
        ans.append((A[sol][-1]-known)/A[sol][-sol-2])
ans.reverse()
print(f'所得结果为\n{Gauss_elimination(A)}')'''
'''开始没装numpy包'''


import numpy as np

def Input():
    n=int(input())

    A=np.zeros([n,n],dtype=np.double())
    for r in range():
        A[r:]=np.array(input().split(),dtype=np.double)
    B=np.zeros([n,1],dtype=np.double)
    for r in range(n):
        B[r:] = np.array(input(), dtype=np.double)
    return A,B

def lufact(A,B):
    n=B.size
    Y=np.zeros([n,1],dtype=np.double)
    R=np.arange(0,n)
    epslion=np.finfo(np.float32).eps

    for p in range(n):
        max_index=np.argmax(np.abs(A[p:n,p]))
        max_row=max_index+p
        A[[p,max_row],:]=A[[max_row,p],:]
        R[[p,max_row]]=R[[max_row,p]]

        if abs(A[p,p])<epslion:
            print('A is singular.No unique solution')
            break
        for k in range(p+1,n):
            mult =A[k,p]/A[p,p]
            A[k,p]=mult
            A[k,p+1:n]=A[k,p+1:n]-mult*A[p,p+1:n]

    Y[0]=B[R[0]]
    for k in range(1,n):
        Y[k]=B[R[k]]-A[k,0:k]@Y[0:k]
    return A,Y
def backsub(A,B):
    n=B.size
    X=np.zeros([n,1],dtype=np.double)
    X[n-1]=B[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        X[i]=(B[i]-A[i,i+1:]@X[i+1:])/A[i][i]
    return X

def out(x):
    print(x)


def main():
    A,B=Input()
    A,B=lufact(A,B)
    out(A)

    X=backsub(A,B)
    out(X)

if __name__=='__main__':
    main()


