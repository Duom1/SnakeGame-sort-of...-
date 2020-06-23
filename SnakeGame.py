# py game library
import pygame
pygame.init()

# display
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Game")
pygame.mouse.set_visible(0)

# variables
width = 10 # cube size
height = 10 # cube size
winW = 1920 # boundaries
winH = 1080 # boundaries
x = 1920 / 2 - (width / 2) # sets the starting osition on the X axes
y = 1080 / 2 - (height / 2) # sets the starting osition on the Y axes
vel = 2 # Velocity of the cube

# main loop
run = True
while run:
    pygame.time.delay(1)
    
    keyPressedX = False
    keyPressedY = False

    # QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # wasd control
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > 0 and keyPressedX == False:  
        x -= vel
        keyPressedX = True

    if keys[pygame.K_d] and x < winW - width and keyPressedX == False:  
        x += vel
        keyPressedX = True

    if keys[pygame.K_w] and y > 0 and keyPressedY == False: 
        y -= vel
        keyPressedY = True

    if keys[pygame.K_s] and y < winH - height and keyPressedY == False:
        y += vel
        keyPressedY = True
    
    # arrow control
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0 and keyPressedX == False:  
        x -= vel
        keyPressedX = True

    if keys[pygame.K_RIGHT] and x < 1920 - width and keyPressedX == False:  
        x += vel
        keyPressedX = True

    if keys[pygame.K_UP] and y > 0 and keyPressedY == False: 
        y -= vel
        keyPressedY = True

    if keys[pygame.K_DOWN] and y < 1080 - height and keyPressedY == False:
        y += vel
        keyPressedY = True
    
    # clear
    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        win.fill((0,0,0))

    # drawiings
    #win.fill((0,0,0)) #optional
    pygame.draw.rect(win, (255,0,255), (x, y, width, height))   
    pygame.display.update() 

# QUIT 
pygame.quit()
