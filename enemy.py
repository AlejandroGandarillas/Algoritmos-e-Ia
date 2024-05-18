import pygame
import random
import math

class Enemy:
    def __init__(self, player_position):
        self.radius = 10  
        self.x, self.y = self.generate_position_away_from_player(player_position)
        
    def generate_position_away_from_player(self, player_position):
        while True:
            x = random.randint(self.radius, 1600 - self.radius)
            y = random.randint(self.radius, 300)  
            distance = math.sqrt((x - player_position[0]) ** 2 + (y - player_position[1]) ** 2)
            if distance > 200:  
                return x, y

    def update(self, new_position):
        self.x, self.y = new_position

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

    def collide_with(self, bullet):
        distance = math.sqrt((self.x - bullet.x) ** 2 + (self.y - bullet.y) ** 2)
        return distance < self.radius + bullet.size
