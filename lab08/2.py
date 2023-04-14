#Imports
import pygame, sys
from pygame.math import Vector2 #Vector2 is a very useful tool to wotk with vectors
from random import randint

#Classes
class Fruit() :

    def __init__(self) :
        self.x = randint(0, CELL_NUMBER - 1)
        self.y = randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self) :
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        SCREEN.blit(fruit, fruit_rect)

    def random(self) :
        self.x = randint(0, CELL_NUMBER - 1)
        self.y = randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

class Snake() :

    def __init__(self) :
        self.body = [Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self) :
        for block in self.body :
            rect = pygame.Rect(block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, ('blue'), rect)

    def move_snake(self) :
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

class Wall() :

    def __init__(self, level):
        self.body_wall = []
        f = open("lab08/level{}.txt".format(level), "r")
        
        for y in range(0, HEIGHT//CELL_SIZE + 1):
            for x in range(0, WIDTH//CELL_SIZE + 1):
                if f.read(1) == '#':
                    self.body_wall.append(Vector2(x, y))

    def draw_wall(self):
        for point in self.body_wall :
            rect = pygame.Rect(CELL_SIZE * point.x, CELL_SIZE * point.y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

#Main class that contains all of 3 previous classes
class Main() :

    def __init__(self) :
        self.snake = Snake()
        self.fruit = Fruit()
        self.wall = Wall(level_count)

    def update(self) :
        self.snake.move_snake()
        self.collision_food()
        self.die_snake()

    def draw_elements(self) :
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.wall.draw_wall()

    def collision_food(self) :
        global SCORE
        if self.fruit.pos == self.snake.body[0] :
            self.snake.body.insert(len(self.snake.body), self.snake.body[1])
            self.fruit.random()
            SCORE += 1
        
    def check_wall(self) :
        for block in self.wall.body_wall :
                if self.fruit.pos == block :
                    while self.fruit.pos != block :
                        self.fruit.random()

    def die_snake(self) :
        if not 0 <= self.snake.body[0].x < CELL_NUMBER :
            self.game_over()
        elif not 0 <= self.snake.body[0].y < CELL_NUMBER :
            self.game_over()

        for block in self.snake.body[1:] :
            if block == self.snake.body[0] :
                self.game_over()

        for wall in self.wall.body_wall :
            if wall == self.snake.body[0] :
                self.game_over()
    
    def game_over(self) :
        pygame.quit()
        sys.exit()

#Basic Variables
HEIGHT = 400
WIDTH = 400
CELL_SIZE = 20
CELL_NUMBER = 20
SCORE = 0
level_count = 0
snake_speed = 200

#Initializing and Setting name for the game
pygame.init()
pygame.display.set_caption('Snake')

#FPS
CLOCK = pygame.time.Clock()
FPS = 60

#Main screen, font and images
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
font_ = pygame.font.SysFont("Verdana", 20)
fruit = pygame.image.load('lab08\Apple_Snake.png').convert_alpha()

#Setting up main class
main = Main()

#Timer
snake_movement = pygame.USEREVENT 
pygame.time.set_timer(snake_movement, snake_speed)

#Main Loop
while True:
    for event in pygame.event.get(): #Quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == snake_movement : #Snake movement over a time
            main.update()
        if event.type == pygame.KEYDOWN : #Setting up buttons on keyboard to play
            if event.key == pygame.K_UP :
                if main.snake.direction.y != 1 :
                    main.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN :
                if main.snake.direction.y != -1 :
                    main.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT :
                if main.snake.direction.x != -1 :
                    main.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT :
                if main.snake.direction.x != 1 :
                    main.snake.direction = Vector2(-1, 0)
    
    if SCORE == 5 : #Changing the speed for snake, next level and checking for walls
        SCORE = 0
        level_count += 1
        if level_count == 3 :
            level_count = 0
        main.wall = Wall(level_count)
        main.check_wall()
        main.snake = Snake()
        snake_speed -= 20

    SCREEN.fill('#558b2f')
    main.draw_elements()

    #Showing score on screen
    scores = font_.render(str(SCORE), True, 'black')
    SCREEN.blit(scores, (10, 10))

    pygame.display.update()
    CLOCK.tick(FPS)