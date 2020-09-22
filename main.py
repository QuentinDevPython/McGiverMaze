import pygame
import traceback
from map import Map
import random

class Main:

	WHITE = (255, 255, 255)

	number_squares, size_squares = 15, 40
	screen_size = (number_squares * size_squares, number_squares * size_squares)
	loop = True
	number_free_squares = 0
	object_position = 0

	try:
	
		pygame.init()

		screen = pygame.display.set_mode(screen_size)
		screen.fill(WHITE)

		pygame.display.set_caption("Save McGiver from the maze")

		wall = pygame.image.load("ressource/wall.png").convert()
		floor = pygame.image.load("ressource/floor.png").convert()
		start = pygame.image.load("ressource/start.png").convert()
		end = pygame.image.load("ressource/end.png").convert()

		McGyver = pygame.image.load("ressource/MacGyver.png")
		Guardian = pygame.image.load("ressource/Guardian.png")

		plastic_tube = pygame.image.load("ressource/plastic_tube.png").convert_alpha()
		needle = pygame.image.load("ressource/needle.png").convert_alpha()
		syringe = pygame.image.load("ressource/syringe.png").convert_alpha()

		for column_maze_grid in range(15):
				for line_maze_grid in range(15):
					if Map.maze_grid[line_maze_grid][column_maze_grid] == "0":
						number_free_squares += 1

		position_plastic_tube = random.randint(0, number_free_squares-1)

		position_needle = random.randint(0, number_free_squares-1)
		while position_needle == position_plastic_tube:
			position_needle = random.randint(0, number_free_squares-1)

		position_syringe = random.randint(0, number_free_squares-1)
		while position_syringe == position_plastic_tube or position_syringe == position_plastic_tube:
			position_syringe = random.randint(0, number_free_squares-1)

		for column_maze_grid in range(15):
			for line_maze_grid in range(15):
				position_x = column_maze_grid*40
				position_y = line_maze_grid*40

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "9":
					screen.blit(wall, (position_x,position_y))

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "0":
					screen.blit(floor, (position_x,position_y))
					object_position += 1

					if object_position == position_plastic_tube:
						screen.blit(plastic_tube, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = 3

					if object_position == position_needle:
						screen.blit(needle, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = 3

					if object_position == position_syringe:
						screen.blit(syringe, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = 3

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "1":
					screen.blit(start, (position_x,position_y))
					screen.blit(McGyver, (position_x+3,position_y-4))

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "2":
					screen.blit(end, (position_x,position_y))
					screen.blit(Guardian, (position_x+3,position_y+4))

		while loop:

			pygame.time.Clock().tick(40)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = False

			pygame.display.flip()

	except:

		traceback.print_exc()

	finally:

		pygame.quit()

