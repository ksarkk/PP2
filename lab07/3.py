import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('The Game3')

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
x = 500
y = 300

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP :
            if (y - 20) <= 25 :
                y = 25
            else : 
                y -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN :
            if (y + 20) >= 575 :
                y = 575
            else : 
                y += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT :
            if (x - 20) <= 25 :
                x = 25
            else : 
                x -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT :
            if (x + 20) >= 975 :
                x = 975
            else : 
                x += 20

    screen.fill('white')
    pygame.draw.circle(screen, 'red', (x, y), 25)

    pygame.display.update()
    clock.tick(60)
    