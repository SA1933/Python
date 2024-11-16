import numpy as np

A = [[1,2,3],
     [4,5,6],
     [7,8,0]]

B = [[10,11,12],
     [13,14,15],
     [16,17,10]]

A = np.array(A)
B = np.array(B)

transpose_data_A = np.transpose(A)
transpose_data_B = np.transpose(B)
invers_array_A = np.linalg.inv(A)
perkalian_1 = np.dot(A,B)
transpose_perkalian_1 = np.linalg.inv(perkalian_1)
perkalian_2 = np.dot(transpose_data_A,transpose_data_B)
transpose_perkalian_2 = np.linalg.inv(perkalian_2)

print ("\nA :")
print (A)
print ("\nB :")
print (B)
print ("\nTranspose data A :")
print (transpose_data_A) 
print ("\ntranspose data B :")
print (transpose_data_B)
print ("\nperkalian 1 :")
print (perkalian_1)
print ("\ntranspose perkalian 1 :")
print (transpose_perkalian_1)
print ("\nperkalian 2 :")
print (perkalian_2)
print ("\ntranspose perkalian 2 :")
print (transpose_perkalian_2)