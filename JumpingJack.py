import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
font = pygame.font.SysFont("comicsans", 30, True)

walkRight = [pygame.image.load('/home/sourav/Desktop/firstgame/R1.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R2.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R3.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R4.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R5.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R6.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R7.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R8.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R9.png')]
walkLeft = [pygame.image.load('/home/sourav/Desktop/firstgame/L1.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L2.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L3.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L4.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L5.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L6.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L7.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L8.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L9.png')]
bg = pygame.image.load('/home/sourav/Desktop/firstgame/bg.jpg')
char = pygame.image.load('/home/sourav/Desktop/firstgame/standing.png')
clock= pygame.time.Clock()
music= pygame.mixer.music.load('/home/sourav/Desktop/firstgame/music1.mp3')
pygame.mixer.music.play(-1)
bulletSound = pygame.mixer.Sound('/home/sourav/Desktop/firstgame/bullet.ogg')
hitSound = pygame.mixer.Sound('/home/sourav/Desktop/firstgame/hit.ogg')

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing= True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)
    def hit(self):
        self.x = 60
        self.y = 410
        self.jumpCount=10
        self.isJump=False
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class projectile():
    def __init__(self,x,y,color,radius,facing):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.facing=facing
        self.vel=7*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
class enemy(object):
    walkRight = [pygame.image.load('/home/sourav/Desktop/firstgame/R1E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R2E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R3E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R4E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R5E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R6E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R7E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R8E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R9E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R10E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/R11E.png')]
    walkLeft = [pygame.image.load('/home/sourav/Desktop/firstgame/L1E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L2E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L3E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L4E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L5E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L6E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L7E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L8E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L9E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L10E.png'), pygame.image.load('/home/sourav/Desktop/firstgame/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end=end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.hitcount=0 
        self.health=30
        self.visible=True

    def draw(self, win):
        self.move()
        if self.visible:

            if self.walkCount + 1 >= 33:
                self.walkCount = 0
        
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 60, 10)) 
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 60 - (2 * (30 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 29, 55)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)    
    def move(self):
        
        
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
                
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
                
                
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        
    def hit(self):
        
        if self.health>0:
            self.health-=1
        else:
            self.visible= False
            

        if self.hitcount==5:
            self.hitcount=0
            


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    text = font.render("Score: " + str(score), 1, (0,0,0))
    win.blit(text,(350,10))
    villian.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    if villian.visible ==False:
        text1 = font.render("GAME OVER !! YOUR SCORE IS :" + str(score), 1, (0,0,0))
        win.blit(text1,(50,150))
        run =False

    pygame.display.update()

#mainloop
score=0
man = player(200, 410, 64,64)
villian=enemy(30,412,64,64,440)
run = True
shotperspace=0
bullets = []
while run:
    clock.tick(27)
    if villian.visible==True:
        if man.hitbox[1] < villian.hitbox[1] + villian.hitbox[3] and man.hitbox[1] + man.hitbox[3] > villian.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > villian.hitbox[0] and man.hitbox[0] < villian.hitbox[0] + villian.hitbox[2]:
                
                man.hit()
                score -= 5
    if shotperspace>0:
        shotperspace+=1
    if shotperspace>3:
        shotperspace=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if villian.visible==True:
            if bullet.y - bullet.radius < villian.hitbox[1] + villian.hitbox[3] and bullet.y + bullet.radius > villian.hitbox[1]:
                if bullet.x + bullet.radius > villian.hitbox[0] and bullet.x - bullet.radius < villian.hitbox[0] + villian.hitbox[2]:
                    villian.hitcount+=1
                    hitSound.play()
                
                    score+=1
                    villian.hit()
                    
                    bullets.pop(bullets.index(bullet))  
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel 
        else:
            bullets.pop(bullets.index(bullet)) 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shotperspace==0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2),(255,0,0),5, facing))
        shotperspace=1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing=False
    else:
        man.standing=True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
