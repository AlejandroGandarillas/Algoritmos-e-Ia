import pygame
import math
from bullet import Bullet

class Player:
    def __init__(self):
        self.x = 800
        self.y = 1100
        self.size = 50
        self.speed = 2  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 1600 - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < 1200 - self.size:
            self.y += self.speed

    def draw(self, screen):
        points = [
            (self.x, self.y - self.size),  
            (self.x - self.size // 2, self.y),  
            (self.x + self.size // 2, self.y)  
        ]
        pygame.draw.polygon(screen, (0, 255, 0), points)

    def get_position(self):
        return (self.x, self.y)

    def shoot(self):
        return Bullet(self.x, self.y - self.size // 2)
