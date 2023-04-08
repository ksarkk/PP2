import pygame
from sys import exit

#Basic setup
pygame.init()
pygame.display.set_caption('The Game2')
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

#Songs 
songs = ['lab07\The Weeknd - Is There Someone Else (Official Audio).mp3', 'lab07\Bank Account   21 Savage.mp3', 'lab07\Dancing in the Moonlight   Toploader.mp3']
index = 0
song_playing = False

#Space button for start or restart a song
#'P' button for pause\unpause
#Right button for next song 
#Left button for previous song

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            pygame.mixer.music.load(songs[index])
            pygame.mixer.music.play(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p :
            if song_playing :
                pygame.mixer.music.pause()
                song_playing = False
            else :
                pygame.mixer.music.unpause()
                song_playing = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT :
            if index < (len(songs) - 1) : index += 1
            else : index = 0
            pygame.mixer.music.load(songs[index])
            pygame.mixer.music.play(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT :
            if index > 0 : index -= 1
            else : index = (len(songs) - 1)
            pygame.mixer.music.load(songs[index])
            pygame.mixer.music.play(-1)
    
    screen.fill('black')
    pygame.display.update()
    clock.tick(60)