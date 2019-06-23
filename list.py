#list=[]
#print(list)
#print(type(list))

#printing elemrnt from list

a=[1,2,3,4,5,6,7,8,]
for i in a:
    print(i)
print("-----------------")

for i in range (len(a)):
    print(a[i])

print(len(a))

print(a[2])
print(a[7])

''' replaceing values '''


a[1]=9
a[2]=10
print(a)

''' adding element in list (append) this will add values at the end '''

a.append(11)
a.append(12)
print(a)

''' adding element at given index (insert) '''

a.insert(2,55)
a.insert(0,111)
print(a)

''' adding two list (extend) '''

c=[11,121,122,123]
a.extend(c)
print(a)
b=[50,51,52,53,54,55]
a.extend(b)
print(a)

''' copy of list '''
c=a.copy()
print(c)

''' (del) deleting values by providing index '''
del a[2]
del a[5]
print(a)

''' (remove) deleting direct values '''
a.remove(55)
a.remove(122)
print(a)

''' reverseing list '''
a.reverse()
print(a)

z=[12111,1,2,22,330]
z[::-1]
print(z)
