import pygame
import os
import random


BIRD_IMAGES = [pygame.image.load(os.path.join('imgs','bird1.png')), pygame.image.load(os.path.join('imgs','bird2.png')),pygame.image.load(os.path.join('imgs','bird3.png'))]
NOT_PRESSED = 0
PRESSED = 1
DISPLAY_WIDTH = 280
TOP_BORDER = 0
BASE_BORDER = 400 
BIRD_TALLNESS = 25
class Bird:

	
	SLOW_DOWN_FRAME = 3

	def __init__(self,x,height,gameDisplay):
		self.gameDisplay = gameDisplay
		self.CURRENT_IMAGE = BIRD_IMAGES[0]
		self.x = x
		self.y = height
		self.image_count = 0
		self.velocity = 0
		self.gravity = 0.01
		self.distance_traveled = 0
		self.fitness_score = 0



	def draw(self):
		self.image_count += 1

		if self.image_count < 5*self.SLOW_DOWN_FRAME:
			self.CURRENT_IMAGE = BIRD_IMAGES[0]
			
		elif 5*self.SLOW_DOWN_FRAME <= self.image_count < 10*self.SLOW_DOWN_FRAME:
			self.CURRENT_IMAGE = BIRD_IMAGES[1]
			
		elif 10*self.SLOW_DOWN_FRAME <=self.image_count < 20*self.SLOW_DOWN_FRAME:
			self.CURRENT_IMAGE = BIRD_IMAGES[2]
		
		elif self.image_count >= 20*self.SLOW_DOWN_FRAME:
			self.image_count = 0
		

		self.gameDisplay.blit(self.CURRENT_IMAGE, (self.x,self.y))


	def move(self,space_status):
		self.y += self.velocity
		self.velocity += self.gravity
			
		if space_status == PRESSED:
			self.velocity = -1
			self.gravity = 0.015
			


	def check_collision(self):
		endGame = False
		if self.y+BIRD_TALLNESS > BASE_BORDER:
			endGame = True 
		
		if self.y < TOP_BORDER:
			endGame = True  

		return endGame


		
	def fitness(self):

		self.fitness_score += 1/280
		#self.fitness_score =self.fitness_score / DISPLAY_WIDTH
		return self.fitness_score 