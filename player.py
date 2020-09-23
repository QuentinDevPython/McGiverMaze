from maze_map import Map

class Player:

	size_squares = 40

	inventory = []

	def __init__(self, position_x, position_y):
		self.position_x = position_x
		self.position_y = position_y

	def can_be_moved_list(self):

		right_movement = False
		left_movement = False
		up_movement = False
		down_movement = False

		position_x,position_y = Map.get_position_player()

		if Map.maze_grid[position_y][position_x+1] == "0":
			right_movement = True
		if Map.maze_grid[position_y][position_x-1] == "0":
			left_movement = True
		if Map.maze_grid[position_y-1][position_x] == "0":
			up_movement = True
		if Map.maze_grid[position_y+1][position_x] == "0":
			down_movement = True

		return [right_movement,left_movement,up_movement,down_movement]

	def can_be_moved(self, movement):

		position_x,position_y = Map.get_position_player()

		if movement == "right" and (Map.maze_grid[position_y][position_x+1] == "0" or Map.maze_grid[position_y][position_x+1] == "3"):
			return True
		if movement == "left" and (Map.maze_grid[position_y][position_x-1] == "0" or Map.maze_grid[position_y][position_x-1] == "3"):
			return True
		if movement == "up" and (Map.maze_grid[position_y-1][position_x] == "0" or Map.maze_grid[position_y-1][position_x] == "3"):
			return True
		if movement == "down" and (Map.maze_grid[position_y+1][position_x] == "0" or Map.maze_grid[position_y+1][position_x] == "3"):
			return True

	def take_object(self, movement):

		position_x,position_y = Map.get_position_player()

		if movement == "right" and Map.maze_grid[position_y][position_x+1] == "3":
			Player.inventory.append(True)
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y][position_x+1] = "1"
			return True

		if movement == "left" and Map.maze_grid[position_y][position_x-1] == "3":
			Player.inventory.append(True)
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y][position_x-1] = "1"
			return True

		if movement == "up" and Map.maze_grid[position_y-1][position_x] == "3":
			Player.inventory.append(True)
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y-1][position_x] = "1"
			return True


		if movement == "down" and Map.maze_grid[position_y+1][position_x] == "3":
			Player.inventory.append(True)
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y+1][position_x] = "1"
			return True

	def move(self, movement):

		position_x,position_y = Map.get_position_player()

		allowed_movements = Player.can_be_moved_list(self)

		if allowed_movements[0] == True and movement == "right":
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y][position_x+1] = "1"

		if allowed_movements[1] == True and movement == "left":
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y][position_x-1] = "1"

		if allowed_movements[2] == True and movement == "up":
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y-1][position_x] = "1"

		if allowed_movements[3] == True and movement == "down":
			Map.maze_grid[position_y][position_x] = "0"
			Map.maze_grid[position_y+1][position_x] = "1"

	def is_Victorious(self):

		if Map.get_position_player()[0] == Map.get_position_Guardian()[0]-1 and Map.get_position_player()[1] == Map.get_position_Guardian()[1] and Player.inventory == [True, True, True]:
			print('Victory')
			return True

		elif Map.get_position_player()[0] == Map.get_position_Guardian()[0]-1 and Map.get_position_player()[1] == Map.get_position_Guardian()[1] and Player.inventory != [True, True, True]:
			print('Defeat')
			return True

		else: 
			pass
