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
line = pygame.Rect((875,0,10,1000))

hitbox_p1_1 = pygame.Rect((51,600,30,50))
hitbox_p1_2 = pygame.Rect((51,550,30,50))
hitbox_p1_3 = pygame.Rect((51,500,30,50))

hitbox_p2_1 = pygame.Rect((1649,600,30,50))
hitbox_p2_2 = pygame.Rect((1649,550,30,50))
hitbox_p2_3 = pygame.Rect((1649,500,30,50))

hitbox_p1_bottom = pygame.Rect((51,650,30,3))
hitbox_p1_top= pygame.Rect((51,499,30,3))

hitbox_p2_bottom = pygame.Rect((1649,650,30,3))
hitbox_p2_top = pygame.Rect((1649,499 ,30,3))


Ballx = 2
Bally = 0
p1_points = 0
p2_points = 0

score_increment = 1

ballpos_y = 500
ballpos_x = 875
Point = False



text_font = pygame.font.SysFont("Arial", 100)

def draw_text(p1_points,font,text_col,x,y):
    img = font.render(p1_points,True,text_col)
    screen.blit(img,(x,y))
text_font2 = pygame.font.SysFont("Arial", 100)

def draw_text(p2_points,font,text_col,x,y):
    img = font.render(p2_points,True,text_col)
    screen.blit(img,(x,y))
    
text_font3 = pygame.font.SysFont("Arial", 300)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))
    
                      
    




while run:
    
    if p1_points < 10 or p2_points < 10:

        if ballpos_y == 500 and ballpos_x == 875:
            Point = False
            

        

        screen.fill("black")

        draw_text(str(p1_points), text_font, (255,255,255), 730, 0)
        draw_text(str(p2_points), text_font2, (255,255,255), 1000, 0)

    
        pygame.draw.rect(screen,"white", player1)
        pygame.draw.rect(screen,"white", player2)
        pygame.draw.rect(screen,"white", ball)
        pygame.draw.rect(screen,"white", line)


            
        pygame.draw.rect(screen,"white", hitbox_p1_1)
        pygame.draw.rect(screen,"white", hitbox_p1_2)
        pygame.draw.rect(screen,"white", hitbox_p1_3)
        pygame.draw.rect(screen,"white", hitbox_p2_1)
        pygame.draw.rect(screen,"white", hitbox_p2_2)
        pygame.draw.rect(screen,"white", hitbox_p2_3)

        pygame.draw.rect(screen,"white", hitbox_p2_top)
        pygame.draw.rect(screen,"white", hitbox_p2_bottom)

        pygame.draw.rect(screen,"white", hitbox_p1_top)
        pygame.draw.rect(screen,"white", hitbox_p1_bottom)

        key = pygame.key.get_pressed()


            


        if key[pygame.K_w] == True:
            if y >= 1000:
                pass
            else:
                player1.move_ip(0,-2)
                hitbox_p1_1.move_ip(0,-2)
                hitbox_p1_2.move_ip(0,-2)
                hitbox_p1_3.move_ip(0,-2)
                hitbox_p1_top.move_ip(0,-2)
                hitbox_p1_bottom.move_ip(0,-2)

                    
                y = y+2
                    
        if key[pygame.K_s] == True:
            if y <= 150:
                pass
            else:
                player1.move_ip(0,2)
                y = y-2
                hitbox_p1_1.move_ip(0,2)
                hitbox_p1_2.move_ip(0,2)
                hitbox_p1_3.move_ip(0,2)
                hitbox_p1_top.move_ip(0,2)
                hitbox_p1_bottom.move_ip(0,2)

            

        if key[pygame.K_i] == True:
            if y2 >= 1000:
                pass
            else:


                player2.move_ip(0,-2)
                hitbox_p2_1.move_ip(0,-2)
                hitbox_p2_2.move_ip(0,-2)
                hitbox_p2_3.move_ip(0,-2)
                hitbox_p2_top.move_ip(0,-2)
                hitbox_p2_bottom.move_ip(0,-2)

                y2 = y2+2
                    
        if key[pygame.K_k] == True:
            if y2 <= 150:
                pass
            else:
                player2.move_ip(0,2)
                hitbox_p2_1.move_ip(0,2)
                hitbox_p2_2.move_ip(0,2)
                hitbox_p2_3.move_ip(0,2)
                hitbox_p2_top.move_ip(0,2)
                hitbox_p2_bottom.move_ip(0,2)

                y2 = y2-2



        if ball.colliderect(hitbox_p1_1):   
            Ballx = 2
            Bally = 2
            
        elif ball.colliderect(hitbox_p1_2):
            Ballx = 2
            Bally = 0
            
        elif ball.colliderect(hitbox_p1_3):
            Ballx = 2
            Bally = -2
            
        elif ball.colliderect(hitbox_p2_1):
            Ballx = -2
            Bally = 2
            
        elif ball.colliderect(hitbox_p2_2):
            Ballx = -2
            Bally = 0
            
        elif ball.colliderect(hitbox_p2_3):
            Ballx = -2
            Bally = -2
            


        elif ball.colliderect(hitbox_p2_3)and ball.colliderect(hitbox_p2_bottom):
            Ballx = -2
            Bally = -2
            
        elif ball.colliderect(hitbox_p2_1)and ball.colliderect(hitbox_p2_top):
            Ballx = -2
            Bally = 2

        elif ball.colliderect(hitbox_p1_3)and ball.colliderect(hitbox_p2_bottom):
            Ballx = 2
            Bally = -2
            
        elif ball.colliderect(hitbox_p1_1)and ball.colliderect(hitbox_p2_top):
            Ballx = 2
            Bally = 2




        elif ball.colliderect(hitbox_p2_bottom):
            Ballx = -2
            Bally = -3
            
        elif ball.colliderect(hitbox_p2_top):
            Ballx = -2
            Bally = -3

        elif ball.colliderect(hitbox_p1_bottom):
            Ballx = 2
            Bally = 3
            
        elif ball.colliderect(hitbox_p1_top):
            Ballx = 2
            Bally = -3
                    
                    


            

        if Ballx == 2:
            ballpos_x = ballpos_x + 2
        if Ballx == -2:
            ballpos_x = ballpos_x - 2 
        if Bally == 2:
            ballpos_y = ballpos_y + 2
        if Bally == -2:
            ballpos_y = ballpos_y - 2

        if Bally == 3:
            ballpos_y = ballpos_y + 3
        if Bally == -3:
            ballpos_y = ballpos_y - 3


        if ballpos_y >= 970:
            Bally = Bally*-1
        if ballpos_y <= 0:
            Bally = Bally*-1

        if ballpos_x <= 0 and Point == False:
            ball = pygame.Rect(875,500,30,30)
            Point = True
            Ballx = 2
            Bally = 0
            ballpos_y = 500
            ballpos_x = 875
            for x in range(1,2):
                p2_points = p2_points + score_increment
               

                
        if ballpos_x >= 1750 and Point == False:
            Point = True
            ball = pygame.Rect(875,500,30,30)
            Ballx = 2
            Bally = 0
            ballpos_y = 500
            ballpos_x = 875
            for x in range(1,2):
                p1_points = p1_points + score_increment
                
                
            

                
            
            

            

        ball.move_ip(Ballx,Bally)


        if p1_points >= 10:
            screen.fill("black")
            draw_text(("Player1 WINS"), text_font3, (255,255,255), 100, 300)
                
        if p2_points >= 10:
            screen.fill("black")
            draw_text(("Player2 WINS"), text_font3, (255,255,255), 100, 300)
              
            
            


           

                    
                        
                           
                
       

        
        
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
    pygame.display.update()
pygame.quit()
