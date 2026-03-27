set1 = {1,2,2,3,3,3,4,4,4,4,5,5,5,5,5}
print(set1)

set1.add(6)
print(set1)

set2 = {2,4,6,8,10}

#Union
print(set1.union(set2))

#Intersection
print(set1.intersection(set2))

#Difference
print(set1.difference(set2))

#Symmetric Difference
print(set1.symmetric_difference(set2))