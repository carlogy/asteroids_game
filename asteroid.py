from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        r_angle = random.uniform(20,50)
        vector_A = self.velocity.rotate(r_angle)
        vector_B = self.velocity.rotate(-r_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroidA = Asteroid(self.position.x, self.position.y, new_radius)
        asteroidB = Asteroid(self.position.x, self.position.y, new_radius)

        asteroidA.velocity = vector_A * 1.2
        asteroidB.velocity = vector_B * 1.2
