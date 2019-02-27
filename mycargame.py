import pygame
import time
import random

pygame.init()#pygame initiation


display_width=700
display_height=900
#colours
black=(0,0,0)
white=(255,255,255)
sky_blue=(135,206,250)
block_colour=(100,100,250)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
##################################################################

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Car Game')
clock=pygame.time.Clock()

carImg=pygame.image.load('car1.png')
car_width=58
car_height=116


#Functions

def car(x,y):#blits car
    gameDisplay.blit(carImg,(x,y))
    pygame.display.update()

def things(thingx,thingy,thingw,thingh,colour):#blocks
    pygame.draw.rect(gameDisplay,colour,[thingx,thingy,thingw,thingh])
    pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):#creates button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)




def shoot(bx,by,x,y):#shooting function: under construction
    
    pygame.draw.rect(gameDisplay,black,[bx,by,10,15])
    return(by-7)


def things_dodged(count):#Score keeper
    font=pygame.font.SysFont(None,25)
    text=font.render('SCORE: '+str(count),True,black)
    gameDisplay.blit(text,(0,0))
                     
def text_objects(text,font):#for printing text
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def message_display(text):#accepts text to be printed
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width//2,display_height//2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():#crash function
    message_display('You Crashed')


def quitgame():#to quit
    pygame.quit()
    quit()

def game_intro():#intro page

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                quitgame()
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Car Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY!",100,550,100,50,green,bright_green,game_loop)
        button("Quit",500,550,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(5)

def game_loop():#event acces and handling loop
    
    
    gameExit =False
    x=(display_width*0.45)
    y=(display_height*0.7)
    x_change=0
    y_change=0
    thing_width=100
    thing_startx=random.randrange(0,display_width-thing_width)
    thing_starty=-600
    thing_speed=10
    thing_height=100
    
    dodged=0
    bx=x+(car_width//2)-2
    by=y


    while not gameExit:
        for event in pygame.event.get():    
            if event.type==pygame.QUIT:
                gameExit=True
            #print(event)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-15
                if event.key==pygame.K_RIGHT:
                    x_change=15
                if event.key==pygame.K_UP:
                    y_change=-15
                if event.key==pygame.K_DOWN:
                    y_change=15
                if event.key==pygame.K_SPACE:
                    by=y
                    by=shoot(bx,by,x,y)

                    
                    
            if event.type==pygame.KEYUP:
                if event.key== pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0
                #if event.key==pygame.K_SPACE:
                    #by=shoot(bx,by,x,y)
                    #if by<0:
                        #by=y


            
            '''if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    by=y
                    by=shoot(bx,by,x,y)
                
                    
                    
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    by=shoot(bx,by,x,y)
                    if by<0:
                        by=y'''        


        x+=x_change
        y+=y_change
                     
        

                     
        gameDisplay.fill(sky_blue)
                     
        things(thing_startx,thing_starty,thing_width,thing_height,block_colour)
        thing_starty+=thing_speed
                     
        car(x,y)
        things_dodged(dodged)

        ################################################################### CRASH BOUNDARIES
        if x<0 or x>display_width-car_width:
            crash()
        if y<0 or y>display_height-car_height:
            crash()
        ###################################################################



        ################################################################### BLOCK REGENERATE,SCORE AND DIFFICULTY
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width-thing_width)
            dodged+=1
            thing_speed+=10
            thing_width+=7
            if thing_speed>=200:
                thing_speed=50
            if thing_width>=150:
                thing_width=100
        ##################################################################   



        ######################################################## CRASH BLOCK
        if (y<thing_starty+thing_height and y>thing_starty)or(y+car_height>thing_starty and y+car_width<thing_starty+thing_height):
            #print('y crossover')
            if (x>thing_startx and x<thing_startx+thing_height) or (x+car_width>thing_startx and x+car_width<thing_startx+thing_width):
                #print('x crossover')
                crash()
        ##############################################


        ############################################################# SHOOTING SYSTEM UNDERWAY
        
                
                
        #bx=x+car_width//2

        '''if (by<thing_starty+thing_height):
            #print('bullet crossed')
            if (bx>thing_startx and bx<thing_startx+thing_height):
                #print('bullet aimed')

            

                thing_starty=0-thing_height
                thing_startx=random.randrange(0,display_width-thing_width)
                by=y
                bx=x+car_width//2
                dodged+=1

            
        #if by<0:
            #by=y
            #bx=x+car_width//2'''
            
         #########################################################################################       
        pygame.display.update()
        clock.tick(15)
game_intro()
game_loop()
pygame.quit()
quit()
