# import pygame module in this program
import pygame
from playsound import playsound
import pygame, pygame.display , pygame.key , pygame.event ,pygame.draw , pygame.font ,pygame.time , pygame.image, pygame.transform , pygame.rect
from pygame.locals import *
import random
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow= (255,211,0)
score=0
ammo=10
screen_width = 800
screen_height = 600


display_surface = pygame.display.set_mode((screen_width, screen_height ))
game_icon= pygame.image.load(r"C:\Users\RAHUL\Downloads\icon.ico")
pygame.display.set_icon(game_icon)


# set the pygame window name
pygame.display.set_caption('Space Shooter')
clock= pygame.time.Clock
font= pygame.font.SysFont(None,45)
# create a surface object, image is drawn on it.
welcome= pygame.image.load(r"C:\Users\RAHUL\Downloads\welcome to space.jpg")
welcome= pygame.transform.scale(welcome,(screen_width,screen_height)).convert_alpha()
back = pygame.image.load(r"C:\Users\RAHUL\Downloads\back.jpg")
shooter = pygame.image.load(r"C:\Users\RAHUL\Downloads\shooter-removebg-preview.png")

def shooter_image(x,y):
    display_surface.blit(shooter, (x,y))


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display_surface.blit(screen_text, [x,y])


def plot_projectile(gameWindow, color, x,y, snake_size):
    pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
exit_game= False
game_over= False
start= True
# infinite loop
shooter_x=320
shooter_y= 450
velocity_x=0
projectile_x=shooter_x
food_x = random.randint(20, screen_width -40)
food_y = random.randint(10, 100)
food_a = random.randint(20, screen_width-40)
food_b = random.randint(10, 100)
food_c = random.randint(20, screen_width-40)
food_d = random.randint(10, 100)
food_e = random.randint(20, screen_width-40)
food_f = random.randint(10, 100)
food_g = random.randint(20, screen_width-40)
food_h = random.randint(10, 100)
food_i = random.randint(20, screen_width-40)
food_j = random.randint(10, 100)
velocity_projectile_y= -20 

v = [0, -2]

while start:
    display_surface.blit(welcome, (0, 0))
    text_screen("Press Space to play",yellow,260,290)
    text_screen("Score more than 150 to win",yellow,210,330)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                playsound(r"C:\Users\RAHUL\Downloads\Welcome to game.wav")
                start=False
    

    pygame.display.update()
    pygame.time.Clock().tick(30)



while not exit_game and game_over==False :
      
    
    display_surface.blit(back, (0, 0))
    shooter_image(shooter_x,shooter_y) 
    projectile_y=400
    
                    
    pygame.draw.rect(display_surface,white,(food_x,food_y,30,20 ))
    pygame.draw.rect(display_surface,white,(food_a,food_b,30,20 ))
    pygame.draw.rect(display_surface,white,(food_c,food_d,30,20 ))
    pygame.draw.rect(display_surface,white,(food_e,food_f,30,20 ))
    pygame.draw.rect(display_surface,white,(food_g,food_h,30,20 ))
    pygame.draw.rect(display_surface,white,(food_i,food_j,30,20 ))
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
        	pygame.quit()   
        	quit()       
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x+=2
                if shooter_x>screen_width:
                    velocity_x*=-1
            if event.key == pygame.K_LEFT:
                velocity_x-=2
            if event.key == pygame.K_q:
                score+=10
            if event.key == pygame.K_RETURN:
                ammo-=1
                if ammo==-1 and score<=150:
                    playsound(r"C:\Users\RAHUL\Downloads\Game over.wav") 
                    exit_game=True                   
                    
                elif score>150:
                    playsound(r"C:\Users\RAHUL\Downloads\Winning.wav")
                    game_over=True
                else:
                    playsound(r"C:\Users\RAHUL\Downloads\4359__noisecollector__pongblipf4.wav")
                    while projectile_y>0:
                        rect = Rect(shooter_x+60, projectile_y, 10, 40)
                        pygame.draw.rect(display_surface,red, rect,border_radius=3)
                        projectile_y= projectile_y+ velocity_projectile_y

                        if abs(rect.top - food_y)<12:
                            score +=10

                            food_x = random.randint(20, screen_width-40)
                            food_y = random.randint(10, 100)
                            food_a = random.randint(20, screen_width-40)
                            food_b = random.randint(10, 100)
                            food_c = random.randint(20, screen_width-40)
                            food_d = random.randint(10, 100)
                            food_e = random.randint(20, screen_width-40)
                            food_f = random.randint(10, 100)
                            food_g = random.randint(20, screen_width-40)
                            food_h = random.randint(10, 100)
                            food_i = random.randint(20, screen_width-40)
                            food_j = random.randint(10, 100)

                        else:
                            pass
                    
    text_screen("Score:"+ str(score),red,0,0)
    text_screen("Ammo left:"+ str(ammo),red,600,0)        
    
    shooter_x+=velocity_x
    
    
    pygame.time.Clock().tick(30)  
    pygame.display.update()

while exit_game:
    display_surface.blit(back, (0, 0))
    text_screen("!!Game Over!!  You Lost and the aliens won",yellow,90,290)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.Clock().tick(30)

while game_over:
    display_surface.blit(back, (0, 0))
    text_screen("!!Congrats Space Ranger!! You smashed the aliens",yellow,20,290)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.Clock().tick(30)
    
    

#game ended