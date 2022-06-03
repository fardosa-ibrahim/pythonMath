from cmath import pi
import re


class Circle:
    def __init__(self,radius) :
        self.radius=radius

    def Area(self):
        total=self.radius*self.radius
        pi=3.14
        area=total*pi
        return area

    def circumference(self):
        total=2*self.radius
        c=total*pi
        return c


class Squre:
    def __init__(self,side):
        self.side=side


    def AreaOfSqure(self):
        SqureArea=self.side*self.side
        return SqureArea


    def circumference(self):
        perimeter=4*self.side
        return perimeter

class Rectancle:

    def __init__(self,sideOne,sideTwo):
        self.sideOne=sideOne
        self.sideTwo=sideTwo

    def AreaOfRectacle(self):
        rectancleArea=self.sideOne*self.sideTwo
        return rectancleArea


    def perimeter(self):
        perimeterTwo=2(self.sideOne*self.sideTwo)
        return perimeterTwo



class Sphere:
    def __init__(self,Radius):
        self.Radius=Radius
    
    def AreaOfSphere(self):
        areaOfSphere=4*pi*self.Radius*self.Radius
        return areaOfSphere

    def volume(self):
        vlm=4/3(pi*self.Radius*self.Radius*self.Radius)
        return vlm
       




    

            
        
    
    

        
        
    