#Mike Joyce

from FinalPlanet import *
from graphics import *
from time import *

class Solar:
    """Class to create a solar system"""
    def __init__(self,msun,win,planets=[]):
        """defines the parameters"""
        self.msun=msun
        self.win=win
        self.planets=planets
        self.num=len(self.planets)

    def System(self,msun):
        """method to draw the Sun"""
        #creates the space backround
        self.win.setBackground("black")
        #randomly draws stars in the background
        for i in range(100):
            x=randrange(-400,400)
            y=randrange(-400,400)
            star=Circle(Point(x,y),3)
            star.setFill("white")
            star.draw(self.win)
        #draws the sun
        Sun=Circle(Point(0,0),50)
        Sun.setFill("yellow")
        Sun.draw(self.win)

        #draws each planet that is put into the solar system
        for planet in self.planets:
            planet.DrawP()

    def AddPlanet(self,planet):
        """method to add a planet to the list"""
        #adds each planet to the list of planets in the solar system
        self.planets.append(planet)
        self.num=+1        
    
    def Move(self):
        """method to move the planets according to their period"""
        theta=0
        #for each planet in the system, the planet is moved based on the angle
        #calculated from its period
        while True:
            for planet in self.planets:
                planet.Theta()
            sleep(0.01)
            #module checks for when the user clicks to stop the planet movement
            pt=self.win.checkMouse()
            if pt!=None:
                break
               
    def PrintInfoSolar(self):
        """method to print the information for all the planets in the system"""
        #for each of the planets in the solar system, it prints out the mass, radius,
        #and period of each
        i=1
        for planet in self.planets:
            print("Planet",i,":")
            planet.PrintInfo()
            i+=1
            


        
def main():
    #asks the user if they want to put in their own info or use some already selected
    option=input("Would you like to enter your own data (Y or N)?: ")
    if option=="Y":
        #asks the user for the number of planets and the size of the sun
        num=eval(input("How many planets should there be?: "))
        sun=eval(input("What is the mass of the sun (in solar masses)?: "))
        #sets us the graph and the system the planets will be added to
        win=GraphWin("Solar System",800,800)
        win.setCoords(-400,-400,400,400)
        system=Solar(sun,win,[])
        #gets the info for each planet
        for i in range(num):
            mplanet=eval(input("\nWhat is the mass of planet "+str(i+1)+" (in Earth masses)?: "))
            mradius=eval(input("What is the orbital distance of planet "+str(i+1)+"(in AU)?: "))
            #adds the planet to the Planet class and adds it to the system
            planet=Planet(sun,mradius,mplanet,win)
            system.AddPlanet(planet)
        #prints the info for each planet and calls the module to move them
        system.PrintInfoSolar()
        system.System(sun)
        system.Move()
    if option=="N":
        sun=6
        win=GraphWin("Solar System",800,800)
        win.setCoords(-400,-400,400,400)
        system=Solar(sun,win,[])
        #reads in info for some already selected planets
        file=open("Planets.txt","r").read()
        lst=file.split("\n")
        for word in lst:
            i=word.split()
            mplanet=float(i[0])
            mradius=float(i[3])
            planet=Planet(sun,mradius,mplanet,win)
            system.AddPlanet(planet)
        #prints the info for each planet and calls the module to move them
        system.PrintInfoSolar()
        system.System(sun)
        system.Move()
    else:
        print("Invalid Response")
    
        
    
        
main()
