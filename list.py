#Create a list of fruits and print it.
items=['apple','mango','banana','grapes','guava']
print(items)
output=['apple', 'mango', 'banana', 'grapes', 'guava']

#Create a list of a 5 numbers and print 1st and last element.
list1=[1,2,3,4,5]
print(list[0],list[4]) 

#Add Orange to the fruit list.
items=['apple','mango','banana','grapes','guava']
items.append("orange")
print(items)
output=['apple', 'mango', 'banana', 'grapes', 'guava', 'orange']

#Remove banana from fruit list.
items=['apple','mango','banana','grapes','guava']
items.remove("banana")
print(items)
output=['apple', 'mango', 'grapes', 'guava']

#Change the second element of a list into python.
items=['apple','mango','banana','grapes','guava']
items[1]='python'
print(items)
output=['apple', 'python', 'banana', 'grapes', 'guava']

#Reverse a list.
items=['apple','mango','banana','grapes','guava']
items.reverse()
print(items)
output=['guava', 'grapes', 'banana', 'mango', 'apple']

#Check whether the apple is present in a list.
items=['apple','mango','banana','grapes','guava']
print('apple' in items)
output=True

#or
items=['apple','mango','banana','grapes','guava']
if 'apple' in items:
    print("Apple is present in the list. ")
else:
    print("Apple is not present in the list. ")
output=Apple is present in the list.

#Sum all the numbers in the list list1.
list1=[1,2,3,4,5]
print(sum(list1))
output=15

#Remove duplicated items in a list.
items1=['apple','mango','banana','grapes','apple']
items1=list(set(items1))
print(items1)
output=['mango', 'grapes', 'apple', 'banana']

#Print each element of a list using a for loop
items=['apple','mango','banana','grapes','guava']
for i in range(0,5):
    print(items[i])
output=
apple
mango
banana
grapes
guava

#Find the length of a list.
items=['apple','mango','banana','grapes','guava']
print(len(items))
output=5

#Find largest number in a list.
my_list=[1,2,55,89,34,78]
print(max(my_list))
output=89

#Find smallest number in a list.
my_list=[1,2,55,89,34,78]
print(min(my_list))
output=1

#Find how many times 55 appears in list.
my_list=[1,2,55,89,34,78]
print(my_list.count(55))
output=1

#Sort a list in ascending order.
my_list=[1,2,55,89,34,78]
print(sorted(my_list))
output=[1, 2, 34, 55, 78, 89]




