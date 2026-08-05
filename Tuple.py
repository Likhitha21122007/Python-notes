#Create a tuple containing 10,20,30,40.
my_tuple=(10,20,30,40)
print(my_tuple)

#Print the first element of a tuple.
my_tuple=(10,20,30,40)
print(my_tuple[0])

#Print last element of a tuple.
my_tuple=(10,20,30,40)
print(my_tuple[-1])

#length of the tuple.
my_tuple=(10,20,30,40)
print(len(my_tuple))

#Check whether 50 is present in the tuple (10,20,30,40,50).
tuple1=(10,20,30,40,50)
print(50 in tuple1)

#OR
tuple1=(10,20,30,40,50)
if 50 in tuple1:
    print("50 is present in tuple1")
else:
    print("50 is not present in tuple1")

#count how many times 2 appears in (1,2,2,3,2,4).
numbers=(1,2,2,3,2,4)
print(numbers.count(2))

#Convert the list [100,200,300] into tuple.
list1=[100,200,300]
tuple=tuple(list1)
print(tuple)

#find the index of 30 in (10,20,30,40,50).
Num=(10,20,30,40,50)
print(Num.index(30))

#Concatenate(1,2,3) and (4,5,6).
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)

#Repeat the tuple "Hi" three times.
tup=("Hi ")
print(tup*3)

#Slice the tuple (10,20,30,40,50) to get (20,30,40).
Tup=(10,20,30,40,50)
print(Tup[1:4])

#convert the tuple (10,0,30,40,50) into list.
Tup=(10,20,30,40,50)
my_list=list(Tup)
print(my_list)

#Unpack the tuple (1000,200,300) into three variables and print them.
number=(1000,200,300)
p,q,r=number
print(p)
print(q)
print(r)

#Sum of all elements in tuple (5,10,15,20).
Tup1=(5,10,15,20)
print(sum(Tup1))

#Create a tuple of 5 fruits and print each fruit using a for loop.
fruits=('apple','banana','grapes','guava','orange')
for i in fruits:
    print(i)

#count how many even numbers present in (2,3,8,11,14,17,20).
num1=(2,3,8,11,14,17,20)
count=0
for i in num1:
    if i%2==0:
        count+=1
print(count)

#Reverse the tuple (2,3,8,11,14,17,20) usimg slicing.
tuple2=(2,3,8,11,14,17,20)
print(tuple2[::-1])

#Create a nested tuple ((1,2),(3,4),(5,6)) and print 4.
tuple2=((1,2),(3,4),(5,6)) 
print(tuple2[1][1])
