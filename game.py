import pygame
import time
from random import randint
import ship
import alien
import missile
pygame.init()
display_width=480
display_height=480
black=(0,0,0)
white=(255,255,255)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Invaders')
clock=pygame.time.Clock()
def game_loop():
	x=(display_width*0.40)
	y=(display_height*0.87)
	x_change=0
	score=0
	aliensList=[]
	miss1=[]
	miss2=[]
	def text_object(text,font):
        	textSurface=font.render(text,True,black)
        	return textSurface,textSurface.get_rect()
	def message_display(text):
        	largeText=pygame.font.Font('freesansbold.ttf',15)
        	lookSurf,TextRect=text_object(text,largeText)
        	TextRect.center=(240,240)
        	gameDisplay.blit(lookSurf,TextRect)
        	pygame.display.update()
        	time.sleep(2)
	def crash():
        	message_display('Your score is '+str(score))

	lastAlien=time.time()
	GameExit=False
	while not GameExit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_a:
					x_change=-60
				elif event.key==pygame.K_d:
					x_change=60
				elif event.key==pygame.K_SPACE:
					miss1.append(missile.redmiss(x,y-0.75))
				elif event.key==pygame.K_s:
					miss2.append(missile.gmiss(x,y-1.5))
				elif event.key==pygame.K_q:
					GameExit=True
				elif event.key==pygame.K_p:#press P to get the score
					crash()
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_a or event.key==pygame.K_d:
					x_change=0
		for i in aliensList:
			if time.time()-i.clock>=8:
				aliensList.remove(i)
		if time.time()-lastAlien>=10:
			aliensList.append(alien.aliens(time.time(),randint(0,7)*60,randint(0,1)*60))
			lastAlien=time.time()
		x+=x_change
		if x > display_width-25 or x < -40:
                        x-=x_change
		gameDisplay.fill(white)
		ship.ship(x,y)
		for i in miss1:
			for j in aliensList:
				if (i.y-j.y <60 and i.x>j.x) and i.x-j.x <15:
					score+=1
					aliensList.remove(j)
					miss1.remove(i)
		for i in miss2:
			for j in aliensList:
				if (i.y-j.y<60 and i.x>j.x) and i.x-j.x<15:
					j.clock+=5
					j.hit=1
					miss2.remove(i)
		for i in miss1:
			i.y=i.y-60
			if i.y<0:
				miss1.remove(i)
		for i in miss2:
			i.y=i.y-120
			if i.y<0:
				miss2.remove(i)
		for i in miss1:#printing
			missile.missile1(i.x,i.y)
		for i in miss2:
			missile.missile2(i.x,i.y)
		for i in aliensList:
			if i.hit==0:
				alien.alien(i.x,i.y)
			else:
				alien.alienHit(i.x,i.y)
		pygame.display.update()
		clock.tick(5)

game_loop()
pygame.quit()
quit()
