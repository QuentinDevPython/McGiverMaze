import pygame
import traceback
<<<<<<< Updated upstream
from map import Map
=======
from maze_map import Map
from player import *
import random
from pygame.locals import *
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======
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
				position_x = column_maze_grid*size_squares
				position_y = line_maze_grid*size_squares

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "9":
					screen.blit(wall, (position_x,position_y))

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "0":
					screen.blit(floor, (position_x,position_y))
					object_position += 1

					if object_position == position_plastic_tube:
						screen.blit(plastic_tube, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

					if object_position == position_needle:
						screen.blit(needle, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

					if object_position == position_syringe:
						screen.blit(syringe, (position_x,position_y))
						Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "1":
					screen.blit(start, (position_x,position_y))
					screen.blit(McGyver, (position_x+3,position_y-1))
					player = Player(position_x,position_y)

				if Map.maze_grid[line_maze_grid][column_maze_grid] == "2":
					screen.blit(end, (position_x,position_y))
					screen.blit(Guardian, (position_x+3,position_y+4))

		pygame.key.set_repeat(400,30)

		while loop:
			if player.is_Victorious():
				loop = False
			else:
				pygame.time.Clock().tick(40)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						loop = False
					if event.type == pygame.KEYDOWN:

						if event.key == K_RIGHT:

							if player.take_object("right"):
								print(player.inventory)
								screen.blit(floor,(Map.get_position_player()[0]*40 - 40, Map.get_position_player()[1]*40))
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40+ 3, Map.get_position_player()[1]*40 -1))

							elif player.can_be_moved("right"):
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40+ 40 + 3, Map.get_position_player()[1]*40 -1))
								player.move("right")

						if event.key == K_LEFT:

							if player.take_object("left"):
								print(player.inventory)
								screen.blit(floor,(Map.get_position_player()[0]*40 + 40, Map.get_position_player()[1]*40))
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40 + 3, Map.get_position_player()[1]*40 -1))

							elif player.can_be_moved("left"):
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40 - 40 + 3, Map.get_position_player()[1]*40-1))
								player.move("left")

						if event.key == K_UP:

							if player.take_object("up"):
								print(player.inventory)
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40+40))
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40 + 3, Map.get_position_player()[1]*40 -1))

							elif player.can_be_moved("up"):
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40+ 3, Map.get_position_player()[1]*40 - 40 -1))
								player.move("up")

						if event.key == K_DOWN:

							if player.take_object("down"):
								print(player.inventory)
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40-40))
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40 + 3, Map.get_position_player()[1]*40 -1))

							elif player.can_be_moved("down"):
								screen.blit(floor,(Map.get_position_player()[0]*40, Map.get_position_player()[1]*40))
								screen.blit(McGyver, (Map.get_position_player()[0]*40+ 3, Map.get_position_player()[1]*40 + 40 -1))
								player.move("down")
							
				pygame.display.flip()
				print(Map.maze_grid)
>>>>>>> Stashed changes

	except:
		traceback.print_exc()

	finally:
		pygame.quit()

