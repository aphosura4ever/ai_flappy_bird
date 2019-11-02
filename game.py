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

font = pygame.font.SysFont("comicsansms", 20)
white = (255,255,255)
score_text = font.render("Score: ", True, white)

def eval_genomes(genomes,config):


	neural_nets = []
	current_generation_genomes = []
	birds = []

	for genome_id,genome in genomes:
		
		net = neat.nn.FeedForwardNetwork.create(genome,config)
		neural_nets.append(net)
		birds.append(Bird(55,180,gameDisplay))
		genome.fitness = 0
		#print(genome)
		current_generation_genomes.append(genome)
		

		
	#bird = Bird(55,180,gameDisplay)
	
	pipe = Pipe(gameDisplay)
	


	gameExit = False
	space_status = 0;

	while not gameExit:
		#clock.tick(200)
	
		for event in pygame.event.get():
			print(event) 
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()

			"""
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					space_status = 1
			"""

		draw_background(BACKGROUND_IMAGE, [0,0])	
		pipe.draw()
		draw_base(BASE_IMAGE , [0,0+BASE_Y_COORDINATE_START])
		
		#for bird in birds:			
			
			
		

		for index,bird in enumerate(birds):
			bird.draw()	
			#output = neural_nets[index].activate((abs(pipe.x0-(bird.x+35)),abs(pipe.x1-(bird.x+35)),abs(pipe.x0+40-(bird.x+35)), pipe.pipes[0][0]+320,pipe.pipes[0][1]))
			output = neural_nets[index].activate((abs(pipe.x0-(bird.x+35)),abs(bird.y-pipe.pipes[0][0]+320),abs(bird.y-(pipe.pipes[0][0]+320+pipe.pipes[0][1])),abs(bird.y-400)))
			#print(bird.x),abs(pipe.x1-(bird.x+35)),abs(bird.y-pipe.pipes[1][0]+320),abs(bird.y-(pipe.pipes[1][0]+320+pipe.pipes[1][1]
			#print(pipe.x0)
			#print(pipe.x0-(bird.x+35))
			#print("Distance to the first pipe %d " %(pipe.x0-bird.x-35))
			#print("gap start: %d " %(pipe.pipes[0][0]+320))
			#print("gap distance %d " %(pipe.pipes[0][1]))
			#print(output)
			if (output[0]) > 0.5:
				space_status = 1
		
			bird.move(space_status)
			#current_generation_genomes[index].fitness = bird.fitness()
			space_status = 0 


		#print(bird.fitness_score)
		
		for index,bird in enumerate(birds):		
			if pipe.check_collision_with_pipe(bird.x , bird.y):
					
				current_generation_genomes[index].fitness -= 2/280
				neural_nets.pop(index)
				birds.pop(index)
				#current_generation_genomes[index].fitness -= 1
				current_generation_genomes.pop(index)
				
				if len(birds) == 0:
					pipe.score == 0
					gameExit = True 
			
			elif bird.check_collision():
				current_generation_genomes[index].fitness -= 8/280
				neural_nets.pop(index)
				birds.pop(index)
				#current_generation_genomes[index].fitness -= 1
				current_generation_genomes.pop(index)		

				if len(birds) == 0:
					pipe.score == 0
					gameExit = True
			else:
			
				#for _,genome in genomes:
					#genome.fitness += 1/20
					#print(genome.fitness)
				if bird.x == pipe.x0+50:
					current_generation_genomes[index].fitness += 30/280
					
				current_generation_genomes[index].fitness += 5/280
				#print(current_generation_genomes[index].fitness)












		gameDisplay.blit(score_text,(150,0))
		#print(bird.y)
		pipe.score_board(bird.x,bird.y,font)
		#print(current_generation_genomes[0])
		"""
		fitness_score_test = font.render(str(bird.fitness_score), True, white)
		gameDisplay.blit(fitness_score_test,(100,0))
		"""

	

		pygame.display.update()

		
			





def run(config_file):
	config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
	p = neat.Population(config)

	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)
	
	winner = p.run(eval_genomes, 1000)


if __name__ == '__main__':
	
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, 'config_neat.txt')
	run(config_path)




