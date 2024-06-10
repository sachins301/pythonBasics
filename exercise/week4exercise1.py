#4.1. Split Number List (2.5 points)
str = '10 67 123 46 20 18 36 250'
lst = [int(x) for x in str.split()]
print(lst)

str1 = '10,67,123,46,20,18,36,250'
lst1 = [int(x) for x in str1.split(",")]
print(lst1)

#4.2 Split Data into List (2.5 points)
str2 = '90,67,87,102,77,80'
lst2 = [int(x) for x in str2.split(",")]
print(sum(lst2))

#4.3 Slice Lists (2.5 points)
lst3 = [1,2,3,4,5,6,7,8,9]
print(lst3[:4])

#4.4 Slice Lists with Increment (2.5 points)
lst4 = ['a','b','c','d','e','f','g']
print(lst4[::2])
