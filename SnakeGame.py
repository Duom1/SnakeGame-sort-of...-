# py game library
import pygame
pygame.init()

# display
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Game")
pygame.mouse.set_visible(0)

# variables
width = 10
height = 10
winW = 1920
winH = 1080
x = 1920 / 2 - (width / 2) #asettaa kuution keskelle X:llä
y = 1080 / 2 - (height / 2) # asettaa kuution keskelle Y:llä
vel = 2

# main loop
run = True
while run:
    pygame.time.delay(1)

    # QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # wasd control
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > 0:  
        x -= vel

    if keys[pygame.K_d] and x < winW - width:  
        x += vel

    if keys[pygame.K_w] and y > 0: 
        y -= vel

    if keys[pygame.K_s] and y < winH - height:
        y += vel
    
    # Nuoli control
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:  
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1920 - width:  
        x += vel

    if keys[pygame.K_UP] and y > 0: 
        y -= vel

    if keys[pygame.K_DOWN] and y < 1080 - height:
        y += vel

    # PIIRROKSET
    #--win.fill((0,0,0)) #optional
    pygame.draw.rect(win, (255,0,255), (x, y, width, height))   
    pygame.display.update() 

# QUIT V2
pygame.quit()