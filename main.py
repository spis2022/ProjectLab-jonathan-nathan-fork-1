import pygame 

import os

import random

screenLength = 512

screenWidth = 384

pipe1 = pygame.Rect(512, -94, 95, 204)

pipe2 = pygame.Rect(512, 260, 95, 204)

rect_player = pygame.Rect(30,180, 39, 24)

dimField = (screenLength, screenWidth)

screen = pygame.display.set_mode(dimField)

player = pygame.image.load(os.path.join("assets", "fish.jpg")).convert()
player.set_colorkey((255,255,255))
player = pygame.transform.scale(player, (39, 24))


background = pygame.image.load(os.path.join("assets", "background.png"))

dead = pygame.image.load(os.path.join("assets", "dead.png"))
dead = pygame.transform.scale(dead, (257, 150))

pipeDown = pygame.image.load(os.path.join("assets", "pipeDown.png"))
pipeDown = pygame.transform.scale(pipeDown, (109, 234))

pipeUp = pygame.image.load(os.path.join("assets", "pipeUp.png"))
pipeUp = pygame.transform.scale(pipeUp, (109, 234))

gameMode = pygame.image.load(os.path.join("assets", "gameMode.png"))
gameMode = pygame.transform.scale(gameMode, (370, 70))






clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("Comicsans", 30)

#Game Loop
running = True

pipeSpeed = 20

gravitySpeed = 3 

gravity = True

jumpState = False

jumpFrame = 0

score = 0

pipeSpeed = 3

FPS = 60

startState = False
while(running):
    
    clock.tick(FPS)
    screen.blit(background, (0,0))
    index = rect_player.collidelist([pipe1, pipe2])
    if(not startState):
        screen.blit(gameMode,(70, 100))
        startText = font.render("press '1' for single player and '2' for two players", True, (0,0,0))
        screen.blit(startText, (25,180))

    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                startState = True
                jumpState = True
                gravity = False
                jumpFrame = 0

    if(startState):
        screen.blit(background, (0,0))
        screen.blit(player, rect_player)
        screen.blit(pipeUp, pipe1)
        # pygame.draw.rect(screen, (0, 200, 100), pipe1)
        screen.blit(pipeDown, pipe2)
        # pygame.draw.rect(screen, (0, 200, 100), pipe2)

        text = font.render("SCORE: " + str(score) , True, (0,0,0))
        screen.blit(text, (10,10))


    if jumpState == True:
        rect_player.move_ip(0, -10)
        jumpFrame += 1
        

    if jumpFrame >= 8:
        jumpState = False
        gravity = True

    if(startState):
        if gravity == True:
            rect_player.move_ip(0, gravitySpeed)

        pipe1.move_ip(-1 * pipeSpeed, 0)

        pipe2.move_ip(-1 * pipeSpeed, 0)

    if pipe1.left <= -75:
        score += 1

        gap = random.randrange(0, 234)
        pipe1 = pygame.Rect(512, -234 + gap, 95, 234)
        pipe2 = pygame.Rect(512, gap + 150, 95, 384 - (gap + 150))
        print(gap)


    if score >= 10:
        pipeSpeed = 6

    if score >= 20:
        pipeSpeed = 9

    if score >= 30:
        pipeSpeed = 12

    if score >= 40:
        pipeSpeed = 15
    
    if index >= 0 or rect_player.top >= 384:
        running = False
        screen.blit(dead, (120, 100))
        
        

       
    pygame.display.update()