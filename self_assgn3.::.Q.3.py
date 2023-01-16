n= int(input("enter the number of values u want in the list "))

my_list = []

for i in range(1,n+1):
    a = int(input("enter a number"))
    my_list.append(a)

result = [(val,val**2) for val in my_list]
print(result)
