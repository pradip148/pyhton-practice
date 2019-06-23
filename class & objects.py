""" creating class """
from math import *
class tringle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area_of_tringle(self):
        z=0.5*self.base*self.height
        print("area of tringle is {}".format(z))

    def diagonal_of_tringle(self):
         d=sqrt(self.height**2)
         print(d)

""" creating objects of class tringle """

t1=tringle(2,3)
t2=tringle(4,5)
t1.area_of_tringle()
t2.area_of_tringle()
t1.diagonal_of_tringle()
t2.diagonal_of_tringle()