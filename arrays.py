from array import *
"""vals=array('i',[ 8,5,6,7,4 ])
newarray=array(vals.typecode,(b for b in vals))
print(newarray)
print(id(vals))
print(id(newarray))"""


""" taking values from user"""

arr= array('i',[])
n=int(input("enter length of array "))
for i in range(n):
    a=int(input("enter the value"))
    arr.append(a)
print(arr)

""" printing the index 

n1=int(input("enter the value which is in array"))
for i in range (n):
    if n1==arr[i]:
        print(i)
    else:
        print(" given value is not present in array ")


  creat array with 5 values and delete value at index no. 2 , without using built-in function 


for i in range (n):
    if arr[2]!=arr[i]:
        print(arr[i]) 

revese the array without using built-in function """
rearr=array('i',[])
for i in range (1,n+1):
    x=(arr[n-i])
    rearr.append(x)
print(rearr)
