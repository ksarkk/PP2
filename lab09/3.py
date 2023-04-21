from turtle import position
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    screen.fill((255, 255, 255))

    rhomb = pygame.image.load('lab09\Rhomb.png').convert_alpha()
    right_tr = pygame.image.load('lab09\Right_triangle.png').convert_alpha()
    equal_tr = pygame.image.load('lab09\eq_trl.png').convert_alpha()
    square = pygame.image.load('lab09\square.png').convert_alpha()

    isMouseDown = False

    drawing_rect = False
    drawing_circle = False
    drawing_pen = True
    drawing_rhomb = False
    drawing_right_tr = False
    drawing_equal_tr = False
    drawing_square = False

    colour = (0, 0, 0)

    while True:
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1 :
                    drawing_rect = True
                    drawing_circle = False
                    drawing_pen = False
                    drawing_rhomb = False
                    drawing_right_tr = False
                    drawing_equal_tr = False
                    drawing_square = False
                elif event.key == pygame.K_2 :
                    drawing_rect = False
                    drawing_circle = True
                    drawing_pen = False
                    drawing_rhomb = False
                    drawing_right_tr = False
                    drawing_equal_tr = False
                    drawing_square = False
                elif event.key == pygame.K_3 :
                    drawing_rect = False
                    drawing_circle = False
                    drawing_pen = True
                    drawing_rhomb = False
                    drawing_right_tr = False
                    drawing_equal_tr = False
                    drawing_square = False
                elif event.key == pygame.K_4 :
                    drawing_rect = False
                    drawing_circle = False
                    drawing_pen = False
                    drawing_rhomb = True
                    drawing_right_tr = False
                    drawing_equal_tr = False
                    drawing_square = False
                elif event.key == pygame.K_5 :
                    drawing_rect = False
                    drawing_circle = False
                    drawing_pen = False
                    drawing_rhomb = False
                    drawing_right_tr = True
                    drawing_equal_tr = False
                    drawing_square = False
                elif event.key == pygame.K_6 :
                    drawing_rect = False
                    drawing_circle = False
                    drawing_pen = False
                    drawing_rhomb = False
                    drawing_right_tr = False
                    drawing_equal_tr = True
                    drawing_square = False
                elif event.key == pygame.K_7 :
                    drawing_rect = False
                    drawing_circle = False
                    drawing_pen = False
                    drawing_rhomb = False
                    drawing_right_tr = False
                    drawing_equal_tr = False
                    drawing_square = True
                elif event.key == pygame.K_b :
                    colour = (0, 0, 255)
                elif event.key == pygame.K_r :
                    colour = (255, 0, 0)
                elif event.key == pygame.K_g :
                    colour = (0, 255, 0)
                elif event.key == pygame.K_e :
                    colour = (255, 255, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

                if drawing_rhomb :
                    rhomb_rect = rhomb.get_rect(center = (currentX, currentY))
                    screen.blit(rhomb, rhomb_rect)
                if drawing_right_tr :
                    right_tr_rect = right_tr.get_rect(center = (currentX, currentY))
                    screen.blit(right_tr, right_tr_rect)
                if drawing_equal_tr :
                    equal_tr_rect = equal_tr.get_rect(center = (currentX, currentY))
                    screen.blit(equal_tr, equal_tr_rect)
                if drawing_square :
                    square_rect = square.get_rect(center = (currentX, currentY))
                    screen.blit(square, square_rect)



            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and drawing_rect:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.rect(screen, colour, r, 1)

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and drawing_circle:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX, prevY, currentX, currentY)
            pygame.draw.ellipse(screen, colour, r, 1)

        if isMouseDown and drawing_pen:
            pygame.draw.line(screen, colour, (prevX, prevY), (currentX, currentY))
            prevX = currentX
            prevY = currentY
        

        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


main()