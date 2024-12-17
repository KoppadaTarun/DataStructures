import array

array1 = array.array("i", [1,2,3,4,5])

def insert_element(array, index):
                                    #------Time complexity O(n) space_complexity O(1)
    array.insert(6, index)

insert_element(array1, 6)

print(array1)

#traverse array T.C - O(n) S.C - O(1)

#searching element - O(n) O(1) for len function O(1) and for range function O(1)

#Delete element 
arr1 = array.array('i',[1,2,4,5,67])

arr1.remove(1)

print(arr1) 

#T.C O(n) if last element O(1) space complexity O(1)

arr1.reverse()

print(arr1)

print(arr1.buffer_info())

