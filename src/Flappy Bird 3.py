import pygame,os,sys
from pygame.locals import *
from random import randint as rand
from win32api import GetSystemMetrics


def game():

	def fps(x):pygame.time.Clock().tick(x)

	def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)

	#icon jogo
	pygame.display.set_icon(pygame.image.load(getdir('icon.ico')))
	    
	#Make window centered
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	#Recebe recorde guardado
	with open(getdir("record.txt"),"r") as f:RECORD = int(f.read())



	#Constantes
	SCREEN_WIDTH = GetSystemMetrics(0)
	SCREEN_HEIGHT = GetSystemMetrics(1)
	WIN_WIDTH=int(SCREEN_HEIGHT*0.6)
	WIN_HEIGHT=int(SCREEN_HEIGHT*0.8)
	PIPE_WIDTH=120
	PIPE_HEIGHT=500
	GAP=660
	MOVE= 15

	#controla habilidades
	smooth_jump = 0
	smooth_glide = 0
	smooth_hyper = 0
	glide_count = 3
	MOVE_count = 0
	hyper_jump = 3

	#Load de skins
	pygame.init()
	bird_skin=pygame.transform.scale(pygame.image.load(getdir('bird.png')),(65,60))	
	pipe_b_skin = pygame.transform.scale(pygame.image.load(getdir('pipe.png')),(PIPE_WIDTH,PIPE_HEIGHT))
	sky=pygame.image.load(getdir('sky.png'))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))

	#Variáveis principais
	pipex = WIN_WIDTH+100
	pipey_t =-rand(110,450)
	pipey_b=pipey_t +GAP
	pipe_t_collision=pipey_t +PIPE_HEIGHT
	pipe_b_collision=pipey_b
	pipe_t_skin = pygame.transform.rotate(pipe_b_skin,180)
	score = 0
	birdx,birdy=(100,200)
	floor_pos=(0,WIN_WIDTH)
	floor_skin = pygame.image.load(getdir('floor.png'))
	floor_x1,floor_x2,floor_width = 20,-WIN_WIDTH,floor_skin.get_width()


	# Main Game Loop
	jumped =False
	hyper_jumped = False
	glided = 0
	grav = 16
	grav_count = 0

	while 1:
		fps(30)

		#HARD INCRESED BY MOVE AND GRAV
		MOVE_count +=1
		if MOVE<35:
			if MOVE_count ==130:
				MOVE +=0.7
				MOVE_count = 0

		#Gravidade
		grav_count +=1
		if grav<20:
			if grav_count ==150:
				grav +=0.6
				grav_count = 0
		birdy+=grav

		#Catch Key Press
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key== K_SPACE:
					jumped = True
				if event.key== K_RIGHT:
					if glide_count>0:
						glided = True
						glide_count-=1
				if event.key== K_UP:
					if hyper_jump>0:
						hyper_jumped = True
						hyper_jump-=1
		if jumped :
			smooth_jump +=1
			birdy -=grav*2.5
			if smooth_jump ==2:
				jumped =False
				smooth_jump = 0	

		if hyper_jumped :
			smooth_hyper +=1
			birdy -=grav*5
			if smooth_hyper ==5:
				smooth_hyper =0
				hyper_jumped =False		

		if glided :
			smooth_glide +=1
			birdy -=12
			if smooth_glide ==15:
				smooth_glide =0
				glided =False

        #pipe move + score and col
		pipex-=MOVE
		if pipex<=-PIPE_WIDTH:
			pipex=WIN_WIDTH
			pipey_t =-rand(110,450)
			pipey_b=pipey_t +GAP
			pipe_t_collision=pipey_t +PIPE_HEIGHT
			pipe_b_collision=pipey_b
			score+=1

        #move floor
		floor_x1 -= MOVE 
		floor_x2 -= MOVE
		if floor_x1+floor_width<0:floor_x1=floor_x2+floor_width-2
		if floor_x2+floor_width<0:floor_x2=floor_x1+floor_width-2


		#Deteta se bird no chão ou fora da janela
		if birdy>=530:break
		if birdy<-60:break

		if abs(birdx -pipex)<55:
			if(birdy<=pipey_t+PIPE_HEIGHT):break
			if(birdy>=pipey_b-55):break
			
		#desenha tudo
		win.blit(sky,(0,0))
		win.blit(bird_skin, (birdx,birdy))
		win.blit(pipe_b_skin,(pipex,pipey_b))
		win.blit(pipe_t_skin,(pipex,pipey_t))
		win.blit(floor_skin, (floor_x1,580))
		win.blit(floor_skin, (floor_x2,580))

		
        #Escreve score
		pygame.font.init()
		font=pygame.font.SysFont('Arial', 50)
		text_surface= font.render(f'{score}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-10,10))

        #Guarda maior dos scores
		if score>RECORD:
			with open(getdir("record.txt"),"w") as f:f.write(str(score))
				
		pygame.display.update()

game()