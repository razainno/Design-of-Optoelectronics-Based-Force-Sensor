
import numpy as np

#digital value for weight 0.5kg
file0= open("data0_nkg.csv")
a0= np.loadtxt(file0, delimiter=",")



#digital value for weight 0.5kg
file1= open("data0.5_nkg.csv")
a1= np.loadtxt(file1, delimiter=",")

#digital value for weight 1.25kg

file2= open("data1.25_nkg.csv")
a2= np.loadtxt(file2, delimiter=",")

#digital value for weight 1.75
file3= open("data1.75_nkg.csv")
a3= np.loadtxt(file3, delimiter=",")



#print(a1.shape,a2.shape,a3.shape)

A=np.vstack((a0,a1,a2,a3))
print(A.shape)



n0 =a0.shape[0]                   #length of list1
list0 = [0*9.8] *n0



n1 =a1.shape[0]                   #length of list1
list1 = [0.5*9.8] *n1


n2=a2.shape[0]                   #length of list2
list2 = [1.25*9.8] *n2

n3 =a3.shape[0]                   #length of list1
list3 = [1.75*9.8] *n3


B=np.array(list0+list1+list2+list3)
print(B.shape)


#calculation of least square of the data


x, residuals, rank, s= np.linalg.lstsq(A, B, rcond=None)

print(x)

