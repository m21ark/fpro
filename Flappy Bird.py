import pygame
from pygame.locals import *
from random import randint
from random import randint as rand
import sys
import os


def fps(x):pygame.time.Clock().tick(x)

def getdir(f_name):return os.path.join(os.path.dirname(__file__), f_name)
       

def main():
	WIN_WIDTH=600
	WIN_HEIGHT=900
	PIPE_WIDTH=120
	PIPE_HEIGHT=460
	GAP=650
	MOVE= 20


	pygame.init()
	bird_skin=pygame.transform.scale(pygame.image.load(getdir('bird.png')),(65,60))	
	pipe_b_skin = pygame.transform.scale(pygame.image.load(getdir('pipe.png')),(PIPE_WIDTH,PIPE_HEIGHT))
	sky=pygame.image.load(getdir('sky.png'))
	win=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
	pygame.display.set_caption('Flappy Bird')
	sky=pygame.transform.scale(sky,(WIN_WIDTH,WIN_HEIGHT))
	pipex = WIN_WIDTH+100
	pipey_t =rand(-350,0)
	pipey_b=pipey_t +GAP


	pipe_t_skin = pygame.transform.rotate(pipe_b_skin,180)
	score = 0
	birdx,birdy=(100,200)
	floor_pos=(0,WIN_WIDTH)
	floor_skin = pygame.image.load(getdir('floor.png'))
	floor_x1,floor_x2,floor_width = -MOVE,-WIN_WIDTH,floor_skin.get_width()


	while True:
		fps(30)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key== K_SPACE:
					birdy -=80

		if birdy>=WIN_HEIGHT-160:
			break

		if birdy<-50:
			break

		win.blit(sky,(0,0))
		win.blit(bird_skin, (birdx,birdy))
		win.blit(pipe_b_skin,(pipex,pipey_b))
		win.blit(pipe_t_skin,(pipex,pipey_t))
		win.blit(floor_skin, (floor_x1,750))
		pipex-=MOVE
		birdy +=18

		if pipex<=-PIPE_WIDTH:
			pipex=WIN_WIDTH
			pipey_t =rand(-350,0)
			pipey_b=pipey_t +GAP
			score+=1

		pygame.font.init()
		font=pygame.font.SysFont('Arial', 50)
		text_surface= font.render(f'{score}', False, (255,255,255))
		win.blit(text_surface,(WIN_WIDTH/2-10,10))


		pygame.display.update()

main()
