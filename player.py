import pygame

class Player:

	screen = pygame.display.get_surface()

	def __init__():
		self.player_position_x = 0
		self.player_position_y = 0

	

	def start_game():

		player = Player(map)

		game = True

		while game:
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						player.move(0, -1, "up")
					if event.key == pygame.K_DOWN:
						player.move(0, 1, "down")
					if event.key == pygame.K_LEFT:
						player.move(-1, 0, "left")
					if event.key == pygame.K_RIGHT:
						player.move(1, 0, "right")