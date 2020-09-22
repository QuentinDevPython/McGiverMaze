import tkinter as tk 
import pygame

class Main:

	WHITE = (255, 255, 255)

	pygame.init()

	number_squares, size_squares = 15, 40
	
	screen_size = (number_squares * size_squares, number_squares * size_squares)
	 
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Save McGiver from the maze")

	loop = True

	while loop:
		pygame.time.Clock().tick(40)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False

		screen.fill(WHITE)
		pygame.display.flip()

	pygame.quit()

	



