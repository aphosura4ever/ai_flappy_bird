import numpy as np 
import pygame
from bird import Bird
import neat 
from pipe import Pipe
import os
import random
import time

DISPLAY_WIDTH = 280
DISPLAY_HEIGHT = 500
BASE_Y_COORDINATE_START = 400
BACKGROUND_IMAGE = pygame.image.load(os.path.join('imgs','bg.png'))
BASE_IMAGE = pygame.image.load(os.path.join('imgs','base.png'))
config_file = 'config_neat.txt'

def draw_background(background,start_coordinates=[]):
	gameDisplay.blit(background,(start_coordinates[0],start_coordinates[1]))

def draw_base(base,base_start_coordinates = []):
	gameDisplay.blit(base, (base_start_coordinates[0],base_start_coordinates[1]))


pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('SMART Flappy Bird')

def eval_genomes(genomes,config):


	neural_nets = []
	genes = []
	birds = []

	for genome in genomes:
		net = neat.nn.FeedForwardNetwork(genome,config)
		neural_nets.append(net)
		birds.append(Bird(55,180))
		genome.fitness = 0
		genes.append(genome)
		
	bird = Bird(55,180,gameDisplay)
	pipe = Pipe(gameDisplay)

	font = pygame.font.SysFont("comicsansms", 20)
	white = (255,255,255)
	score_text = font.render("Score: ", True, white)

	gameExit = False

	clock = pygame.time.Clock()
	space_status = 0;



	while not gameExit:
		#clock.tick(200)
	
		for event in pygame.event.get():
			print(event) 
			if event.type == pygame.QUIT:
				gameExit = True 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					space_status = 1

		draw_background(BACKGROUND_IMAGE, [0,0])	
		bird.draw()
		pipe.draw()
		draw_base(BASE_IMAGE , [0,0+BASE_Y_COORDINATE_START])
		
		bird.move(space_status)
		space_status = 0
		bird.fitness()
		
		if bird.check_collision() or pipe.check_collision_with_pipe(bird.x , bird.y):
			 bird = Bird(55,180,gameDisplay)
			 pipe = Pipe(gameDisplay)
			 print(random.randint(0,DISPLAY_HEIGHT))
			 space_status = 0;
			 bird.fitness_score = 0
		


		gameDisplay.blit(score_text,(200,0))
		pipe.score_board(bird.x,bird.y,font)

		"""
		fitness_score_test = font.render(str(bird.fitness_score), True, white)
		gameDisplay.blit(fitness_score_test,(100,0))
		"""

		pygame.display.update()

	pygame.quit()
	quit()







def run(config_file):
	config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
	p = neat.Population(config)

	p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    
    winner = p.run(eval_genomes, 50)


if __name__ == '__main__':
   
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config_neat.txt')
    run(config_path)




