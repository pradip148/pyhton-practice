""" intersection of  two lists

a=[]
b=[]
c=[]
n=int(input(" enter length of first list"))
for i in range(n):
    x=int(input(" enter value"))
    a.append(x)

print('--------------')

m=int(input(" entr the length of second list "))
for i in range(m):
    y=int(input(" enter value"))
    b.append(y)

print("----------------")

print(a)
print(b)

for i in a:
    if i in (b):
        c.append(i)

print("intersection of list a & list b is {} ".format(c))


#sum of all element in list
#mul of all element in list

sum=0
mul=1
z=[]
n=int(input(" enter length of first list"))
for i in range(n):
    x=int(input(" enter value"))
    z.append(x)

for i in z:
    sum=sum+i
    mul=mul*i
print("sum of all element from list is {}".format(sum))
print("mul of all element from list is {}".format(mul))"""
"""x=[]
y=[]
evencout=0
oddcout=0

a=[1,2,3,4,1,5,6,2,3]
for i in a:
    if i%2==0:
        x.append(i)
        evencout=evencout+1
    else:
        y.append(i)
        oddcout=oddcout+1

print(" even numbers= {}".format(x))
print(" odd numbers ={}".format(y))
print("even count={}".format(evencout))
print("odd count={}".format(oddcout))"""

l=[8,2, 3, 4, 5, 2, 3, 6,5, 6]
print(l)
l[0]=1111
print(l)


"""y=[]
x=[1,2,3,4,5,1,2,5,9,8,7,2,]
t=set(x)
for i in t:
    y.append(i)

print(x)
print(t)
print(type(t))
print(y)
print(type(y))"""




