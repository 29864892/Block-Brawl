import gamebox
import pygame
import random
camera = gamebox.Camera(800,600)
camera.clear("white")
maincharacter1 = gamebox.from_color(650,500, "blue", 13,20)
maincharacter2 = gamebox.from_color(300,500, "red", 13,20)
y = random.randint(100,700)
plane = gamebox.from_image(850, 100, "https://i.imgur.com/R9An3y1.png")
background = gamebox.from_image(400,300,"https://i.imgur.com/7WG3rQk.png")
package = gamebox.from_image(850, 600, "https://i.imgur.com/h5fyp8A.png")
BigArray = []
background2 = gamebox.from_image(400, 300, "https://i.imgur.com/zAy47Sk.png")
background3 = gamebox.from_image(400, 300, "https://i.imgur.com/mwkwTgG.png")
background4 = gamebox.from_image(400, 300, "https://i.imgur.com/v5R51YE.png")
background5 = gamebox.from_image(400, 300, "https://i.imgur.com/8cugH8E.png")
background6 = gamebox.from_image(400, 300, "https://i.imgur.com/UEOZCRm.png")
background7 = gamebox.from_image(400, 300, "https://i.imgur.com/9lLac9O.png")
background8 = gamebox.from_image(400, 300, "https://i.imgur.com/f0H5amE.png")
nuke1 = gamebox.from_image(900, -25, "https://i.imgur.com/h6KxUA2.png")
nuke2 = gamebox.from_image(900, -25, "https://i.imgur.com/h6KxUA2.png")
gamestart = []
gravity1, gravity2, timer, timer1, timer2, x, speed1, speed2, count1, count2, count3 = 0,0,0,0,0,0,0,0,0,0,0
plane.speedx = -5
package.speedy = 5
goods = False
size1 = 1
size2 = 1
array = []
wall = gamebox.from_color(400,550, "blue", 800, 100)
wall1 = gamebox.from_color(850,300, "blue", 100, 600)
wall2 = gamebox.from_color(-50,300, "blue", 100, 600)
slidenumber = 0
beforeGame = True
gameOn = True
player1win = False
player2win = False
alpha = 0
slideshow = []
slideshow.append(background2)
slideshow.append(background3)
slideshow.append(background4)
slideshow.append(background5)
slideshow.append(background6)
slideshow.append(background7)
slideshow.append(background8)
speedman1 = 4
speedman2 = 4
invincibleman1 = False
invincibleman2 = False
def tick(keys):
    global x, timer, timer1, timer2, gravity1, gravity2, y, plane, goods, package, array, size1, size2, maincharacter1, maincharacter2, speed1, speed2, gameOn, player1win, player2win, slidenumber, beforeGame, alpha, speedman1, speedman2, invincibleman1, invincibleman2, count1, count2, nuke1, nuke2, count3
    if nuke1.touches(maincharacter2):
        gameOn = False
        player1win = True
    if nuke2.touches(maincharacter1):
        gameOn = False
        player2win = True
    if invincibleman1:
        maincharacter1.color = "white"
        count1 += 1
    if invincibleman2:
        maincharacter2.color = "white"
        count2 += 1
    if not invincibleman1:
        maincharacter1.color = "blue"
    if not invincibleman2:
        maincharacter2.color = "red"
    if count1 / 240 > 1:
        count1 = 0
        invincibleman1 = False
    if count2 / 240 > 1:
        count2 = 0
        invincibleman2 = False
    if maincharacter1.y >= 500:
        gravity1 = 0
    elif maincharacter1.y < 500:
        gravity1 -= .1
    if maincharacter2.y >= 500:
        gravity2 = 0
    elif maincharacter2.y < 500:
        gravity2 -= .1
    if maincharacter1.bottom_touches(maincharacter2) and not invincibleman2:
        gameOn = False
        player1win = True
    if maincharacter2.bottom_touches(maincharacter1) and not invincibleman1:
        gameOn = False
        player2win = True
    if beforeGame:
        camera.draw(slideshow[slidenumber])
        if pygame.K_RIGHT in keys:
            slidenumber += 1
            keys.clear()
            if slidenumber == 4:
                camera.clear("white")
        camera.display()
        if slidenumber == 6:
            camera.draw(slideshow[slidenumber])
            camera.display()
            beforeGame = False
    if not gameOn and not beforeGame:
        camera.clear('black')
        if player1win:
            background1 = gamebox.from_image(400,300,"https://i.imgur.com/ucAWNBG.png")
            replay = gamebox.from_text(550, 550, "Press Tab To Replay", 60, "black")
            camera.draw(background1)
            camera.draw(replay)
            camera.display()
            if pygame.K_TAB in keys:
                keys.clear()
                camera.clear("white")
                gameOn = True
                player1win = False
                beforeGame = False
                maincharacter1 = gamebox.from_color(650, 500, "blue", 13, 20)
                maincharacter2 = gamebox.from_color(300, 500, "red", 13, 20)
                speedman1 = 4
                speedman2 = 4
                nuke1.x = 900
                nuke2.x = 900
        if player2win:
            count3 += 1
            background1 = gamebox.from_image(400,300,"https://i.imgur.com/NfljNfn.png")
            replay = gamebox.from_text(550, 550, "Press Tab To Replay", 60, "black")
            camera.draw(background1)
            camera.draw(replay)
            camera.display()
            if count3 / 360 > 1:
                count3 = 0
                camera.clear("black")
            if pygame.K_TAB in keys:
                keys.clear()
                camera.clear("white")
                gameOn = True
                player2win = False
                beforeGame = False
                maincharacter1 = gamebox.from_color(650, 500, "blue", 13, 20)
                maincharacter2 = gamebox.from_color(300, 500, "red", 13, 20)
                speedman1 = 4
                speedman2 = 4
                nuke1.x = 900
                nuke2.x = 900
    if (pygame.K_RETURN in keys or pygame.K_RETURN in gamestart) and gameOn and not beforeGame:
        if pygame.K_RETURN not in gamestart:
            gamestart.append(pygame.K_RETURN)
        try:
            if maincharacter1.touches(package):
                array.remove(package)
                if alpha == 0:
                    size1 += 1
                    maincharacter1 = gamebox.from_color(maincharacter1.x, maincharacter1.y, "blue", 13 * size1, 20)
                if alpha == 1:
                    if size1 <= 1:
                        size1 = size1/2
                    if size1 > 1:
                        size1 -= 1
                    maincharacter1 = gamebox.from_color(maincharacter1.x, maincharacter1.y, "blue", 13 * size1, 20)
                if alpha == 2:
                    speedman1 = speedman1 * 2
                if alpha == 3:
                    invincibleman1 = True
                if alpha == 4:
                    nuke1 = gamebox.from_image(maincharacter2.x, -25, "https://i.imgur.com/h6KxUA2.png")
                    nuke1.speedy = 14

            if maincharacter2.touches(package):
                array.remove(package)
                if alpha == 0:
                    size2 += 1
                    maincharacter2 = gamebox.from_color(maincharacter2.x, maincharacter2.y, "red", 13 * size2, 20)
                if alpha == 1:
                    if size2 <= 1:
                        size2 = size2/2
                    if size2 > 1:
                        size2 -= 1
                    maincharacter2 = gamebox.from_color(maincharacter2.x, maincharacter2.y, "red", 13 * size2, 20)
                if alpha == 2:
                    speedman2 = speedman2 * 2
                if alpha == 3:
                    invincibleman2 = True
                if alpha == 4:
                    nuke2 = gamebox.from_image(maincharacter1.x, -25, "https://i.imgur.com/h6KxUA2.png")
                    nuke2.speedy = 14
        except:
            None
        timer += 1
        timer1 += 1
        timer2 += 1
        maincharacter1.speedy = speed1
        maincharacter2.speedy = speed2
        keysPressed = pygame.key.get_pressed()
        if timer / 60 > 1:
            if keysPressed[273] == 1:
                timer = 0
                maincharacter1.speedy = -20
        if timer1 / 60 > 1:
            if keysPressed[119] == 1:
                timer1 = 0
                maincharacter2.speedy = -20
        if timer2 / 300 > 1:
            plane = gamebox.from_image(850, 100, "https://i.imgur.com/R9An3y1.png")
            plane.speedx = -5
            camera.draw(plane)
            goods = True
            x = random.randint(150,650)
            timer2 = 0
        if pygame.K_LEFT in keys:
            maincharacter1.speedx = -speedman1
        elif pygame.K_RIGHT in keys:
            maincharacter1.speedx = speedman1
        if pygame.K_a in keys:
            maincharacter2.speedx = -speedman2
        elif pygame.K_d in keys:
            maincharacter2.speedx = speedman2
        camera.draw(wall)
        camera.draw(background)
        camera.draw(wall1)
        camera.draw(wall2)
        camera.draw(nuke1)
        camera.draw(nuke2)
        nuke1.move_speed()
        nuke2.move_speed()
        maincharacter2.speedy -= gravity2
        maincharacter1.speedy -= gravity1
        if abs(maincharacter1.speedy) > 100:
            maincharacter1.speedy = 0
        if abs(maincharacter2.speedy) > 100:
            maincharacter2.speedy = 0
        wall.move_to_stop_overlapping(maincharacter1)
        wall.move_to_stop_overlapping(maincharacter2)
        maincharacter1.move_to_stop_overlapping(maincharacter2)
        maincharacter1.move_speed()
        maincharacter2.move_speed()
        maincharacter1.move_to_stop_overlapping(maincharacter2)
        maincharacter2.move_to_stop_overlapping(maincharacter1)
        maincharacter1.move_to_stop_overlapping(wall)
        maincharacter2.move_to_stop_overlapping(wall)
        maincharacter1.move_to_stop_overlapping(wall1)
        maincharacter2.move_to_stop_overlapping(wall1)
        maincharacter1.move_to_stop_overlapping(wall2)
        maincharacter2.move_to_stop_overlapping(wall2)
        plane.move_speed()
        maincharacter1.speedx, maincharacter2.speedx = 0,0
        camera.draw(maincharacter1)
        camera.draw(maincharacter2)
        speed1 = maincharacter1.speedy
        speed2 = maincharacter2.speedy
        if goods:
            if x - 2.6 < plane.x < x + 2.6:
                alpha = random.randint(0,4)
                if alpha == 0:
                    package = gamebox.from_image(plane.x, plane.y, "https://i.imgur.com/h5fyp8A.png")
                if alpha == 1:
                    package = gamebox.from_image(plane.x, plane.y, "https://i.imgur.com/NUcA6PV.png")
                if alpha == 2:
                    package = gamebox.from_image(plane.x, plane.y, "https://i.imgur.com/PD31S8N.png")
                if alpha == 3:
                    package = gamebox.from_image(plane.x, plane.y, "https://i.imgur.com/944DnLy.png")
                if alpha == 4:
                    package = gamebox.from_image(plane.x, plane.y, "https://i.imgur.com/NGPKzAo.png")

                array.append(package)
                package.speedy = 5
                goods = False
        package.move_speed()
        for package in array:
            camera.draw(package)
        camera.draw(plane)
        camera.display()
        camera.clear("black")


gamebox.timer_loop   (60,tick)
