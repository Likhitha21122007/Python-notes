#Create a list of fruits and print it.
items=['apple','mango','banana','grapes','guava']
print(items)

#Create a list of a 5 numbers and print 1st and last element.
list1=[1,2,3,4,5]
print(list[0],list[4]) 

#Add Orange to the fruit list.
items=['apple','mango','banana','grapes','guava']
items.append("orange")
print(items)

#Remove banana from fruit list.
items=['apple','mango','banana','grapes','guava']
items.remove("banana")
print(items)

#Change the second element of a list into python.
items=['apple','mango','banana','grapes','guava']
items[1]='python'
print(items)

#Reverse a list.
items=['apple','mango','banana','grapes','guava']
items.reverse()
print(items)

#Check whether the apple is present in a list.
items=['apple','mango','banana','grapes','guava']
print('apple' in items)
#or
items=['apple','mango','banana','grapes','guava']
if 'apple' in items:
    print("Apple is present in the list. ")
else:
    print("Apple is not present in the list. ")

#Sum all the numbers in the list list1.
list1=[1,2,3,4,5]
print(sum(list1))

#Remove duplicated items in a list.
items1=['apple','mango','banana','grapes','apple']
items1=list(set(items1))
print(items1)

#Print each element of a list using a for loop
items=['apple','mango','banana','grapes','guava']
for i in range(0,5):
    print(items[i])

#Find the length of a list.
items=['apple','mango','banana','grapes','guava']
print(len(items))

#Find largest number in a list.
my_list=[1,2,55,89,34,78]
print(max(my_list))


#Find smallest number in a list.
my_list=[1,2,55,89,34,78]
print(min(my_list))

#Find how many times 55 appears in list.
my_list=[1,2,55,89,34,78]
print(my_list.count(55))

#Sort a list in ascending order.
my_list=[1,2,55,89,34,78]
print(sorted(my_list))




