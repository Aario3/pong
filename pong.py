import pygame
import random


pygame.init()

run = True
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1750

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT ))
y = 500
y2 = 500

player1 = pygame.Rect((50,500,30,150))
player2 = pygame.Rect((1650,500,30,150))
ball = pygame.Rect((875,500,30,30))

hitbox_p1_1 = pygame.Rect((49,600,30,50))
hitbox_p1_2 = pygame.Rect((49,550,30,50))
hitbox_p1_3 = pygame.Rect((49,500,30,50))
hitbox_p2_1 = pygame.Rect((1651,600,30,50))
hitbox_p2_2 = pygame.Rect((1651,550,30,50))
hitbox_p2_3 = pygame.Rect((1651,500,30,50))

Ballx = 1
Bally = 0

ballpos_y = 500
ballpos_x = 850

rrandom = 1
collide = 1



 #make 3 hitboxes for each side and which hitbox it hits is whe re ball y goes

while run:
    screen.fill("black")

    pygame.draw.rect(screen,"white", player1)
    pygame.draw.rect(screen,"white", player2)
    pygame.draw.rect(screen,"white", ball)
    pygame.draw.rect(screen,"white", hitbox_p1_1)
    pygame.draw.rect(screen,"white", hitbox_p1_2)
    pygame.draw.rect(screen,"white", hitbox_p1_3)
    pygame.draw.rect(screen,"white", hitbox_p2_1)
    pygame.draw.rect(screen,"white", hitbox_p2_2)
    pygame.draw.rect(screen,"white", hitbox_p2_3)
    key = pygame.key.get_pressed()


    


    if key[pygame.K_w] == True:
        if y == 1000:
            pass
        else:
            player1.move_ip(0,-1)
            hitbox_p1_1.move_ip(0,-1)
            hitbox_p1_2.move_ip(0,-1)
            hitbox_p1_3.move_ip(0,-1)
            
            y = y+1
            
    if key[pygame.K_s] == True:
        if y == 150:
            pass
        else:
            player1.move_ip(0,1)
            y = y-1
            hitbox_p1_1.move_ip(0,1)
            hitbox_p1_2.move_ip(0,1)
            hitbox_p1_3.move_ip(0,1)

    

    if key[pygame.K_i] == True:
        if y2 == 1000:
            pass
        else:
            player2.move_ip(0,-1)
            hitbox_p2_1.move_ip(0,-1)
            hitbox_p2_2.move_ip(0,-1)
            hitbox_p2_3.move_ip(0,-1)

            y2 = y2+1
            
    if key[pygame.K_k] == True:
        if y2 == 150:
            pass
        else:
            player2.move_ip(0,1)
            hitbox_p2_1.move_ip(0,1)
            hitbox_p2_2.move_ip(0,1)
            hitbox_p2_3.move_ip(0,1)

            y2 = y2-1



    if ball.colliderect(hitbox_p1_1):   
        Ballx = 1
        Bally = -1
    elif ball.colliderect(hitbox_p1_2):
        Ballx = 1
        Bally = 0
    elif ball.colliderect(hitbox_p1_3):
        Ballx = 1
        Bally = 1
    elif ball.colliderect(hitbox_p2_1):
        Ballx = -1
        Bally = 1   
    elif ball.colliderect(hitbox_p2_2):
        Ballx = -1
        Bally = 0  
    elif ball.colliderect(hitbox_p2_3):
        Ballx = -1
        Bally = -1
            
            


    

    if Ballx == 1:
        ballpos_x = ballpos_x + 1
    if Ballx == -1:
        ballpos_x = ballpos_x - 1
    if Bally == 1:
        ballpos_y = ballpos_y + 1
    if Bally == -1:
        ballpos_y = ballpos_y - 1

    if ballpos_y == 1000:
        Bally = -1
    if ballpos_y == 0:
        Bally = 1

    

    ball.move_ip(Ballx,Bally)
    
    


   

            
                
                   
        
       

        
        
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
    pygame.display.update()
pygame.quit()
