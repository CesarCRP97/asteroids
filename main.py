import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    dt = 0

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids_objects = AsteroidField()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #update all objects in updatables
        updatables.update(dt)

        for ast in asteroids:
            if player.is_colliding(ast):
                print("Game Over!")
                sys.exit()

        for d in drawables:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000







if __name__ == "__main__":
    main()
