import random
import math

class Particle:
    def __init__(self, x, y):
        self.position = [x, y]
        self.velocity = [random.uniform(-0.0001, 0.0001), random.uniform(-0.0001, 0.0001)]  
        self.best_position = list(self.position)
        self.best_value = float('inf')

class PSO:
    def __init__(self, enemies):
        self.enemies = enemies
        self.particles = [Particle(enemy.x, enemy.y) for enemy in enemies]
        self.global_best_position = list(self.particles[0].position)
        self.global_best_value = float('inf')
        self.w = 0.5       
        self.c1 = 1        
        self.c2 = 2        
        self.cohesion_factor = 1
        self.separation_factor = 1
        self.separation_distance = 30

    def update(self, player_position):
        
        if len(self.particles) != len(self.enemies):
            self.particles = [Particle(enemy.x, enemy.y) for enemy in self.enemies]

        for i, particle in enumerate(self.particles):
            current_value = self.fitness(particle.position, player_position, i)
            if current_value is not None and current_value < particle.best_value:
                particle.best_position = list(particle.position)
                particle.best_value = current_value

            if current_value is not None and current_value < self.global_best_value:
                self.global_best_position = list(particle.position)
                self.global_best_value = current_value

            for d in range(2):
                r1 = random.random()
                r2 = random.random()
                cognitive_velocity = self.c1 * r1 * (particle.best_position[d] - particle.position[d])
                social_velocity = self.c2 * r2 * (self.global_best_position[d] - particle.position[d])
                particle.velocity[d] = self.w * particle.velocity[d] + cognitive_velocity + social_velocity
                particle.position[d] += particle.velocity[d]

                
                if particle.position[d] < 0:
                    particle.position[d] = 0
                    particle.velocity[d] *= -1
                    angle = random.uniform(-0.1, 0.1)
                    particle.velocity[1 - d] += angle
                elif particle.position[d] > (1600 if d == 0 else 1200):
                    particle.position[d] = 1600 if d == 0 else 1200
                    particle.velocity[d] *= -1
                    angle = random.uniform(-0.1, 0.1)
                    particle.velocity[1 - d] += angle

            self.enemies[i].update((int(particle.position[0]), int(particle.position[1])))

    def fitness(self, position, player_position, index):
        
        distance_to_player = math.sqrt((position[0] - player_position[0]) ** 2 + (position[1] - player_position[1]) ** 2)

        
        cohesion = 0
        for i, particle in enumerate(self.particles):
            if i != index:
                cohesion += math.sqrt((position[0] - particle.position[0]) ** 2 + (position[1] - particle.position[1]) ** 2)
        if len(self.particles) > 1:
            cohesion /= (len(self.particles) - 1)

        
        separation = 0
        for i, particle in enumerate(self.particles):
            if i != index:
                distance = math.sqrt((position[0] - particle.position[0]) ** 2 + (position[1] - particle.position[1]) ** 2)
                if distance < self.separation_distance:
                    separation += (self.separation_distance - distance)

       
        fitness_value = distance_to_player - self.cohesion_factor * cohesion + self.separation_factor * separation
        return fitness_value
