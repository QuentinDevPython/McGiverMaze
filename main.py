import pygame
import traceback
from map import Map

class Main:

	WHITE = (255, 255, 255)

	number_squares, size_squares = 15, 40
	screen_size = (number_squares * size_squares, number_squares * size_squares)
	loop = True

	try:
	
		pygame.init()

		

		screen = pygame.display.set_mode(screen_size)
		screen.fill(WHITE)

		pygame.display.set_caption("Save McGiver from the maze")

		wall = pygame.image.load("ressource/wall.png").convert()
		floor = pygame.image.load("ressource/floor.png")
		start = pygame.image.load("ressource/start.png")
		end = pygame.image.load("ressource/end.png")
		McGyver = pygame.image.load("ressource/MacGyver.png")
		Guardian = pygame.image.load("ressource/Guardian.png")

		while loop:
			pygame.time.Clock().tick(40)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = False

			for i in range(15):
				for j in range(15):
					x = i*40
					y = j*40
					if Map.maze_grid[i][j] == "9":
						screen.blit(wall, (x,y))
					if Map.maze_grid[i][j] == "0":
						screen.blit(floor, (x,y))
					if Map.maze_grid[i][j] == "1":
						screen.blit(start, (x,y))
						screen.blit(McGyver, (x+3,y))
					if Map.maze_grid[i][j] == "2":
						screen.blit(end, (x,y))
						screen.blit(Guardian, (x+3,y+4))
			#endroit où construire ma map

			pygame.display.flip()

	except:
		traceback.print_exc()

	finally:
		pygame.quit()

