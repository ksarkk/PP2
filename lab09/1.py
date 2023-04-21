#Imports
import pygame 
from sys import exit 
from random import randint, choice

#Initializing and Setting name for the game
pygame.init()
pygame.display.set_caption("Racer")

#Background of the game
screen = pygame.display.set_mode((400, 600))
background = pygame.image.load("lab08\AnimatedStreet.png")

#Background Song
back_song = pygame.mixer.Sound('lab08\Background.wav')
back_song.set_volume(0.2)
back_song.play(loops = -1)

crash_sound = pygame.mixer.Sound('lab08\crash.wav')
crash_sound.set_volume(0.2)

#FPS
clock = pygame.time.Clock()
fps = 60

#Needed Variables and Images
game_active = True

speed = 5
car_speed = 5
score = 0
coin_score1 = 0
coin_score2 = 0

coin_png = pygame.image.load('lab08\Mini_coin.png').convert_alpha()
coin_png_rect = coin_png.get_rect(center = (355, 24))

coin_speed_png = pygame.image.load('lab08\Mini_coin_speed.png').convert_alpha()
coin_speed_png_rect = coin_speed_png.get_rect(center = (355, 48))

#Fonts and Text 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over = font.render("Game Over", False, 'Black')

restart = font_small.render('press "space" button to restart', False, 'black')
restart_rect = restart.get_rect(midtop = (200, 320))

#Classes
class Player(pygame.sprite.Sprite) :

    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('lab08\Player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200, 580))

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-car_speed, 0)
        if self.rect.right < 400:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(car_speed, 0)

class Enemy(pygame.sprite.Sprite) :

    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load('lab08\Enemy.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (randint(40, 360), 0))

    def update(self) :
        global score
        self.rect.move_ip(0, speed)

        if game_active :
            if (self.rect.top > 600) :
                score += 1
                self.rect.midbottom = ((randint(40, 360), 0))
        else :
            self.rect.midbottom = ((randint(40, 360), 0))

class Coin(pygame.sprite.Sprite) :

    def __init__(self, type) :
        super().__init__()

        self.type_check = type
        if type == 'score' :
            self.image = pygame.image.load('lab08\coin_score.png').convert_alpha()
        else :
            self.image = pygame.image.load('lab08\coin_speed.png').convert_alpha()

        self.rect = self.image.get_rect(center = (randint(20, 380), 530))

    def update(self) :
        global score, car_speed, coin_score2, coin_score1, speed
        if collision_with_coin() :
            if self.type_check == 'score' :
                coin_score1 += 1
                if coin_score1 == 5 :
                    speed += 1
                score += 5
            else : 
                coin_score2 += 1
                if coin_score2 == 5 :
                    speed += 1
                score += 1
                car_speed += 1

#Setting functions for collision
def collision_with_enemy() :
    if pygame.sprite.spritecollide(player.sprite, enemy, False) :
        crash_sound.play(loops=0)
        return False
    else : return True

def collision_with_coin() :
    if pygame.sprite.spritecollide(player.sprite, coin, True) : return True
    else : return False

#Function for screen after GAMEOVER   
def gameover() :
    screen.fill('red')
    screen.blit(game_over, (30, 250))
    screen.blit(restart, restart_rect)

#Setting Classes
player = pygame.sprite.GroupSingle()
player.add(Player())

enemy = pygame.sprite.Group()
enemy.add(Enemy())

coin = pygame.sprite.Group()

#Timers
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

coin_appear = pygame.USEREVENT + 2
pygame.time.set_timer(coin_appear, 5000)

#Main Loop
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : #Quit button
            pygame.quit()
            exit()
        if event.type == inc_speed : #Increasing speed for enemy
            speed += 0.2
        if event.type == coin_appear :
            coin.empty()
            coin.add(Coin(choice(['score', 'score', 'speed'])))
        if not game_active : #Setting Restart 
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    enemy.update()
                    coin.empty()
                    game_active = True
                    score = 0
                    coin_score1 = 0
                    coin_score2 = 0
                    speed = 5
                    car_speed = 5
    
    if game_active :

        screen.blit(background, (0, 0))

        #Showing score on screen
        scores = font_small.render(str(score), True, 'black')
        screen.blit(scores, (10, 10))

        coin_scores = font_small.render(str(coin_score1), True, 'black')
        screen.blit(coin_scores, (370, 10))
        screen.blit(coin_png, coin_png_rect)

        coin_speed_scores = font_small.render(str(coin_score2), True, 'black')
        screen.blit(coin_speed_scores, (370, 34))
        screen.blit(coin_speed_png, coin_speed_png_rect)

        player.draw(screen)
        player.update()

        enemy.draw(screen)
        enemy.update()

        coin.draw(screen)
        coin.update()

        game_active = collision_with_enemy()

    else : gameover()
         
    pygame.display.update()
    clock.tick(fps)