import random

list1 = [1, 1, 2, 3, 5, 8, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list3 = []
list4 = []
for i in list1:
    if i in list2:
        list3.append(i)
        for j in list3:
            if j not in list4:
                list4.append(j)
print(list1)
print(list2)
print("common elements in list1 and list2 are ",list4)

# Extras solution
list5 = []
for i in range(50):
    i = random.randint(1,100)
    list5.append(i)
print(list5)
list6 =[]
for j in range(40):
    j = random.randint(1,100)
    list6.append(j)
list7 = []
list8 = []
for x in list5:
    if x in list6:
        list7.append(x)
        for y in list7:
            if y not in list8:
                list8.append(y)
print("list5: " , list5)
print("list6", list6)
print("list7", list7)
print("common elements in list5 and list6 are ",list8)