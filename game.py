import pygame
import random
import time
import sys

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Window")
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
moveX, moveY = 0, 0
i = 0
start_time = time.time()

def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if(x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):
        return True
    elif(x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
        return True
    elif(x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        return True
    elif(x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        return True
    else:
        return False
    

class PlayerRectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25

    def render(self):
         pygame.draw.rect(window, green, (self.x, self.y, self.width, self.height))
            
class DroppingRectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25

    def render(self, collision):
        if(time.time() - start_time < 5):
            collision = False
            pygame.draw.rect(window, yellow, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))
        if(collision == True):
            sys.exit(0)           
       
            
player = PlayerRectangle(500, 500)
gameLoop = True
enemy1 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy2 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy3 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy4 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy5 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy6 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy7 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy8 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy9 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy10 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy11 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy12 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy13 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy14 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy15 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy16 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy17 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy18 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy19 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy20 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy21 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy22 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy23 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy24 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy25 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy26 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy27 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy28 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy29 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))
enemy30 = DroppingRectangle(random.randint(0, 775),random.randint(0, 575))

while gameLoop:
    if(time.time() - start_time <= 5):
        print("Position yourself!")
    else:
        print("You have survived %.2f seconds!" % (time.time() - start_time - 5))
    
    enemyX = random.randint(-15, 15)
    enemyY = random.randint(-15, 15)
    enemyX2 = random.randint(-15, 15)
    enemyY2 = random.randint(-15, 15)
    enemyX3 = random.randint(-15, 15)
    enemyY3 = random.randint(-15, 15)
    enemyX4 = random.randint(-15, 15)
    enemyY4 = random.randint(-15, 15)
    enemyX5 = random.randint(-15, 15)
    enemyY5 = random.randint(-15, 15)
    enemyX6 = random.randint(-15, 15)
    enemyY6 = random.randint(-15, 15)
    enemyX7 = random.randint(-15, 15)
    enemyY7 = random.randint(-15, 15)
    enemyX8 = random.randint(-15, 15)
    enemyY8 = random.randint(-15, 15)
    enemyX9 = random.randint(-15, 15)
    enemyY9 = random.randint(-15, 15)
    enemyX10 = random.randint(-15, 15)
    enemyY10 = random.randint(-15, 15)

    enemyX11 = random.randint(-15, 15)
    enemyY11 = random.randint(-15, 15)
    enemyX12 = random.randint(-15, 15)
    enemyY12 = random.randint(-15, 15)
    enemyX13 = random.randint(-15, 15)
    enemyY13 = random.randint(-15, 15)
    enemyX14 = random.randint(-15, 15)
    enemyY14 = random.randint(-15, 15)
    enemyX15 = random.randint(-15, 15)
    enemyY15 = random.randint(-15, 15)
    enemyX16 = random.randint(-15, 15)
    enemyY16 = random.randint(-15, 15)
    enemyX17 = random.randint(-15, 15)
    enemyY17 = random.randint(-15, 15)
    enemyX18 = random.randint(-15, 15)
    enemyY18 = random.randint(-15, 15)
    enemyX19 = random.randint(-15, 15)
    enemyY19 = random.randint(-15, 15)
    enemyX20 = random.randint(-15, 15)
    enemyY20 = random.randint(-15, 15)

    enemyX21 = random.randint(-15, 15)
    enemyY21 = random.randint(-15, 15)
    enemyX22 = random.randint(-15, 15)
    enemyY22 = random.randint(-15, 15)
    enemyX23 = random.randint(-15, 15)
    enemyY23 = random.randint(-15, 15)
    enemyX24 = random.randint(-15, 15)
    enemyY24 = random.randint(-15, 15)
    enemyX25 = random.randint(-15, 15)
    enemyY25 = random.randint(-15, 15)
    enemyX26 = random.randint(-15, 15)
    enemyY26 = random.randint(-15, 15)
    enemyX27 = random.randint(-15, 15)
    enemyY27 = random.randint(-15, 15)
    enemyX28 = random.randint(-15, 15)
    enemyY28 = random.randint(-15, 15)
    enemyX29 = random.randint(-15, 15)
    enemyY29 = random.randint(-15, 15)
    enemyX30 = random.randint(-15, 15)
    enemyY30 = random.randint(-15, 15)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                moveX =- 5
            if(event.key == pygame.K_RIGHT):
                moveX = 5
            if(event.key == pygame.K_UP):
                moveY =- 5
            if(event.key == pygame.K_DOWN):
                moveY = 5
                
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT):
                moveX = 0
            if(event.key == pygame.K_RIGHT):
                moveX = 0
            if(event.key == pygame.K_UP):
                moveY = 0
            if(event.key == pygame.K_DOWN):
                moveY = 0

                
    window.fill(white)

    if(enemy1.x + enemyX >= 0 and enemy1.x + enemyX <= 775 and enemy1.y + enemyY >= 0 and enemy1.y + enemyY <= 575):
        enemy1.x += enemyX
        enemy1.y += enemyY
        collision = detectCollisions(enemy1.x, enemy1.y, enemy1.width, enemy1.height, player.x, player.y, player.width, player.height)
        enemy1.render(collision)

    if(enemy2.x + enemyX2 >= 0 and enemy2.x + enemyX2 <= 775 and enemy2.y + enemyY2 >= 0 and enemy2.y + enemyY2 <= 575):
        enemy2.x += enemyX2
        enemy2.y += enemyY2
        collision = detectCollisions(enemy2.x, enemy2.y, enemy2.width, enemy2.height, player.x, player.y, player.width, player.height)
        enemy2.render(collision)

    if(enemy3.x + enemyX3 >= 0 and enemy3.x + enemyX3 <= 775 and enemy3.y + enemyY3 >= 0 and enemy3.y + enemyY3 <= 575):
        enemy3.x += enemyX3
        enemy3.y += enemyY3
        collision = detectCollisions(enemy3.x, enemy3.y, enemy3.width, enemy3.height, player.x, player.y, player.width, player.height)
        enemy3.render(collision)

    if(enemy4.x + enemyX4 >= 0 and enemy4.x + enemyX4 <= 775 and enemy4.y + enemyY4 >= 0 and enemy4.y + enemyY4 <= 575):
        enemy4.x += enemyX4
        enemy4.y += enemyY4
        collision = detectCollisions(enemy4.x, enemy4.y, enemy4.width, enemy4.height, player.x, player.y, player.width, player.height)
        enemy4.render(collision)

    if(enemy5.x + enemyX5 >= 0 and enemy5.x + enemyX5 <= 775 and enemy5.y + enemyY5 >= 0 and enemy5.y + enemyY5 <= 575):
        enemy5.x += enemyX5
        enemy5.y += enemyY5
        collision = detectCollisions(enemy5.x, enemy5.y, enemy5.width, enemy5.height, player.x, player.y, player.width, player.height)
        enemy5.render(collision)

    if(enemy6.x + enemyX6 >= 0 and enemy6.x + enemyX6 <= 775 and enemy6.y + enemyY6 >= 0 and enemy6.y + enemyY6 <= 575):
        enemy6.x += enemyX6
        enemy6.y += enemyY6
        collision = detectCollisions(enemy6.x, enemy6.y, enemy6.width, enemy6.height, player.x, player.y, player.width, player.height)
        enemy6.render(collision)

    if(enemy7.x + enemyX7 >= 0 and enemy7.x + enemyX7 <= 775 and enemy7.y + enemyY7 >= 0 and enemy7.y + enemyY7 <= 575):
        enemy7.x += enemyX7
        enemy7.y += enemyY7
        collision = detectCollisions(enemy7.x, enemy7.y, enemy7.width, enemy7.height, player.x, player.y, player.width, player.height)
        enemy7.render(collision)

    if(enemy8.x + enemyX8 >= 0 and enemy8.x + enemyX8 <= 775 and enemy8.y + enemyY8 >= 0 and enemy8.y + enemyY8 <= 575):
        enemy8.x += enemyX8
        enemy8.y += enemyY8
        collision = detectCollisions(enemy8.x, enemy8.y, enemy8.width, enemy8.height, player.x, player.y, player.width, player.height)
        enemy8.render(collision)

    if(enemy9.x + enemyX9 >= 0 and enemy9.x + enemyX9 <= 775 and enemy9.y + enemyY9 >= 0 and enemy9.y + enemyY9 <= 575):
        enemy9.x += enemyX9
        enemy9.y += enemyY9
        collision = detectCollisions(enemy9.x, enemy9.y, enemy9.width, enemy9.height, player.x, player.y, player.width, player.height)
        enemy9.render(collision)

    if(enemy10.x + enemyX10 >= 0 and enemy10.x + enemyX10 <= 775 and enemy10.y + enemyY10 >= 0 and enemy10.y + enemyY10 <= 575):
        enemy10.x += enemyX10
        enemy10.y += enemyY10
        collision = detectCollisions(enemy10.x, enemy10.y, enemy10.width, enemy10.height, player.x, player.y, player.width, player.height)
        enemy10.render(collision)


    if(enemy11.x + enemyX11 >= 0 and enemy11.x + enemyX11 <= 775 and enemy11.y + enemyY11 >= 0 and enemy11.y + enemyY11 <= 575):
        enemy11.x += enemyX11
        enemy11.y += enemyY11
        collision = detectCollisions(enemy11.x, enemy11.y, enemy11.width, enemy11.height, player.x, player.y, player.width, player.height)
        enemy11.render(collision)

    if(enemy12.x + enemyX12 >= 0 and enemy12.x + enemyX12 <= 775 and enemy12.y + enemyY12 >= 0 and enemy12.y + enemyY12 <= 575):
        enemy2.x += enemyX12
        enemy2.y += enemyY12
        collision = detectCollisions(enemy12.x, enemy12.y, enemy12.width, enemy12.height, player.x, player.y, player.width, player.height)
        enemy2.render(collision)

    if(enemy13.x + enemyX13 >= 0 and enemy13.x + enemyX13 <= 775 and enemy13.y + enemyY13 >= 0 and enemy13.y + enemyY13 <= 575):
        enemy13.x += enemyX13
        enemy13.y += enemyY13
        collision = detectCollisions(enemy13.x, enemy13.y, enemy13.width, enemy13.height, player.x, player.y, player.width, player.height)
        enemy13.render(collision)

    if(enemy14.x + enemyX14 >= 0 and enemy14.x + enemyX14 <= 775 and enemy14.y + enemyY14 >= 0 and enemy14.y + enemyY14 <= 575):
        enemy14.x += enemyX14
        enemy14.y += enemyY14
        collision = detectCollisions(enemy14.x, enemy14.y, enemy14.width, enemy14.height, player.x, player.y, player.width, player.height)
        enemy14.render(collision)

    if(enemy15.x + enemyX15 >= 0 and enemy15.x + enemyX15 <= 775 and enemy15.y + enemyY15 >= 0 and enemy15.y + enemyY15 <= 575):
        enemy15.x += enemyX15
        enemy15.y += enemyY15
        collision = detectCollisions(enemy15.x, enemy15.y, enemy15.width, enemy15.height, player.x, player.y, player.width, player.height)
        enemy15.render(collision)

    if(enemy16.x + enemyX16 >= 0 and enemy16.x + enemyX16 <= 775 and enemy16.y + enemyY16 >= 0 and enemy16.y + enemyY16 <= 575):
        enemy16.x += enemyX16
        enemy16.y += enemyY16
        collision = detectCollisions(enemy16.x, enemy16.y, enemy16.width, enemy16.height, player.x, player.y, player.width, player.height)
        enemy16.render(collision)

    if(enemy17.x + enemyX17 >= 0 and enemy17.x + enemyX17 <= 775 and enemy17.y + enemyY17 >= 0 and enemy17.y + enemyY17 <= 575):
        enemy17.x += enemyX17
        enemy17.y += enemyY17
        collision = detectCollisions(enemy17.x, enemy17.y, enemy17.width, enemy17.height, player.x, player.y, player.width, player.height)
        enemy17.render(collision)

    if(enemy18.x + enemyX18 >= 0 and enemy18.x + enemyX18 <= 775 and enemy18.y + enemyY18 >= 0 and enemy18.y + enemyY18 <= 575):
        enemy18.x += enemyX18
        enemy18.y += enemyY18
        collision = detectCollisions(enemy18.x, enemy18.y, enemy18.width, enemy18.height, player.x, player.y, player.width, player.height)
        enemy18.render(collision)

    if(enemy19.x + enemyX19 >= 0 and enemy19.x + enemyX19 <= 775 and enemy19.y + enemyY19 >= 0 and enemy19.y + enemyY19 <= 575):
        enemy19.x += enemyX19
        enemy19.y += enemyY19
        collision = detectCollisions(enemy19.x, enemy19.y, enemy19.width, enemy19.height, player.x, player.y, player.width, player.height)
        enemy19.render(collision)

    if(enemy20.x + enemyX20 >= 0 and enemy20.x + enemyX20 <= 775 and enemy20.y + enemyY20 >= 0 and enemy20.y + enemyY20 <= 575):
        enemy20.x += enemyX20
        enemy20.y += enemyY20
        collision = detectCollisions(enemy20.x, enemy20.y, enemy20.width, enemy20.height, player.x, player.y, player.width, player.height)
        enemy20.render(collision)


    if(enemy21.x + enemyX21 >= 0 and enemy21.x + enemyX21 <= 775 and enemy21.y + enemyY21 >= 0 and enemy21.y + enemyY21 <= 575):
        enemy21.x += enemyX21
        enemy21.y += enemyY21
        collision = detectCollisions(enemy21.x, enemy21.y, enemy21.width, enemy21.height, player.x, player.y, player.width, player.height)
        enemy21.render(collision)

    if(enemy22.x + enemyX22 >= 0 and enemy22.x + enemyX22 <= 775 and enemy22.y + enemyY22 >= 0 and enemy22.y + enemyY22 <= 575):
        enemy22.x += enemyX22
        enemy22.y += enemyY22
        collision = detectCollisions(enemy22.x, enemy22.y, enemy22.width, enemy22.height, player.x, player.y, player.width, player.height)
        enemy22.render(collision)

    if(enemy23.x + enemyX23 >= 0 and enemy23.x + enemyX23 <= 775 and enemy23.y + enemyY23 >= 0 and enemy23.y + enemyY23 <= 575):
        enemy23.x += enemyX23
        enemy23.y += enemyY23
        collision = detectCollisions(enemy23.x, enemy23.y, enemy23.width, enemy23.height, player.x, player.y, player.width, player.height)
        enemy23.render(collision)

    if(enemy24.x + enemyX24 >= 0 and enemy24.x + enemyX24 <= 775 and enemy24.y + enemyY24 >= 0 and enemy24.y + enemyY24 <= 575):
        enemy24.x += enemyX24
        enemy24.y += enemyY24
        collision = detectCollisions(enemy24.x, enemy24.y, enemy24.width, enemy24.height, player.x, player.y, player.width, player.height)
        enemy24.render(collision)

    if(enemy25.x + enemyX25 >= 0 and enemy25.x + enemyX25 <= 775 and enemy25.y + enemyY25 >= 0 and enemy25.y + enemyY25 <= 575):
        enemy25.x += enemyX25
        enemy25.y += enemyY25
        collision = detectCollisions(enemy25.x, enemy25.y, enemy25.width, enemy25.height, player.x, player.y, player.width, player.height)
        enemy25.render(collision)

    if(enemy26.x + enemyX26 >= 0 and enemy26.x + enemyX26 <= 775 and enemy26.y + enemyY26 >= 0 and enemy26.y + enemyY26 <= 575):
        enemy26.x += enemyX26
        enemy26.y += enemyY26
        collision = detectCollisions(enemy26.x, enemy26.y, enemy26.width, enemy26.height, player.x, player.y, player.width, player.height)
        enemy26.render(collision)

    if(enemy27.x + enemyX27 >= 0 and enemy27.x + enemyX27 <= 775 and enemy27.y + enemyY27 >= 0 and enemy27.y + enemyY27 <= 575):
        enemy27.x += enemyX27
        enemy27.y += enemyY27
        collision = detectCollisions(enemy27.x, enemy27.y, enemy27.width, enemy27.height, player.x, player.y, player.width, player.height)
        enemy27.render(collision)
  
    if(enemy28.x + enemyX28 >= 0 and enemy28.x + enemyX28 <= 775 and enemy28.y + enemyY28 >= 0 and enemy28.y + enemyY28 <= 575):
        enemy28.x += enemyX28
        enemy28.y += enemyY28
        collision = detectCollisions(enemy28.x, enemy28.y, enemy28.width, enemy28.height, player.x, player.y, player.width, player.height)
        enemy28.render(collision)

    if(enemy29.x + enemyX29 >= 0 and enemy29.x + enemyX29 <= 775 and enemy29.y + enemyY29 >= 0 and enemy29.y + enemyY29 <= 575):
        enemy29.x += enemyX29
        enemy29.y += enemyY29
        collision = detectCollisions(enemy29.x, enemy29.y, enemy29.width, enemy29.height, player.x, player.y, player.width, player.height)
        enemy29.render(collision)

    if(enemy30.x + enemyX30 >= 0 and enemy30.x + enemyX30 <= 775 and enemy30.y + enemyY30 >= 0 and enemy30.y + enemyY30 <= 575):
        enemy30.x += enemyX30
        enemy30.y += enemyY30
        collision = detectCollisions(enemy30.x, enemy30.y, enemy30.width, enemy30.height, player.x, player.y, player.width, player.height)
        enemy30.render(collision)


    if(player.x + moveX >= 0 and player.x + moveX <= 750 and player.y + moveY >= 0 and player.y + moveY <= 550):
        player.x += moveX
        player.y += moveY
        player.render()
    
    clock.tick(60)
    pygame.display.flip()
