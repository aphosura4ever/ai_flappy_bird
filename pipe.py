import pygame 
import os 
import random 

BOTTOM_PIPE = pygame.image.load(os.path.join('imgs','pipe.png'))
TOP_PIPE = pygame.transform.rotate(pygame.image.load(os.path.join('imgs','pipe.png')),180)
OUT_OF_SCREEN = 200
DISPLAY_HEIGHT= 500
white = (255,255,255)
class  Pipe:
	
	DISTANCE_BETWEEN_PIPES = 250


	"""docstring for  Pipe"""
	def __init__(self,gameDisplay):
		self.start_gap0 = random.randint(-320,-150) 
		self.gap0 = random.randint(100,150)
		self.start_gap1 = random.randint(-320,-150) 
		self.gap1 = random.randint(100,150)
		self.start_gap2 = random.randint(-320,-150) 
		self.gap2 = random.randint(100,150)
		self.gameDisplay = gameDisplay
		self.top_pipe_image = TOP_PIPE
		self.bottom_pipe_image = BOTTOM_PIPE
		self.x0 = OUT_OF_SCREEN
		self.x1 = OUT_OF_SCREEN + self.DISTANCE_BETWEEN_PIPES
		self.x2 = OUT_OF_SCREEN + 2*self.DISTANCE_BETWEEN_PIPES
		self.pipes = [ (self.start_gap0,self.gap0),(self.start_gap1,self.gap1),(self.start_gap2,self.gap2)]
		self.score = 0
		
	
	def add_pipe(self):
		new_start_gap = random.randint(-320,0) 
		new_gap = random.randint(80,150)
   

		self.pipes.pop(0)
		self.pipes.append((new_start_gap,new_gap))

		
		



	def draw(self):

		self.gameDisplay.blit(self.top_pipe_image, (self.x0,self.pipes[0][0]))
		self.gameDisplay.blit(self.bottom_pipe_image,(self.x0,self.pipes[0][0]+320+self.pipes[0][1]))


		self.gameDisplay.blit(self.top_pipe_image, (self.x1,self.pipes[1][0]))
		self.gameDisplay.blit(self.bottom_pipe_image,(self.x1,self.pipes[1][0]+320+self.pipes[1][1]))


		self.gameDisplay.blit(self.top_pipe_image, (self.x2,self.pipes[2][0]))
		self.gameDisplay.blit(self.bottom_pipe_image,(self.x2,self.pipes[2][0]+320+self.pipes[2][1]))

		self.x0 -= 0.5
		self.x1 -= 0.5
		self.x2 -= 0.5

		if self.x0 < -40: 
			self.x0 = self.x1
			self.x1 = self.x2
			self.x2 = OUT_OF_SCREEN + 2*self.DISTANCE_BETWEEN_PIPES
			self.add_pipe()


	def check_collision_with_pipe(self, bird_x, bird_y ):
		endGame = False 
		
		if (self.x0 < bird_x+35 and self.x0+50 > bird_x) and (self.pipes[0][0]+320 > bird_y or self.pipes[0][0]+320+self.pipes[0][1] < bird_y+23):
			endGame = True 
			self.score = 0
		return endGame 

	def score_board(self, bird_x, bird_y, font):
		
		
		if bird_x == self.x0+50:
			self.score+=1  
		
		
		score = font.render(str(self.score), True, white)
		
		self.gameDisplay.blit(score,(265,0))


