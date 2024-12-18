import numpy as np


twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(twoDarray)

#inserting an element in two d array

# newTwoDArray = np.insert(twoDarray, 0, [[13,14,15,16]], axis=1)
# newTwoDArray = np.insert(twoDarray, 0, [[13,14,15]], axis=0)

# twoDarray = np.append(arr = twoDarray, values=[[15,16,17]], axis=0)

# print(twoDarray)

#Traversing an array 
# for i in range(len(twoDarray)): #-------------------O(m)
#                                                                                 #---O(mn)
#     for j in range(len(twoDarray[0])): #_____________O(n)
#         print(twoDarray[i][j])   #-----------------------O(1)


#Searching element in array
# for i in range(len(twoDarray)):
#     for j in range(len(twoDarray[0])):
#         if(twoDarray[i][j]==11):
#             print(f"The location is {i}, {j}")



#Deletion of array

newTwodarray = np.delete(twoDarray, 1, axis=0)   #Time complexity O(mn) space complexity O(mn)

print(newTwodarray)
