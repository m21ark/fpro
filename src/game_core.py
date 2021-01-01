import pygame,os,sys
from pygame.locals import *
from random import randint as rand
from random import choice

def game():

	def fps(x):pygame.time.Clock().tick(x)
	def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)

	#icon jogo
	pygame.display.set_icon(pygame.image.load(getdir('assets\\icon.ico')))
	    
	#Make window centered
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	#Recebe recorde guardado
	with open(getdir("assets\\stored_info.txt"),"r") as f:
		stored_info = f.read().split(",")
		RECORD = int(stored_info[0])
		COIN_VAULT = int(stored_info[1])

	#Constantes
	SCREEN_HEIGHT =  pygame.display.Info().current_h
	WIN_WIDTH=int(SCREEN_HEIGHT*0.6)
	WIN_HEIGHT=int(SCREEN_HEIGHT*0.8)
	PIPE_WIDTH=120
	PIPE_HEIGHT=500
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

	#Skin info load
	with open(getdir("assets\\skin_info.txt"),"r") as f:
		skins_list = f.read().split(",")

	bird_skins = skins_list[:skins_list.index("Xbird0")+1]
	pipe_skins = skins_list[skins_list.index("Xbird0")+1:skins_list.index("Xpipe0")+1]
	sky_skins = skins_list[skins_list.index("Xpipe0")+1:]

	bird_skins_have = list(map(lambda x: x.strip("X"),list(filter(lambda x:  "X" in x,bird_skins))))
	pipe_skins_have = list(map(lambda x: x.strip("X"),list(filter(lambda x:   "X" in x,pipe_skins))))
	sky_skins_have = list(map(lambda x: x.strip("X"),list(filter(lambda x:   "X" in x,sky_skins))))

	#Inicio de pygame
	pygame.init()


	#Load de skins
	bird_skin=pygame.transform.scale(pygame.image.load(getdir(f'assets\\{choice(bird_skins_have)}.png')),(65,60))	
	pipe_b_skin = pygame.transform.scale(pygame.image.load(getdir(f'assets\\{choice(pipe_skins_have)}.png')),(PIPE_WIDTH,PIPE_HEIGHT))
	sky=pygame.image.load(getdir(f'assets\\{choice(sky_skins_have)}.png'))

	#Load de outras informações
	coin=pygame.transform.scale(pygame.image.load(getdir('assets\\coin.png')),(40,45))
	coin_icon=pygame.transform.scale(pygame.image.load(getdir('assets\\coin.png')),(30,30))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))
	floor_skin = pygame.image.load(getdir('assets\\floor.png'))

	POINT_SOUND = pygame.mixer.Sound(getdir("assets\\point.wav"))
	DIE_SOUND = pygame.mixer.Sound(getdir("assets\\die.wav"))

	#Variáveis principais
	pipex = WIN_WIDTH+300
	coinx,coiny = (2*WIN_WIDTH+300,int(rand(50,500)))
	pipey_t =-rand(110,450)
	pipey_b=pipey_t +GAP
	pipe_t_collision=pipey_t +PIPE_HEIGHT
	pipe_b_collision=pipey_b
	pipe_t_skin = pygame.transform.rotate(pipe_b_skin,180)
	score = 0
	birdx,birdy=(100,200)
	floor_pos=(0,WIN_WIDTH)
	floor_x1,floor_x2,floor_width = 20,-WIN_WIDTH+27,floor_skin.get_width()


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
			with open(getdir("assets\\stored_info.txt"),"w") as f:
				record = f.write(str(",".join([str(i) for i in [score,COIN_VAULT]])))
		else:
			with open(getdir("assets\\stored_info.txt"),"w") as f:
				record = f.write(str(",".join([str(i) for i in [RECORD,COIN_VAULT]])))

		while 1:
			fps(20)
			win.blit(sky,(0,0))
			win.blit(pygame.image.load(getdir('assets\\gameover.png')),(WIN_WIDTH/2-160,150))
			pygame.font.init()
			font=pygame.font.SysFont('Arial', 50)
			text_surface1= font.render(f'Highscore:{RECORD}', False, (255,255,255))
			text_surface2= font.render(f'Score:{score}', False, (255,255,255))
			text_surface3= font.render(f'Coins:{COIN_VAULT}', False, (255,255,255))
			text_surface4= font.render(f'Press "ENTER" to restart!', False, (255,255,255))
			win.blit(text_surface1,(WIN_WIDTH/2-100,300))
			win.blit(text_surface2,(WIN_WIDTH/2-100,350))
			win.blit(text_surface3,(WIN_WIDTH/2-100,400))
			font=pygame.font.SysFont('Arial', 25)
			win.blit(text_surface4,(WIN_WIDTH/2-235,500))
			font=pygame.font.SysFont('Arial', 50)
			text_surface1= font.render(f'Highscore:{RECORD}', False, (0,0,0))
			text_surface2= font.render(f'Score:{score}', False, (0,0,0))
			text_surface3= font.render(f'Coins:{COIN_VAULT}', False, (0,0,0))
			text_surface4= font.render(f'Press "ENTER" to restart!', False, (0,0,0))
			win.blit(text_surface1,(WIN_WIDTH/2-105+2,300+2))
			win.blit(text_surface2,(WIN_WIDTH/2-105+2,350+2))
			win.blit(text_surface3,(WIN_WIDTH/2-105+2,400+2))
			font=pygame.font.SysFont('Arial', 25)
			win.blit(text_surface4,(WIN_WIDTH/2-235+2,500+2))


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
	grav = 15
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


		fps(30)

		#HARD INCRESED BY MOVE AND GRAV
		MOVE_count +=1
		if MOVE<40:
			if MOVE_count ==170:
				MOVE +=0.5
				MOVE_count = 0

		#Gravidade
		grav_count +=1
		if grav<25:
			if grav_count ==170:
				grav +=0.5
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
		if coinx<-1.5*WIN_WIDTH:
			coinx = 3.5*WIN_WIDTH
			coiny =int(rand(50,500))


        #move floor
		floor_x1 -= MOVE 
		floor_x2 -= MOVE
		if floor_x1+floor_width<0:floor_x1=floor_x2+floor_width-2
		if floor_x2+floor_width<0:floor_x2=floor_x1+floor_width-2

		#Deteta se bird no chão ou fora da janela ou colide
		if birdy>=530:
			DIE_SOUND.play()
			break
		if birdy<-60:
			DIE_SOUND.play()
			break

		#deteta colisao
		def  collide(t, win,bird_skin,pipe_tup):
			birdx,birdy = t
			bird_mask = pygame.mask.from_surface(bird_skin)
			pipe_t_skin,pipe_b_skin,pipex,pipey_b,pipey_t= pipe_tup 
			
			top_mask = pygame.mask.from_surface(pipe_t_skin)
			bottom_mask = pygame.mask.from_surface(pipe_b_skin)

			top_offset = (int(pipex) - int(birdx), int(pipey_t) - round(birdy))
			bottom_offset = (int(pipex) - int(birdx), int(pipey_b) - round(birdy))

			b_col = bird_mask.overlap(bottom_mask, (bottom_offset))
			t_col = bird_mask.overlap(top_mask,(top_offset))

			if b_col or t_col:return True
			return False

		if collide((birdx,birdy), win,bird_skin,(pipe_t_skin,pipe_b_skin,pipex,pipey_b,pipey_t)):
			DIE_SOUND.play()
			break

		#deteta apanhar moeda
		if abs(birdx -coinx)<50:
			if(abs(coiny-birdy)<40):
				POINT_SOUND.play()
				coinx = 1.5*WIN_WIDTH
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
		win.blit(coin_icon,(WIN_WIDTH-40,13))

		#Escreve score
		pygame.font.init()
		font=pygame.font.SysFont('Arial', 40)
		# Highscore
		text_surface= font.render(f'Higscore:{RECORD}', False, (255,255,255))
		win.blit(text_surface,(10,0))
		text_surface= font.render(f'Higscore:{RECORD}', False, (0,0,0))
		win.blit(text_surface,(10+2,0+2))
		# Score
		text_surface= font.render(f'Score:{score}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-50,0))
		text_surface= font.render(f'Score:{score}', False, (0,0,0))
		win.blit(text_surface,(WIN_WIDTH/2-50+2,0+2))
		# Coins
		text_surface= font.render(f'{COIN_VAULT}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH-90,0))
		text_surface= font.render(f'{COIN_VAULT}', False, (0,0,0))
		win.blit(text_surface,(WIN_WIDTH-90+2,0+2))
		if RECORD<score:
			RECORD = score
				
		pygame.display.update()


	#Guarda maior dos scores e moedas
	death(birdy)


# game()