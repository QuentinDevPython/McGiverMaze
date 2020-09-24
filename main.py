import pygame
from game import Game

class Main:

	def load_game():

		WHITE = (255, 255, 255)
		number_squares, size_squares = 15, 40
		screen_size = (number_squares * size_squares, number_squares * size_squares)

		pygame.init()

		screen = pygame.display.set_mode(screen_size)
		screen.fill(WHITE)

		pygame.display.set_caption("Save McGiver from the maze")

		load_images_list = Game.load_images(pygame)

		position_object = Game.random_position_objects()
		player = Game.maze_grid_initialization(screen, size_squares, load_images_list[0], load_images_list[1], load_images_list[2], load_images_list[3], load_images_list[4], load_images_list[5], load_images_list[6], load_images_list[7], load_images_list[8], position_object)

		Game.run_game(player, pygame, screen, load_images_list[1], load_images_list[4])

	load_game()