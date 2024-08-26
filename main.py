# Required imports
import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    # Initialize player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Initialize clock
    clock = pygame.time.Clock()
    dt = 0
    
    # Gameplay loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Close button function
                return
        
        for obj in updatable:
            obj.update(dt)
       
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")    # Paint screen black
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        
        # Limit framerate to 60FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()