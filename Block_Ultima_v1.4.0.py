from xml.sax import SAXNotRecognizedException
import pygame
import random
import math
pygame.font.init()
pygame.init
StaticFont = "Segou UI"
originalDisplayHeight = 500
originalDisplayWidth = 500
win = pygame.display.set_mode((500,500),pygame.RESIZABLE)
pygame.display.set_caption("Block Ultima")
run = True
NewWave = 20
# Draw Effect/s
def DrawEffects():
    i = 0
    x = 40
    y = 50
    while i < len(EffectsType):
        DrawRectCentered(win,70,70,70,x,y,13,30)
        if EffectsType[i] == "ChargeInvincibility":
            DrawRectCentered(win,250,25,25,x,y,10,math.floor((Effects1[i]/Effects2[i])*35))
        if EffectsType[i] == "ChargeCooldown":
            DrawRectCentered(win,250,250,50,x,y,10,math.floor((Effects1[i]/Effects2[i])*35))
        x = x + 45

        i = i+1

# Description for upgrade
def DrawUpgradeDescription(Type):
    if Type == 0:
        DrawText("Increases Crash Damage!",250,350,15,StaticFont,100,100,100,True)
    if Type == 1:
        DrawText("Makes enemy bullets hurt less!",250,350,15,StaticFont,100,100,100,True)
    if Type == 2:
        DrawText("Makes you faster!",250,350,15,StaticFont,100,100,100,True)
    if Type == 3:
        DrawText("Gives you 3% more gold per upgrade!",250,350,15,StaticFont,100,100,100,True)
    if Type == 4:
        DrawText("Gives you a dash ability!",250,350,15,StaticFont,100,100,100,True)
    if Type == 5:
        DrawText("Makes your ship hull stronger!",250,350,15,StaticFont,100,100,100,True)
    if Type == 6:
        DrawText("Increases your max Fuel!",250,350,15,StaticFont,100,100,100,True)
    if Type == 7:
        DrawText("Makes your crash fuelcells bigger!",250,350,15,StaticFont,100,100,100,True)
# Gold Cost for upgrades
def GenerateGoldCost(Type,Amount):
    cost = 0
    if Type == 0:
        cost = 1+Amount
    if Type == 1:
        cost = (5*Amount+1)*(Amount//2+1)
    if Type == 2:
        cost = 2*(Amount+1)
    if Type == 3:
        cost = 5*(((Amount+1)**2)/2)
    if Type == 4:
        cost = 2*((Amount+1)**3)
    if Type == 5:
        cost = 4*(Amount+1)
    if Type == 6:
        cost = 4*(Amount+1)
    if Type == 7:
        cost = 4*(Amount+1)
    return(cost)

# Fuel box generation

def fuelGenerator():
    boxX.append(random.randint(0,490))
    boxY.append(random.randint(0,490))
    if random.randint(1,4) == 4:
        boxType = "hp"
    else:
        boxType = "fuel"
    Box.append(boxType)

# Next Wave Also refills the enemies
def nextWave():
    global enemiesToBeSpawned
    global wave
    global NewWave
    if enemiesToBeSpawned == 0:
        if len(enemyHP) == 0:
            NewWave = 20
            wave = wave + 1
            if wave < 5:
                enemiesToBeSpawned = wave
            else:
                enemiesToBeSpawned = 5+((wave)%3)


# Despawn Bullets
def despawnBullets(i):
    BulletX.pop(i)
    BulletVelocityX.pop(i)
    BulletY.pop(i)
    BulletVelocityY.pop(i)
    BulletTeam.pop(i)
    

# Spawn enemies


def spawnEnemy():
    global enemiesToBeSpawned
    if enemiesToBeSpawned > 0:
        enemiesToBeSpawned = enemiesToBeSpawned -1
        X = random.randint(0,500)
        Y = random.randint(0,500)
        
        if random.randint(0,1) == 1:
            if X > 250:
                X = 0
            else: 
                X = 500
        else:
            if Y > 250:
                Y = 0
            else:
                Y = 500
        enemyX.append(X)
        enemyY.append(Y)
        enemyFireCooldownCalculate = 60 - wave//2
        if enemyFireCooldownCalculate <= 25:
            enemyFireCooldownCalculate = 30
        enemyHP.append(50+(wave*25))
        enemySpeed.append(0.5)
        enemyFireCooldown.append(enemyFireCooldownCalculate)
        enemyHeight.append(5)
        enemyWidth.append(5)

# The name says it all
def enemyDegreesTowardPlayer(x1,y1,x2,y2):
    radianAngle = math.atan2((y2-y1),(x2-x1))
    return(radianAngle)

# Random number generator
def Random(base ,randoriginal):
    rand = randoriginal*2
    rand = random.randint(0,rand)
    rand = randoriginal-rand
    base = base + rand
    return(base)

# Calculate the smallest for height and width
# CalculateHeightANDwidthIntoSmallesT = CHADIST
def CHADIST():
    if win.get_width() > win.get_height():
        return(win.get_height())
    else:
        return(win.get_width())

# Draw Next Wave
def DrawWave():
    global NewWave
    if NewWave > 0:
        NewWave=NewWave-1
        DrawText("Wave " + str(wave),100,50,30,"Segoe UI",120,240,240,True)



# Draw Rectangle(resizes with screen)
def DrawRect(surface,R,G,B,X,Y,W,H):
    pygame.draw.rect((surface),(R,G,B), (((CHADIST()/originalDisplayWidth)*X)+((win.get_width()-CHADIST())/2),((CHADIST()/originalDisplayHeight)*Y)+((win.get_height()-CHADIST())/2), (CHADIST()/originalDisplayWidth)*W, (CHADIST()/originalDisplayHeight)*H))

# Draw Rectangle thats Centered(resizes with screen)
def DrawRectCentered(surface,R,G,B,X,Y,W,H):
    X = X-W/2
    Y = Y-H/2
    pygame.draw.rect((surface),(R,G,B), (((CHADIST()/originalDisplayWidth)*X)+((win.get_width()-CHADIST())/2),((CHADIST()/originalDisplayHeight)*Y)+((win.get_height()-CHADIST())/2), (CHADIST()/originalDisplayWidth)*W, (CHADIST()/originalDisplayHeight)*H))

# Draw Text at X,Y with specific size,font and RGB (resizes with screen)
def DrawText(text,X,Y,Size,font,R,G,B,Boolean):
    font = pygame.font.SysFont(font, math.floor((CHADIST()/originalDisplayHeight)*Size))
    textSurface = font.render(text, Boolean, (R, G, B))
    textrect = textSurface.get_rect(center= ( math.floor(((CHADIST()/originalDisplayWidth)*X)+((win.get_width()-CHADIST())/2)),math.floor(((CHADIST()/originalDisplayHeight)*Y)+((win.get_height()-CHADIST())/2)) ))
    win.blit(textSurface, textrect)

# Draws an Image
def DrawImage(X,Y,imgname,rotation):
    image = pygame.image.load(imgname)
    Size = image.get_size()
    ratio = (CHADIST()/originalDisplayWidth)
    image1 = pygame.transform.scale(image ,(math.floor(ratio*Size[0]) , math.floor(ratio*Size[1])) ) 
    image2 = pygame.transform.rotate(image1, rotation)
    imgRect = image2.get_rect(center= ( math.floor(((CHADIST()/originalDisplayWidth)*X)+((win.get_width()-CHADIST())/2)),math.floor(((CHADIST()/originalDisplayHeight)*Y)+((win.get_height()-CHADIST())/2)) ))
    win.blit(image2, imgRect)

### Menu Variables
gold = 0
upgradetype = []
upgradeCount = []

listOfUpgradeTypes = [0,1,2,3,4,5,6,7]

listOfUpgradesNumber = [0,0,0,0,0,0,0,0]

Damage = 0
buyTypeNumber = 0
alreadychanged1 = 0
Dashes = 0

Buy = False
wave = 1
alive = True
restart = 1
gameWindow = "game"
while run:
    if restart == 1:
        restart = 0
        ## Variables
        # Player variables
        x = 250
        y = 250
        width = 5
        height = 5
        hp = 100
        hpmax = 100
        fuel = 25
        fuelmax = 25
        chargemeter = 0
        chargemax = 25
        i10 = 0
        i11 = 0

        # Movement variables , VelChange is speed
        velChange = 0.1
        velocityX = 0
        velocityY = 0

        # Trail variables
        xold = []
        yold = []

        # Enemy X,Y,HP,Speed,Firing cooldown
        enemyX = []
        enemyY = []
        enemyHP = []
        enemySpeed = []
        enemyFireCooldown = []

        # Enemy Hitbox
        enemyHeight = []
        enemyWidth = []

        # Enemy Spawn
        enemySpawnCooldown = 30
        if wave > 0:
            wave = wave - 1
        i3 = 0
        enemiesToBeSpawned = 0
        NewWave = 20

        # Enemy Bullet X,Y,VelocityX,VelocityY
        BulletX = []
        BulletY = []
        BulletVelocityX = []
        BulletVelocityY = []
        BulletTeam = []

        # Fuel boxes
        boxX = []
        boxY = []
        Box = []

        # Define Keys
        chargeon = 0

        # Define Effects
        EffectsType = []
        Effects1 = []
        Effects2 = []
        fuelGenerator()

        ### Menu variables
     
        # Gold variables
        enemyDeathCountThisRun = 0
    keys = pygame.key.get_pressed() 
    
    #Gets mouse position
    MousePosition = pygame.mouse.get_pos()
    MousePositionX = MousePosition[0]-(((win.get_width())-CHADIST())/2)
    MousePositionY = MousePosition[1]-(((win.get_height())-CHADIST())/2)
    MousePositionX = (MousePositionX)/(CHADIST()/(originalDisplayWidth))
    MousePositionY = (MousePositionY)/(CHADIST()/(originalDisplayHeight))
    #Upgrades
    pygame.time.delay(16)
    if listOfUpgradesNumber[0] > 0:
        Damage = 0.1*listOfUpgradesNumber[0]
    else:
        Damage = 0.1
    if listOfUpgradesNumber[1] > 0:
        Defence = 0.1*listOfUpgradesNumber[1]
    else:
        Defence = 0
    if listOfUpgradesNumber[2] > 0:
        velChange = 0.1*(1.01**listOfUpgradesNumber[2])
    if listOfUpgradesNumber[3] > 0:
        goldMultiplier = 1.4**listOfUpgradesNumber[3]
    else:
        goldMultiplier = 1
    # Dash
    DashMax = listOfUpgradesNumber[4] + 1
    if Dashes < DashMax:
        Dashes = Dashes +0.01
    if listOfUpgradesNumber[4] >= 0:
            if alive == True:
                DashAngle = enemyDegreesTowardPlayer(x,y,MousePositionX,MousePositionY)
                DistanceSpeed = enemyDegreesTowardPlayer(x,y,x+velocityX,y+velocityY)
                DashDistance = math.sqrt((x-MousePositionX)**2+(y-MousePositionY)**2)
                if DashDistance >= 40:
                    DashDistance = 40
                xd=x+math.cos(DashAngle)*DashDistance
                yd=y+math.sin(DashAngle)*DashDistance
                if keys[pygame.K_e]:
                    if math.floor(Dashes) > 0:
                        Dashes = Dashes - 1
                        print('dashed')
                        velocityX=math.cos(DashAngle)*((DistanceSpeed+1)*2)
                        velocityY=math.sin(DashAngle)*((DistanceSpeed+1)*2)
                        x=xd
                        y=yd
                
            
    if listOfUpgradesNumber[5] >= 0:
        hpmax= 100+25*listOfUpgradesNumber[5]
    if listOfUpgradesNumber[6] >= 0:
        fuelmax= 25+5*listOfUpgradesNumber[6]
    if listOfUpgradesNumber[7] >= 0:
        chargemax= 25+5*listOfUpgradesNumber[7]
        

    if keys[pygame.K_m]:
        if gameWindow == "menu":
            if alreadychanged == 0:
                gameWindow = "game"
                alreadychanged = 1
        if gameWindow == "game":
            if alreadychanged == 0:
                gameWindow = "menu"
                alreadychanged = 1
    else:
        alreadychanged = 0

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
    
    if gameWindow == "game":
        nextWave()
        chargeon = 0
        if alive == True:
        
            Drag = 1.05
            if keys[pygame.K_a]:
                velocityX = velocityX - velChange
                Drag = 1.01
            if keys[pygame.K_d]:
                velocityX = velocityX + velChange
                Drag = 1.01
            if keys[pygame.K_w]:
                velocityY = velocityY - velChange
                Drag = 1.01
            if keys[pygame.K_s]:    
                velocityY = velocityY + velChange
                Drag = 1.01
            if event.type == pygame.MOUSEBUTTONDOWN:    
                Lmb = pygame.mouse.get_pressed()
                if Lmb[0]:
                    chargeon = 1


        tryRestart = 0

        if keys[pygame.K_SPACE]:
            tryRestart = 1

        if chargemeter <= 0:
            charge = 0
            chargeon = 0
        i = 0
        while i < len(EffectsType):
            if Effects1[i] < Effects2[i]:
                Effects1[i] = Effects1[i] + 1
            else:
                Effects1.pop(i)
                Effects2.pop(i)
                EffectsType.pop(i)
            i=i+1
        # EffectsType = Type
        # Effects1 = The starting timer of the effect in 1000/16
        # Effects2 = when the effect will stop 
        if ("ChargeCooldown" in EffectsType) == False:
            if chargeon == 1:
                charge = 1
                chargeon = 0
                EffectsType.append("ChargeInvincibility")
                Effects1.append(0)
                Effects2.append(60)
                EffectsType.append("ChargeCooldown")
                Effects1.append(0)
                Effects2.append(120)

        velocityX = velocityX/Drag
        velocityY = velocityY/Drag

        x = x + velocityX
        y = y + velocityY
        # Check if player has went out of bounds
        if x > (500-width/2):
            x = 500 - width/2
            velocityX = 0 - velocityX
        if x < (0+width/2):
            x = 0+width/2
            velocityX = 0 - velocityX
        if y > (500-height/2):
            y = 500 - height
            velocityY = 0 - velocityY
        if y < (0+height/2):
            y = 0+height/2
            velocityY = 0 - velocityY




    
        win.fill((0,0,0))

        # Check for chargemeter
        if chargemeter <= 0:
            charge = 0

        # Enemy Movement and Damage
        i2 = 0
        while i2 < len(enemySpeed):
            radiansVar = enemyDegreesTowardPlayer(x,y,enemyX[i2],enemyY[i2])
            enemyDistanceFromPlayer = math.sqrt((x-enemyX[i2])**2+(y-enemyY[i2])**2)
            if charge == 1:
                if enemyDistanceFromPlayer < 20:
                    enemyHP[i2] =  enemyHP[i2]-((2*(math.sqrt((velocityX)**2+(velocityY)**2)))*(Damage+1))
            if enemyDistanceFromPlayer > 120:
                enemyX[i2]=   enemyX[i2]-math.cos(radiansVar)*enemySpeed[i2]
                enemyY[i2]=   enemyY[i2]-math.sin(radiansVar)*enemySpeed[i2]
            i2 = i2 + 1

        # Bullet and Enemy Collision
        i15 = 0
        while i15 < len(enemyX):
            i16=0
            while i16 < len(BulletX):
                if BulletTeam[i16] == "Player":
                    enemyDistanceFromPlayer = math.sqrt((BulletX[i16]-enemyX[i15])**2+(BulletY[i16]-enemyY[i15])**2)
                    if enemyDistanceFromPlayer < 20:
                        enemyHP[i15] =  enemyHP[i15]-(0.1*(math.sqrt((BulletX[i16]-BulletVelocityX[i16])**2+(BulletY[i16]-BulletVelocityY[i16])**2)))
                        BulletX.pop(i16)
                        BulletVelocityX.pop(i16)
                        BulletY.pop(i16)
                        BulletVelocityY.pop(i16)
                        BulletTeam.pop(i16)
                        break
                i16=i16+1
            i15=i15+1
        
        
        # Enemy Death
        i6 = 0
        while i6 < len(enemySpeed):
            if enemyHP[i6] <= 0:
                enemyHP.pop(i6)
                enemySpeed.pop(i6)
                enemyX.pop(i6)
                enemyY.pop(i6)
                enemyFireCooldown.pop(i6)
                enemyDeathCountThisRun = enemyDeathCountThisRun + 1
            i6 = i6+1
        
        # Enemy Spawning
        
        if enemySpawnCooldown <= i3:
            spawnEnemy()
            i3 = 0
        i3 = i3 + 1

        # Enemy anti Cliping
        i51 = 0
        i52 = 0
        while i51 < len(enemySpeed):
            while i52 < len(enemySpeed):
                if i51 == i52:
                    break
                radiansVar = enemyDegreesTowardPlayer(enemyX[i51],enemyY[i51],enemyX[i52],enemyY[i52])
                enemyDistanceFromPlayer = math.sqrt((enemyX[i51]-enemyX[i52])**2+(enemyY[i51]-enemyY[i52])**2)
                if enemyDistanceFromPlayer < 5:
                    enemyX[i51]=   enemyX[i51]-math.cos(radiansVar)*enemySpeed[i51]
                    enemyY[i51]=   enemyY[i51]-math.sin(radiansVar)*enemySpeed[i51]
                i52 = i52 +1
            i51 = i51 + 1
            i52 = 0



        # Enemy Firing
        i7 = 0
        while i7 < len(enemySpeed):
            radiansVar = enemyDegreesTowardPlayer(x,y,enemyX[i7],enemyY[i7])
            if enemyFireCooldown[i7] == 0:
                BulletVelocityX.append((math.cos(radiansVar))*2)
                BulletVelocityY.append((math.sin(radiansVar))*2)
                BulletX.append(enemyX[i7])
                BulletY.append(enemyY[i7])
                BulletTeam.append("Enemy")
                enemyFireCooldown[i7] = 61
            enemyFireCooldown[i7] = enemyFireCooldown[i7] - 1
            i7 = i7 +1

        # Enemy Bullet Velocity
        i9 = 0
        while i9 < len(BulletY):
            BulletY[i9] = BulletY[i9] - BulletVelocityY[i9]
            BulletX[i9] = BulletX[i9] - BulletVelocityX[i9]
            i9=i9+1
        # Check if bullets are offscreen
        i=0
        while i < len(BulletX):
            if BulletX[i] > (500-width/2):
                despawnBullets(i)
                break
            if BulletX[i] < 0+width/2:
                despawnBullets(i)
            i=i+1
        i=0
        while i < len(BulletX):
            if BulletY[i] > (500-height/2):
                despawnBullets(i)
                break
            if BulletY[i] < 0+height/2:
                despawnBullets(i)
            i=i+1
            
            
        # stats draw
        hpbar = hp/hpmax*500
        fuelbar = fuel/fuelmax*500
        chargebar = chargemeter/chargemax*500

        # Fuel to charge 
        if chargemax > chargemeter:
            if fuel > 0:
                fuel = fuel - 0.1
                chargemeter = chargemeter + 0.1

        # Charge used up
        if charge == 1:
            chargemeter = chargemeter - 0.5

        # Box collison
        i11 = 0
        while i11 < len(Box):
            enemyDistanceFromPlayer = math.sqrt((x-boxX[i11])**2+(y-boxY[i11])**2)
            if enemyDistanceFromPlayer < 20:
                if Box[i11] == "fuel":
                    fuel = fuel + 25
                if Box[i11] == "hp":
                    hp = hp + 25
                boxX.pop(0)
                boxY.pop(0)
                Box.pop(0)
            i11 = i11+1
        
        

        # Charge,Fuel overflow/underflow check
        if chargemeter < 0:
            chargemeter = 0
        if chargemeter >= chargemax:
            chargemeter = chargemax
        if fuel < 0:
            fuel = 0
        if fuel >= fuelmax:
            fuel = fuelmax

        # Hp Overflow check
        if hp > hpmax:
            hp = hpmax

        # Generate fuel boxes around the map
        if 1 > len(Box):
            fuelGenerator()


        # Check for bullet and player collision
        i14 = 0
        while i14 < len(BulletY):
            bulletDistanceFromPlayer = math.sqrt((x-BulletX[i14])**2+(y-BulletY[i14])**2)
            if bulletDistanceFromPlayer < 10:
                if ("ChargeInvincibility" in EffectsType) == False:
                    if BulletTeam[i14] == "Enemy":
                        enemydmg = (20+wave)-Defence
                        if enemydmg <= 0:
                            enemydmg = 1
                        hp = hp - enemydmg
                else:
                    if BulletTeam[i14] == "Enemy":
                        BulletVelocityY[i14] = 0 - BulletVelocityY[i14] 
                        BulletVelocityX[i14] = 0 - BulletVelocityX[i14] 
                        BulletTeam[i14] = "Player"
                if ("ChargeInvincibility" in EffectsType) == False:
                    BulletX.pop(i14)
                    BulletY.pop(i14)
                    BulletVelocityX.pop(i14)
                    BulletVelocityY.pop(i14)
            i14 = i14 + 1 

        ### Drawing
        ## Game Layer
        DrawEffects()

        DrawRectCentered(win,50,50,50,MousePositionX,MousePositionY,10,10)

        DrawRectCentered(win,50,50,50,250,496,(Dashes/DashMax)*500,8)

        DrawRectCentered(win,250,250,250,250,496,(math.floor(Dashes/DashMax))*500,8)

        # Draw Fuel boxes
        i13 = 0
        while i13 < len(Box):
            if Box[i13] == "fuel":
                DrawRect(win,90,90,90, boxX[i13], boxY[i13], 10, 10)
            if Box[i13] == "hp":
                DrawRect(win,90,150,90, boxX[i13], boxY[i13], 10, 10)
            i13 = i13 +1
        
        # Player trails
        if len(xold) > 10:
            xold.pop(0)
        if len(yold) > 10:
            yold.pop(0)

        xold.append(x)
        yold.append(y)

        i1 = 0
        while i1 < len(xold):
            R = Random(20,20)
            G = Random(20,20)
            B = Random(20,20)
            DrawRectCentered(win,R,G,B, xold[i1], yold[i1], width, height)
            i1 = i1 + 1
        
            # Enemy Bullet draw
        i8 = 0
        while i8 < len(BulletY):
            if BulletTeam[i8] == "Player":
                DrawRectCentered(win,0, 250, 0, BulletX[i8], BulletY[i8], 6, 6)
            if BulletTeam[i8] == "Enemy":
                DrawRectCentered(win,230, 0, 0, BulletX[i8], BulletY[i8], 6, 6)
            i8 = i8 + 1
        
        # Display the enemy
        i4 = 0
        while i4 < len(enemySpeed):
            DrawRectCentered(win,250, 200, 0, enemyX[i4], enemyY[i4], enemyWidth[i4], enemyHeight[i4])
            if enemyHP[i4] < (50+(wave*25)):
                enemyHpBarY = enemyY[i4] - 5
                enemyHpBarX = enemyX[i4] - 5
                enemyBarWidth = (enemyHP[i4]/(50+(wave*25)))*15
                DrawRectCentered(win,255, 190, 190, enemyHpBarX, enemyHpBarY, enemyBarWidth, 4)
            i4=i4+1

        
        # Draw HP,Fuel,Chargebar and the player 
        DrawRect(win,255,192,203, 0, 0, hpbar, 5)
        DrawRect(win,100,100,100, 0, 5, fuelbar, 5)
        DrawRect(win,230,230,0, 0, 10, chargebar, 5)

        if charge == 0:
            DrawRectCentered(win,232, 190, 172, x, y, width, height)
        if charge == 1:
            DrawRectCentered(win,255, 255, 255, x, y, width, height)
        if charge == 0:
            DrawRectCentered(win,232, 190, 172, xd, yd, width, height)
        if charge == 1:
            DrawRectCentered(win,255, 255, 255, xd, yd, width, height)

        # Death Message screen
       
        if hp <= 0:
            DrawText("You have Died...",250,250,25,"Helvetica",120,0,0,True)  
            DrawText("Press space to restart.",250,250,10,"Helvetica",50,0,0,True)  
            alive = False
            if tryRestart == 1:
                restart = 1
                alive = True
            if enemyDeathCountThisRun > 0:
                gold = gold + (math.floor(((enemyDeathCountThisRun*(((wave//2)*0.2)+1)*goldMultiplier)+0.000000000000001)*100))//100
                enemyDeathCountThisRun = 0
        DrawWave()
    if gameWindow == "menu":
        win.fill((5,5,5))
        
        DrawRectCentered(win,10,10,10,250,250,50,50)
        DrawRectCentered(win,50,50,50,200,250,35,35)
        DrawRectCentered(win,50,50,50,300,250,35,35)
        DrawText("Gold: "+str(gold),80,40,30,"Helvetica",210,210,10,True)
        displaySpriteType = 'ultima-sprites-' + str(buyTypeNumber) + '.png'
        DrawImage(250,250,displaySpriteType,0)
        keys = pygame.key.get_pressed() 
        AC1reset = False
        if keys[pygame.K_UP]:
            AC1reset = True
            if alreadychanged1 == False:
                buyTypeNumber = buyTypeNumber+1
                alreadychanged1 = True
        if keys[pygame.K_DOWN]: 
            AC1reset = True
            if alreadychanged1 == False:
                buyTypeNumber = buyTypeNumber-1
                alreadychanged1 = True
        if keys[pygame.K_b]: 
            AC1reset = True
            if alreadychanged1 == False:
                Buy = True
                alreadychanged1 = True
        if AC1reset == False:
            alreadychanged1 = False
        
        if buyTypeNumber > 7:
            buyTypeNumber = 0
        if buyTypeNumber < 0:
            buyTypeNumber = 7
        # Buying and displaying info about buying = cost,amount bought,desc

        if Buy == True:
            Buy = False
            Cost = GenerateGoldCost(buyTypeNumber,listOfUpgradesNumber[buyTypeNumber])
            if gold >= Cost:
                listOfUpgradesNumber[buyTypeNumber] = listOfUpgradesNumber[buyTypeNumber] + 1
                gold = gold - Cost
        DrawText("Cost: "+str(GenerateGoldCost(buyTypeNumber,listOfUpgradesNumber[buyTypeNumber])),250,290,30,StaticFont,210,210,10,True)
        DrawText("Amount Bought: "+str(listOfUpgradesNumber[buyTypeNumber]),250,315,23,StaticFont,210,210,10,True)
        DrawText("Press B to buy,Up and Down to change Upgrade ",250,365,15,StaticFont,210,210,10,True)
        DrawUpgradeDescription(buyTypeNumber)


    pygame.display.update()
pygame.quit()