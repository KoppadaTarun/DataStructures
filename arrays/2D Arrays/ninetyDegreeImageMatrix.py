import copy

# #Brute Force method

# arr1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# arr2 = copy.deepcopy(arr1)

# arr3 = copy.deepcopy(arr1)

# n = len(arr1)


# for i in range(n):
#     for j in range(n):
#         arr2[j][(n-1)-i] = arr1[i][j]

# print(arr2)

# #90 anti clockwise

# print("Anti clock wise")

# for i in range(n):
#     for j in range(n):
#         # print(arr3[(n-1)-j][i])
        
#        arr3[(n-1)-j][i] = arr1[i][j]

# print(arr3)
# print(arr1)


#Optimization
#transpose

#!no need to change the diagonal values 
#[0][1] -[1][0] , [0][2]-[2][0], [0][3] -[3][0] will swap
#[1][2] -[2][1] , [1][3]-[3][1] will swap
#[2][3] - [3][2] will swap  i starts from 0 and ends to 2 j starts from 0 to 3
arr4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(arr4)
arr5 = copy.deepcopy(arr4)

for i in range(n-1):
    
    for j in range(i+1,n):

        a = arr5[j][i]

        arr5[j][i] = arr4[i][j]

        arr5[i][j]= a

print(arr4)
print(arr5)

#[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]


#Reverse

for i in arr5:
    i.reverse()

print(arr5)