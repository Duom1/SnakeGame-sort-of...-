# SnakeGame *(sort of...)*
This is a game made with python and pygame. If you want to look at the source code you can find it at the bottom of this README file. Or you can download the **SnakeGame.py** but must have python 3.8.3 and pygame library downloaded.

## How to download 
  1. Click **SnakeGame.exe** not SnakeGame.py
  1. Click download (if you can find it)
  1. Drag and drop the file onto your desktop
  1. Double click the file and enjoy

## Patch notes
* v: 1.0
  * **--Other information:**
  * Simple drawing mecanism
  * Controls WASD and Arrow keys
  * Black background and purple line
  * Fullscreen 1920 x 1080
  * Cursor is now invisible
  * **--Variables:**
  * Spawning position midle
  * Velocity is 2 and time.delay is 1
  * Cube size is 10 x 10
  * No moving borders needed

## How to play
* To move use **WASD** or the arrowkeys.
* You can exit the game by pressing **Windows key**.
* ~~Press **C** to clear the screen.~~ (not done yet)

## Gameplay 
![Gameplay1](https://cdn.discordapp.com/attachments/709674549373042692/725004629531820132/Game_23.6.2020_18.08.55.png)
![Gameplay2](https://media.discordapp.net/attachments/709674549373042692/725005915752759316/Game_23.6.2020_17.23.38.png?width=1204&height=677)

## Source Code
``` python
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
    
    # arrow control
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:  
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1920 - width:  
        x += vel

    if keys[pygame.K_UP] and y > 0: 
        y -= vel

    if keys[pygame.K_DOWN] and y < 1080 - height:
        y += vel
    
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
```
