mylist=[]
elements=[10, 20, 30, 40]
#append element to mylist
for element in elements:
    mylist.append(element)
#insert 15 to second position
mylist.insert(1, 15)
#extend to mylist
mylist.extend([50, 60, 70])
#remove the last element from mylist
mylist.pop()
#sort mylist in ascending order
mylist.sort()
#print the index of value 30 in mylist
print(mylist.index(30))
