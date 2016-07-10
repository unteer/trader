
#Mike Joyce

from math import *
from random import *
from graphics import *

class Planet:
    """Class to take in data about each planet"""

    def __init__(self,sun,radius,mplanet,win):
        """constructor to take in info about each planet"""
        self.sun=sun
        self.radius=radius
        self.mplanet=mplanet
        self.win=win
        self.period=self.Period(self.sun,self.mplanet)
        self.color='blue'
        self.x=0.1
        self.y=0.1
        self.theta=0

    def Period(self,sun,mplanet):
        """method to calculate the orbital period of the planet"""
        #uses Newton's Version of Kepler's 3rd Law to calculate the period
        #of the planet
        masstot=self.sun*(1.99*10**30)+self.mplanet*(5.972*10**24)
        distance=self.radius*1.496*10**11
        seconds=sqrt(4*(pi**2)*(distance**3)/((6.67*10**-11)*masstot))
        #this formula calculate the period in seconds so it is then turned into
        #years for convenience
        period=seconds/(3.156*10**7)
        return period

    def Scale(self,radius,mplanet):
        """method to create the scale comparing the sizes and distances"""
        #the size and distance away from the sun are set to scale for the graphics
        #based on the mass of the planet and the radius given
        dist=self.radius*10
        size=5*self.mplanet
        return dist,size

    def Color(self):
        """method to determine the color of the planet"""
        #reads through a list of colors from a file
        #file=open("Color.txt","r").read()
        #lst=file.split("\n")
        #num=randrange(0,28)
        #randomly chooses a color from the list
        #for i in lst:
        #    color=lst[num]
        return (0,0,255)

    def Theta(self):
        """method to find the angles the planet will turn based on each period"""
        #calculate the initial angle based on the period dividing it will result in
        #1 revolution will equal to 2*pi. The extra constant is to control the speed
        #that the planet moves
        theta1=(2*pi)/(self.period*365)*15
        #the theta is then transferred to the Move module
        self.Move(self.theta)
        #theta is then increased as to keep moving in a circle
        self.theta=self.theta+theta1

    def Move(self,theta):
        """method to move the planets according to their period"""
        #the previous circle is undrawn
        self.circ.undraw()
        #the coordinates of the new circle are calculated based on the theta given
        x=-self.radius*10*cos(theta)
        y=self.radius*10*sin(theta)
        #the new circle is drawn based on these new coordinates
        self.circ=Circle(Point(x,y),(5*self.mplanet))
        self.circ.setFill(self.color)
        self.circ.draw(self.win)
            
    def PrintInfo(self):
        """method to print the information for the planet"""
        #gives the mass, radius, an period for each planet
        print("\tMass: {0:0.1f}".format(self.mplanet),"Earth masses","\n\tRadius: ",self.radius,"AU","\n\tPeriod: {0:0.1f}".format(self.period),"years","\n")

    def DrawP(self):
        """method to draw the planet and its distance from the Sun"""
        #this draws the planet with it initially being left of the sun
        dist,size=self.Scale(self.radius,self.mplanet)
        self.circ=Circle(Point(0+dist,0),size)
        self.circ.setFill(self.color)
        self.circ.draw(self.win)
