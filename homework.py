list = []

for i in range(1,300):
    if (i % 2 == 0): 
        list.append(i)

print("Length of the list is ", len(list))


print("The squared values are: ")
for x in list:
    print(x**2)

print("57 is in the list: ", 57 in list)