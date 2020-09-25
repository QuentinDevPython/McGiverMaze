from maze_map import Map
from player import Player
import random
from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN

class Game:

    def load_images(pygame):

        wall = pygame.image.load("ressource/wall.png").convert()
        floor = pygame.image.load("ressource/floor.png").convert()
        start = pygame.image.load("ressource/start.png").convert()
        end = pygame.image.load("ressource/end.png").convert()

        McGyver = pygame.image.load("ressource/MacGyver.png")
        Guardian = pygame.image.load("ressource/Guardian.png")

        plastic_tube = pygame.image.load("ressource/plastic_tube.png").convert_alpha()
        needle = pygame.image.load("ressource/needle.png").convert_alpha()
        syringe = pygame.image.load("ressource/syringe.png").convert_alpha()

        return wall, floor, start, end, McGyver, Guardian, plastic_tube, needle, syringe

    def random_position_objects():

        number_free_squares = 0
        position_object = [-1,-1,-1]

        for column_maze_grid in range(15):
            for line_maze_grid in range(15):
                if Map.maze_grid[line_maze_grid][column_maze_grid] == "0":
                    number_free_squares += 1

        position_object[0] = (random.randint(0, number_free_squares-1))

        position_object[1] = random.randint(0, number_free_squares-1)
        while position_object[1] == position_object[0]:
            position_object[1] = random.randint(0, number_free_squares-1)

        position_object[2] = random.randint(0, number_free_squares-1)
        while position_object[2] == position_object[0] or position_object[2] == position_object[1]:
            position_object[2] = random.randint(0, number_free_squares-1)

        return position_object

    def maze_grid_initialization(screen, size_squares, wall, floor, start, end, McGyver, Guardian, plastic_tube, needle, syringe, position_object):

        object_position = 0

        for column_maze_grid in range(15):
            for line_maze_grid in range(15):
                position = (column_maze_grid*size_squares, line_maze_grid*size_squares)

                if Map.maze_grid[line_maze_grid][column_maze_grid] == "9":
                    screen.blit(wall, (position[0],position[1]))

                if Map.maze_grid[line_maze_grid][column_maze_grid] == "0":
                    screen.blit(floor, (position[0],position[1]))
                    object_position += 1

                    if object_position == position_object[0]:
                        screen.blit(plastic_tube, (position[0],position[1]))
                        Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

                    if object_position == position_object[1]:
                        screen.blit(needle, (position[0],position[1]))
                        Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

                    if object_position == position_object[2]:
                        screen.blit(syringe, (position[0],position[1]))
                        Map.maze_grid[line_maze_grid][column_maze_grid] = "3"

                if Map.maze_grid[line_maze_grid][column_maze_grid] == "1":
                    screen.blit(start, (position[0],position[1]))
                    screen.blit(McGyver, (position[0]+3,position[1]-1))
                    player = Player(position, [])

                if Map.maze_grid[line_maze_grid][column_maze_grid] == "2":
                    screen.blit(end, (position[0],position[1]))
                    screen.blit(Guardian, (position[0]+3,position[1]+4))

        return player

    def run_game(player, pygame, screen, floor, McGyver):

        loop = True

        pygame.key.set_repeat(400,30)

        while loop:
            if player.is_victorious():
                loop = False
            else:
                pygame.time.Clock().tick(40)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    if event.type == pygame.KEYDOWN:

                        if event.key == K_RIGHT:

                            player.player_movement("right", -40, 0, 40, 0, screen, floor, McGyver, player)

                        if event.key == K_LEFT:

                            player.player_movement("left", 40, 0, -40, 0, screen, floor, McGyver, player)

                        if event.key == K_UP:

                            player.player_movement("up", 0, 40, 0, -40, screen, floor, McGyver, player)

                        if event.key == K_DOWN:

                            player.player_movement("down", 0, -40, 0, 40, screen, floor, McGyver, player)
							
                pygame.display.flip()	

        pygame.quit()