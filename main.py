import pygame
from player import Player
from enemy import Enemy
from pso import PSO
from bullet import Bullet


pygame.init()


screen = pygame.display.set_mode((1600, 1200))  
pygame.display.set_caption("Space Invaders con PSO")

player = Player()

enemies = [Enemy(player_position=(player.x, player.y)) for _ in range(50)]  
pso = PSO(enemies)

bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(player.shoot())

    player.update()
    pso.update(player.get_position())
 
    for bullet in bullets:
        bullet.update()
    
    for bullet in bullets:
        for enemy in enemies:
            if enemy.collide_with(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    bullets = [bullet for bullet in bullets if bullet.y > 0]

    screen.fill((0, 0, 0))
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.flip()

pygame.quit()
