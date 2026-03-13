import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        log_event("asteroid_split")
        angle = random.uniform(20,30)
        new_vec1 = self.velocity.rotate(angle)
        new_vec2 = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x,self.position.y,new_rad)
        ast2 = Asteroid(self.position.x,self.position.y,new_rad)
        ast1.velocity = new_vec1 *1.2
        ast2.velocity = new_vec2 *1.2
        self.kill()
        return