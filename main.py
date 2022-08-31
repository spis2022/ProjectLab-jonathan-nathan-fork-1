import pygame 

import os

import random

screenLength = 512

screenWidth = 384

pipe1 = pygame.Rect(512, -94, 109, 234)

pipe2 = pygame.Rect(512, 275, 109, 234)

rect_player = pygame.Rect(30, 180, 39, 24)
rect_playerB = pygame.Rect(30, 100, 39, 24)
rect_playerR = pygame.Rect(30, 200, 39, 24)

dimField = (screenLength, screenWidth)

screen = pygame.display.set_mode(dimField)

player = pygame.image.load(os.path.join("assets", "fish.jpg")).convert()
player.set_colorkey((255,255,255))
player = pygame.transform.scale(player, (39, 24))

playerB = pygame.image.load(os.path.join("assets", "fish.jpg")).convert()
playerB.set_colorkey((255,255,255))
playerB = pygame.transform.scale(playerB, (39, 24))

playerR = pygame.image.load(os.path.join("assets", "redFish.jpg")).convert()
playerR.set_colorkey((255,255,255))
playerR = pygame.transform.scale(playerR, (39, 24))

# playerUp = pygame.image.load(os.path.join("assets", "blueFishUp.jpg")).convert()
# playerUp.set_colorkey((255,255,255))
# playerUp = pygame.transform.scale(playerUp, (39, 24))

# playerUpB = pygame.image.load(os.path.join("assets", "blueFishUp.jpg")).convert()
# playerUpB.set_colorkey((255,255,255))
# playerUpB = pygame.transform.scale(playerUpB, (39, 24))

# playerR = pygame.image.load(os.path.join("assets", "redFish.jpg")).convert()
# playerR.set_colorkey((255,255,255))
# playerR = pygame.transform.scale(playerR, (39, 24))

# playerDown = pygame.image.load(os.path.join("assets", "blueFishDown.jpg")).convert()
# playerDown.set_colorkey((255,255,255))
# playerDown = pygame.transform.scale(playerDown, (39, 24))

# playerDownB = pygame.image.load(os.path.join("assets", "blueFishDown.jpg")).convert()
# playerDownB.set_colorkey((255,255,255))
# playerB = pygame.transform.scale(playerDownB, (39, 24))

# playerR = pygame.image.load(os.path.join("assets", "redFish.jpg")).convert()
# playerR.set_colorkey((255,255,255))
# playerR = pygame.transform.scale(playerR, (39, 24))



background = pygame.image.load(os.path.join("assets", "background.png"))

gameTitle = pygame.image.load(os.path.join("assets", "splashyFish.png")).convert()
gameTitle.set_colorkey((0,216,255))
gameTitle = pygame.transform.scale(gameTitle, (410, 200))

pressEnter = pygame.image.load(os.path.join("assets", "enter.png"))
pressEnter = pygame.transform.scale(pressEnter, (253, 80))

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

gravityB = True

jumpStateB = False

gravityR = True

jumpStateR = False

jumpFrame = 0

jumpFrameB = 0

jumpFrameR = 0

score = 0

pipeSpeed = 3

FPS = 60

pipeMoveUp = True

startState = False
gameStarted1 = False
gameStarted2 = False
while(running):
    
    clock.tick(FPS)
    screen.blit(background, (0,0))
    screen.blit(gameTitle, (50, 10))
    screen.blit(pressEnter, (130, 210))
    index = rect_player.collidelist([pipe1, pipe2])
    indexB = rect_playerB.collidelist([pipe1, pipe2])
    indexR = rect_playerR.collidelist([pipe1, pipe2])
    if(startState and (not gameStarted1 or not gameStarted2)):
        screen.blit(background, (0,0))
        screen.blit(gameMode,(70, 100))
        startText = font.render("press '1' for single player and '2' for two players", True, (0,0,0))
        screen.blit(startText, (25,180))

    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_1:
                gameStarted1 = True
            if event.key == pygame.K_2:
                gameStarted2 = True
            if event.key == pygame.K_RETURN:
                startState = True
            if event.key == pygame.K_SPACE:
                jumpState = True
                gravity = False
                jumpFrame = 0
            if event.key == pygame.K_b:
                jumpStateB = True
                gravityB = False
                jumpFrameB = 0
            if event.key == pygame.K_r:
                jumpStateR = True
                gravityR = False
                jumpFrameR = 0

    if(startState and (gameStarted1 or gameStarted2)):
        screen.blit(background, (0,0))
        if(gameStarted1): 
            screen.blit(player, rect_player)
        if(gameStarted2): 
            screen.blit(playerB, rect_playerB)
            screen.blit(playerR, rect_playerR)
        screen.blit(pipeUp, pipe1)
        # pygame.draw.rect(screen, (0, 200, 100), pipe1)
        screen.blit(pipeDown, pipe2)
        # pygame.draw.rect(screen, (0, 200, 100), pipe2)

        font = pygame.font.SysFont("Comicsans", 40)
        text = font.render("SCORE: " + str(score) , True, (0,0,0))
        screen.blit(text, (10,10))


        if jumpState == True:
            # screen.blit(playerUp, rect_player)
            rect_player.move_ip(0, -10)
            jumpFrame += 1
        
        if jumpFrame >= 8:
            jumpState = False
            gravity = True

        if jumpStateB == True:
            rect_playerB.move_ip(0, -10)
            jumpFrameB += 1
        

        if jumpFrameB >= 8:
            jumpStateB = False
            gravityB = True

        if jumpStateR == True:
            rect_playerR.move_ip(0, -10)
            jumpFrameR += 1
        

        if jumpFrameR >= 8:
            jumpStateR = False
            gravityR = True

        if(startState):
            if gravity == True:
                # screen.blit(playerDown, rect_player)
                rect_player.move_ip(0, gravitySpeed)
            if gravityB == True:
                rect_playerB.move_ip(0, gravitySpeed)
            if gravityR == True:
                rect_playerR.move_ip(0, gravitySpeed)
            
                

            pipe1.move_ip(-1 * pipeSpeed, 0)

            pipe2.move_ip(-1 * pipeSpeed, 0)

            if pipe1.bottom <= 20:
                pipeMoveUp = False
            if pipe2.top >= 364:
                pipeMoveUp = True

            if pipeMoveUp:
                pipe1.move_ip(0, -2)
                pipe2.move_ip(0, -2)
            else:
                pipe1.move_ip(0, 2)
                pipe2.move_ip(0, 2)
            
        if pipe1.left <= -109:
            score += 1

            gap = random.randrange(0, 234)
            pipe1 = pygame.Rect(512, -234 + gap, 109, 234)
            pipe2 = pygame.Rect(512, gap + 150, 109, 384 - (gap + 150))
            print(gap)


    if score >= 10:
        pipeSpeed = 6

    if score >= 20:
        pipeSpeed = 9

    if score >= 30:
        pipeSpeed = 12

    if score >= 40:
        pipeSpeed = 15
    
    if (index >= 0 or rect_player.top >= 384 or rect_player.bottom <= 0) and gameStarted1:
        running = False
        screen.blit(dead, (120, 100))

    if (indexB >= 0 or rect_playerB.top >= 384 or rect_playerB.bottom <= 0) and gameStarted2:
        running = False
        screen.blit(dead, (120, 100))
        winningText = font.render("Red Fish Wins", True, (0,0,0))
        screen.blit(winningText, (150, 250))

    if (indexR >= 0 or rect_playerR.top >= 384 or rect_playerR.bottom <= 0) and gameStarted2:
        running = False
        screen.blit(dead, (120, 100))
        winningText = font.render("Blue Fish Wins", True, (0,0,0))
        screen.blit(winningText, (150, 250))
        

       
    pygame.display.update()