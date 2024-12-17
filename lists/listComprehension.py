list1 = [1,2,3,4,5,6]

# newlist1 = [item*2 for item in list1]

# print(newlist1)


newlist2 = [item*2 for item in list1 if item%2==0]

newlist3 = [item*2 if item%2==0 else item*3 for item in list1]

print(newlist3)

print(newlist2)

a = 'a'
if(a.isalpha()):
    print(True)


#use elif

list2 = [-10, 0 , 1, 5, 2, 24, 48, 89, 63, 71]

newlist5 = ["negative" if num<0 else "zero" if num==0 else "positive" for num in list2]

print(newlist5)


na = [item for item in list2 if item>0]

print(na)

na = ["Even" if num%2==0 else "Odd" for num in list2]

print(na)

na = ["negative" if num<0 else "zero" if num==0 else "positive" for num in list2]

print(na)