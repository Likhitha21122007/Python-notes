#Create a set with the values {10,20,30,40,50} and print it
s= {10,20,30,40,50}
print(s)

#Create a set from a list [1,2,2,3,4,4,5] and print the result.
my_list=[1,2,2,3,4,4,5]
my_set=set(my_list)
print(my_set)

#Add an element 60 to a set s.
s= {10,20,30,40,50}
s.add(60)
print(s)

#Add multiple element {70,80,90} to that set.
s= {10,20,30,40,50}
s.update({70,80,90})
print(s)

#Remove the element 30 from a set
s= {10,20,30,40,50}
s.remove(30)
print(s)

#Remove an element using discard().
s= {10,20,30,40,50}
s.discard(40)
print(s)

#Remove and return a random element using pop().
s= {10,20,30,40,50}
s.pop()
print(s)

#Find the union of two sets.
s1={1,2,3}
s2={4,5,6}
print(s1|s2)

#OR
s1={1,2,3}
s2={4,5,6}
print(s1.union(s2))


#Find the intersection of two sets.
s1={1,2,3,4}
s2={4,5,6}
print(s1.intersection(s2))

#Find the difference between 2 sets.
s1={1,2,3,4}
s2={4,5,6}
print(s1.difference(s2))

#Find the symmetric difference between two sets.
s1={1,2,3,4}
s2={4,5,6}
print(s1.symmetric_difference(s2))

#Check is one set is a subset of another.
s1={1,2,3,4}
s2={4,5,6}
print(s1.issubset(s2))

#Check if one set is super set of another.
s1={1,2,3,4}
s2={4,5,6}
print(s1.issuperset(s2))

#Check whether two sets are disjoint.
s1={1,2,3,4}
s2={4,5,6}
print(s1.isdisjoint(s2))

#Copy one set to another.
s1={1,2,3,4}
s2=s1.copy()
print(s2)

#Convert list into sets.
list1=[1,2,3,4]
set3=set(list1)
print(set3)

#Convert set into list.
number={10,20,30,89,90}
my_list=list(number)
print(my_list)

#Find maximum and minimum numbers.
number={10,20,30,89,90}
print("Maximum=",max(number))
print("Minimum=",min(number))

#Print all the elements in a list using for loop.
number={10,20,30,89,90}
for i in number:
    print(i)

#Create a frozen set.
My_set=frozenset({10,20,30,40})
print(My_set)

