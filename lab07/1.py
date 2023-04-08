import pygame
import datetime
from sys import exit

#Basic setup
pygame.init()
pygame.display.set_caption('The Game1') 
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

#Images
micky_clock = pygame.image.load('lab07\main-clock.png').convert_alpha()
right_hand = pygame.image.load('lab07\Right-hand.png').convert_alpha()
right_hand_copy = right_hand
left_hand = pygame.image.load('lab07\left-hand.png').convert_alpha()
left_hand_copy = left_hand

#Current Time
now_time = datetime.datetime.now()
second_delta = 60 - now_time.second
angle_minute = (now_time.minute * -6) + 90
angle_second = (now_time.second * -6) + 90

#Rectangles of images
left_hand = left_hand_copy = pygame.transform.rotate(left_hand, angle_second)
left_hand_rect = left_hand.get_rect(center = (400, 400))

right_hand = right_hand_copy = pygame.transform.rotate(right_hand, angle_minute)
right_hand_rect = right_hand.get_rect(center = (400, 400))

micky_clock_rect = micky_clock.get_rect(center = (400, 400))

#Timer
timer_second = pygame.USEREVENT + 1
pygame.time.set_timer(timer_second, 1000)

timer_second_delta = pygame.USEREVENT + 2
pygame.time.set_timer(timer_second_delta, second_delta * 1000)
delta_bool = True

timer_minute = pygame.USEREVENT + 3

angle_count_sec = 0
angle_count_min = 0

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if event.type == timer_second :
            angle_count_sec -= 6
            left_hand = pygame.transform.rotate(left_hand_copy, angle_count_sec)
            left_hand_rect = left_hand.get_rect(center = (400, 400))
        if delta_bool :
            if event.type == timer_second_delta :
                angle_count_min -= 6
                right_hand = pygame.transform.rotate(right_hand_copy, angle_count_min)
                right_hand_rect = right_hand.get_rect(center = (400, 400))
                timer_minute = pygame.USEREVENT + 3
                pygame.time.set_timer(timer_minute, 60000)
                delta_bool = False
        if event.type == timer_minute :
            angle_count_min -= 6
            right_hand = pygame.transform.rotate(right_hand_copy, angle_count_min)
            right_hand_rect = right_hand.get_rect(center = (400, 400))

    screen.fill('white')
    screen.blit(micky_clock, micky_clock_rect)
    screen.blit(right_hand, right_hand_rect)
    screen.blit(left_hand, left_hand_rect)
    pygame.display.update()
    clock.tick(60)