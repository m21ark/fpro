import pygame
from pygame.locals import *
from random import randint
from pyautogui import alert
import tkinter
from random import randint as rand
import sys
import os

def fps(x):pygame.time.Clock().tick(x)

def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)
       
def main():
	#Constantes
	WIN_WIDTH=600
	WIN_HEIGHT=900
	PIPE_WIDTH=120
	PIPE_HEIGHT=460
	GAP=650
	MOVE= 20

	#Load de skins
	pygame.init()
	bird_skin=pygame.transform.scale(pygame.image.load(getdir('bird.png')),(65,60))	
	pipe_b_skin = pygame.transform.scale(pygame.image.load(getdir('pipe.png')),(PIPE_WIDTH,PIPE_HEIGHT))
	sky=pygame.image.load(getdir('sky.png'))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))

	#Definir variáveis principais	
	pipex = WIN_WIDTH+100
	pipey_t =rand(-350,0)
	pipey_b=pipey_t +GAP
	pipe_t_collision=pipey_t +PIPE_HEIGHT
	pipe_b_collision=pipey_b
	pipe_t_skin = pygame.transform.rotate(pipe_b_skin,180)
	score = 0
	birdx,birdy=(100,200)
	floor_pos=(0,WIN_WIDTH)
	floor_skin = pygame.image.load(getdir('floor.png'))
	floor_x1,floor_x2,floor_width = -MOVE,-WIN_WIDTH,floor_skin.get_width()

	#loop principal
	while True:
		fps(30)
		win.blit(sky,(0,0))

		#Key Press
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key== K_SPACE:
					birdy -=80

		#Deteta se bird fora da janela ou no chão
		if birdy>=WIN_HEIGHT-160:
			break

		if birdy<-50:
			break

        #Controla o movimento dos tubos e a pontuação
		pipex-=MOVE
		if pipex<=-PIPE_WIDTH:
			pipex=WIN_WIDTH
			pipey_t =rand(-350,0)
			pipey_b=pipey_t +GAP
			pipe_t_collision=pipey_t +PIPE_HEIGHT
			pipe_b_collision=pipey_b
			score+=1


		#Desenha tudo
		win.blit(bird_skin, (birdx,birdy))
		win.blit(pipe_b_skin,(pipex,pipey_b))
		win.blit(pipe_t_skin,(pipex,pipey_t))
		win.blit(floor_skin, (floor_x1,750))

		"""desenhos de hitbox
		pygame.draw.rect(win,(255,0,0)  , pygame.Rect(birdx, birdy,60 , 60)) 
		pygame.draw.rect(win,(0,255,0)  , pygame.Rect(pipex, pipey_t,PIPE_WIDTH ,465))
		pygame.draw.rect(win,(0,0,255)  , pygame.Rect(pipex, pipey_b,PIPE_WIDTH ,465))
		""" 

		#verifica colisao (V1 - Ainda tem algumas falhas sendo possivel bater no cano à saida dele)
		if abs(birdx -pipex)<60:
			if(birdy<=pipey_t+PIPE_HEIGHT):break
			if(birdy>=pipey_b-55):break

		#gravidade
		birdy +=18
			
        #trata da score
		pygame.font.init()
		font=pygame.font.SysFont('Arial', 50)
		text_surface= font.render(f'{score}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-10,10))

		#atualiza janela
		pygame.display.update()

main()