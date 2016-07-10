import pygame, sys,  random
from pygame.locals import *

class Location(object):

    def __init__(self,  name, coords,  inventory=[],  population=0, ships=[],  *args,  **kwargs):
        self.name = name
        self.inventory = inventory
        self.population = population
        self.ships = ships
        self.coords = coords
        
class Planet(Location):

    def __init__(self, name,  coords, star, radius=3, mass=0,  *args,  **kwargs):
       Location.__init__(self,  name,  coords,  *args,  **kwargs)
       self.radius = radius
       self.set_period()
       
    def set_period(self):
        masstot=self.sun*(1.99*10**30)+self.mplanet*(5.972*10**24)
        distance=self.radius*1.496*10**11
        seconds=sqrt(4*(pi**2)*(distance**3)/((6.67*10**-11)*masstot))
        #this formula calculate the period in seconds so it is then turned into
        #years for convenience
        period=seconds/(3.156*10**7)
        return period

class Star(Location):

    def __init__(self, name,  coords, radius=0, mass=1,  *args,  **kwargs):
       Location.__init__(self,  name,  coords,  *args,  **kwargs)
       self.radius = radius
       self.mass = mass

class Ship(object):
    
    def __init__(self,  name,  coords,  speed=1):
        self.coords = coords
        self.speed = speed
        self.name = name
    
class Game(object):

    def __init__(self):
        self.init_pygame()
        self.star = Star('Sol', (int(self.window_width / 2),  int(self.window_height/2)))
        self.planets = self.create_planets()
        self.ships = self.create_ships()
        self.run()
    
    def init_pygame(self):
        pygame.init()
        
        self.fps = 15
        
        ##WINDOW
        self.window_width = 640
        self.window_height = 480
        
        ##COLORS
        self.color_white = (255, 255, 255)
        self.color_black = (  0,   0,   0)
        self.color_red = (255,   0,   0)
        self.color_green = (  0, 255,   0)
        self.color_blue = (0,  0,  255)
        self.color_yellow = (128,  128,  0)
        self.color_dark_green = ( 0, 155,   0)
        self.color_dark_grey = ( 40,  40,  40)
        self.color_bgcolor = self.color_black
        
        pygame.display.set_caption('Trader')
        self.fps_clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((self.window_width, self.window_height))
            
    def create_ships(self):
        ships = {}
        ships["Rouge One"] = Ship("Rogue One",  coords=self.get_random_coords())
        return ships
        
    def create_planets(self):
        planets = {}
        planets["Mercury"] = Planet("Mercury",  self.get_random_coords())
        planets["Venus"] = Planet("Venus",  self.get_random_coords())
        planets["Earth"] = Planet("Earth",  self.get_random_coords())
        planets["Mars"] = Planet("Mars",  self.get_random_coords())
        return planets
        
    def get_random_coords(self):
        return (random.randint(0, self.window_width - 1),  random.randint(0, self.window_height - 1))
        
    def terminate(self):
        pygame.quit()
        sys.exit()

    def draw_planets(self):
        for planet in self.planets.values():
            print("Drawing %s" % planet.name)
            pygame.draw.circle(self.display_surface,  self.color_green,  planet.coords,  10)
    
    def draw_stars(self):
        for star in self.stars.values():
            print("Drawing %s" %  star.name)
            pygame.draw.circle(self.display_surface,  self.color_yellow,  star.coords,  20)
            
    def run(self):
        winCondition = False

        while not winCondition:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
            
            self.display_surface.fill(self.color_bgcolor)
            self.draw_planets()
            self.draw_stars()
            pygame.display.update()
            self.fps_clock.tick(self.fps)

if __name__=='__main__':
    game = Game()
