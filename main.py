from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()



    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    field = AsteroidField()

    dt = 0
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")


        [item.draw(screen) for item in drawable]

        for item in updateable:
            if item == player:
                player.timer -= dt
            item.update(dt)

        # [item.update(dt) for item in updateable]

        for item in asteroids:
            if item.collision_check(player):
                print("Game over!")
                exit()

            for shot in shots:
                if shot.collision_check(item):
                    item.split()
                    shot.kill()

        pygame.display.flip()
        dt =  time_clock.tick(120) / 1000



if __name__ == "__main__":
    main()
