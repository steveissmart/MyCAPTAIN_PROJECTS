print("Enter the number of elements you want in the two sets:-")
Elements_in_set_1 = int(input("Number of elements in set 1 : "))
Elements_in_set_2 = int(input("Number of elements in set 2 : "))
List_1 = []
List_2 = []

for i in range (0,Elements_in_set_1):
    i = int(input("enter the element"))
    List_1.append(i)
for j in range (0,Elements_in_set_2):
    j = int(input("enter the element"))
    List_2.append(j)
Set_1 = set(List_1)
Set_2 = set(List_2)
print("The two sets are:")
print("Set 1: ", Set_1)
print("Set 2: ", Set_2)
print("The union of two sets is:")
print("Set_1 Union Set_2: ",set.union(Set_1,Set_2))
print("The intersection of two sets is:")
print("Set_1 intersection Set_2: ",set.intersection(Set_1,Set_2))
print("The difference of two sets is:")
print("Set_1 difference Set_2: ",set.difference(Set_1,Set_2))
print("The Symmetric difference of two sets is:")
print("Set_1 Symmetric difference Set_2: ",set.symmetric_difference(Set_1,Set_2))