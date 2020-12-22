import os,sys,pygame
from pygame.locals import *
from random import randint as rand
from win32api import GetSystemMetrics

def fps(x):pygame.time.Clock().tick(x)

def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)

#icon jogo
pygame.display.set_icon(pygame.image.load(getdir('icon.png')))
    
#Make window centered
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Recebe recorde guardado
with open(getdir("record.txt"),"r") as f:RECORD = int(f.read())
	
def main():
	#Constantes
	SCREEN_WIDTH = GetSystemMetrics(0)
	SCREEN_HEIGHT = GetSystemMetrics(1)
	WIN_WIDTH=int(SCREEN_HEIGHT*0.6)
	WIN_HEIGHT=int(SCREEN_HEIGHT*0.9)
	PIPE_WIDTH=120
	PIPE_HEIGHT=460
	GAP=650
	MOVE= 15

	#Load de skins
	pygame.init()
	bird_skin=pygame.transform.scale(pygame.image.load(getdir('bird4.png')),(65,60))	
	pipe_b_skin = pygame.transform.scale(pygame.image.load(getdir('pipe3.png')),(PIPE_WIDTH,PIPE_HEIGHT))
	sky=pygame.image.load(getdir('sky2.png'))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))

	#Variáveis principais
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


	#Loop Principal
	while 1:
		fps(40)
		win.blit(sky,(0,0))

		#Gravidade
		birdy +=9

		#Catch Key Press
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key== K_SPACE:
					birdy -=51

		#Deteta se bird no chão ou fora da janela
		if birdy>=620:break
		if birdy<-50:break

        #pipe move + score and col
		pipex-=MOVE
		if pipex<=-PIPE_WIDTH:
			pipex=WIN_WIDTH
			pipey_t =rand(-350,0)
			pipey_b=pipey_t +GAP
			pipe_t_collision=pipey_t +PIPE_HEIGHT
			pipe_b_collision=pipey_b
			score+=1

        #Move Chão
		floor_x1 -= MOVE 
		floor_x2 -= MOVE
		if floor_x1+floor_width<0:floor_x1=floor_x2+floor_width-2
		if floor_x2+floor_width<0:floor_x2=floor_x1+floor_width-2

		"""desenhos de hitbox
		pygame.draw.rect(win,(255,0,0)  , pygame.Rect(birdx, birdy,60 , 60)) 
		pygame.draw.rect(win,(0,255,0)  , pygame.Rect(pipex, pipey_t,PIPE_WIDTH ,465))
		pygame.draw.rect(win,(0,0,255)  , pygame.Rect(pipex, pipey_b,PIPE_WIDTH ,465))
		""" 

		#verifica colisao (V1 - Ainda tem algumas falhas sendo possiMOVE bater no cano à saida dele)
		if abs(birdx -pipex)<60:
			if(birdy<=pipey_t+PIPE_HEIGHT):break
			if(birdy>=pipey_b-55):break
			
		#Desenha tudo
		win.blit(pipe_b_skin,(pipex,pipey_b))
		win.blit(pipe_t_skin,(pipex,pipey_t))
		win.blit(floor_skin, (floor_x1,670))
		win.blit(floor_skin, (floor_x2,670))
		win.blit(bird_skin, (birdx,birdy))

        #Write score
		pygame.font.init()
		font=pygame.font.SysFont('Arial', 50)
		text_surface= font.render(f'{score}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-10,10))

		pygame.display.update()

		#Guarda novo recorde se maior q anterior
		if score>RECORD:
			with open(getdir("record.txt"),"w") as f:record = f.write(str(score))

main()