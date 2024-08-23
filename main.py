from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)

    updateable.add(player)
    drawable.add(player)


    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        [item.draw(screen)  for item in drawable ]

        [item.update(dt) for item in updateable]

        pygame.display.flip()
        dt =  time_clock.tick(120) / 1000






if __name__ == "__main__":
    main()
