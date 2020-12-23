import pygame,os,sys
from pygame.locals import *
from random import randint as rand
from win32api import GetSystemMetrics
from time import sleep

def game():

	def fps(x):pygame.time.Clock().tick(x)
	def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)

	#icon jogo
	pygame.display.set_icon(pygame.image.load(getdir('icon.ico')))
	    
	#Make window centered
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	#Recebe recorde guardado
	with open(getdir("stored_info.txt"),"r") as f:
		stored_info = f.read().split(",")
		RECORD = int(stored_info[0])
		COIN_VAULT = int(stored_info[1])

	#Constantes
	SCREEN_WIDTH = GetSystemMetrics(0)
	SCREEN_HEIGHT = GetSystemMetrics(1)
	WIN_WIDTH=int(SCREEN_HEIGHT*0.6)
	WIN_HEIGHT=int(SCREEN_HEIGHT*0.8)
	PIPE_WIDTH=120
	PIPE_HEIGHT=500
	SPACER = 1000 #espaco entre moedas consecutivas
	GAP=660
	MOVE= 15
	RUN = True
	ATSTART = True

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
	coin=pygame.transform.scale(pygame.image.load(getdir('coin.png')),(40,45))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))

	POINT_SOUND = pygame.mixer.Sound(getdir("point.wav"))
	DIE_SOUND = pygame.mixer.Sound(getdir("die.wav"))

	#Variáveis principais
	pipex = WIN_WIDTH+300
	coinx,coiny = (SPACER,int(rand(50,500)))
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


	def death(birdy):
		while birdy<800:
			birdy +=10
			win.blit(sky,(0,0))
			win.blit(coin,(coinx,coiny))
			win.blit(pipe_b_skin,(pipex,pipey_b))
			win.blit(pipe_t_skin,(pipex,pipey_t))
			win.blit(bird_skin, (birdx,birdy))
			win.blit(floor_skin, (floor_x1,580))
			win.blit(floor_skin, (floor_x2,580))
			pygame.display.update()


		if score>RECORD:
			with open(getdir("stored_info.txt"),"w") as f:
				record = f.write(str(",".join([str(i) for i in [score,COIN_VAULT]])))
		else:
			with open(getdir("stored_info.txt"),"w") as f:
				record = f.write(str(",".join([str(i) for i in [RECORD,COIN_VAULT]])))

		while 1:
			fps(20)
			win.blit(sky,(0,0))
			win.blit(pygame.image.load(getdir('gameover.png')),(WIN_WIDTH/2-160,150))
			pygame.font.init()
			font=pygame.font.SysFont('Arial', 50)
			text_surface1= font.render(f'Highscore:{RECORD}', False, (0,0,0))
			text_surface2= font.render(f'Score:{score}', False, (0,0,0))
			text_surface3= font.render(f'Coins:{COIN_VAULT}', False, (0,0,0))
			text_surface4= font.render(f'Press "ENTER" to restart!', False, (0,0,0))
			win.blit(text_surface1,(WIN_WIDTH/2-100,300))
			win.blit(text_surface2,(WIN_WIDTH/2-100,350))
			win.blit(text_surface3,(WIN_WIDTH/2-100,400))
			font=pygame.font.SysFont('Arial', 30)
			win.blit(text_surface4,(WIN_WIDTH/2-230,500))

			sleep(1)
			#Catch Key Press
			for event in pygame.event.get():
				if event.type==QUIT:
					pygame.quit()
					sys.exit()
				if event.type==KEYDOWN:
					if event.key== K_RETURN:
						game()

			pygame.display.update()





	# Main Game Loop
	jumped =False
	hyper_jumped = False
	glided = 0
	grav = 16
	grav_count = 0


	
	while RUN:
		if ATSTART:
			for event in pygame.event.get():
				if event.type==QUIT:
					pygame.quit()
					sys.exit()
				if event.type==KEYDOWN:
					if event.key== K_SPACE:
						ATSTART = False

			#desenha tudo
			win.blit(sky,(0,0))
			win.blit(coin,(coinx,coiny))
			win.blit(pipe_b_skin,(pipex,pipey_b))
			win.blit(pipe_t_skin,(pipex,pipey_t))
			win.blit(bird_skin, (birdx,birdy))
			win.blit(floor_skin, (floor_x1,580))
			win.blit(floor_skin, (floor_x2,580))
			pygame.display.update()
			fps(20)
			continue


		fps(60)

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
			

		#Coin Controller
		coinx -=MOVE
		if coinx<-SPACER:
			coinx = int(rand(SPACER,2*SPACER))+321
			coiny =int(rand(50,500))


        #move floor
		floor_x1 -= MOVE 
		floor_x2 -= MOVE
		if floor_x1+floor_width<0:floor_x1=floor_x2+floor_width-2
		if floor_x2+floor_width<0:floor_x2=floor_x1+floor_width-2

		#Deteta se bird no chão ou fora da janela ou colide
		if birdy>=530:
			DIE_SOUND.play()
			sleep(1)
			break
		if birdy<-60:
			DIE_SOUND.play()
			sleep(1)
			break

		if abs(birdx -pipex)<55:
			if(birdy<=pipey_t+PIPE_HEIGHT):
				DIE_SOUND.play()
				sleep(1)
				break
			if(birdy>=pipey_b-55):
				DIE_SOUND.play()
				sleep(1)
				break

		#deteta apanhar moeda
		if abs(birdx -coinx)<50:
			if(abs(coiny-birdy)<40):
				POINT_SOUND.play()
				coinx = int(rand(SPACER,2*SPACER))+321
				coiny =int(rand(50,500))
				COIN_VAULT +=1


		#desenha tudo
		win.blit(sky,(0,0))
		win.blit(coin,(coinx,coiny))
		win.blit(pipe_b_skin,(pipex,pipey_b))
		win.blit(pipe_t_skin,(pipex,pipey_t))
		win.blit(bird_skin, (birdx,birdy))
		win.blit(floor_skin, (floor_x1,580))
		win.blit(floor_skin, (floor_x2,580))

		#Escreve score
		pygame.font.init()
		font=pygame.font.SysFont('Arial', 50)
		text_surface= font.render(f'H:{RECORD},S:{score},C:{COIN_VAULT}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-120,10))
		if RECORD<score:
			RECORD = score
				
		pygame.display.update()


	#Guarda maior dos scores e moedas
	death(birdy)


game()