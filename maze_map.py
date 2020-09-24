class Map:

	WIDTH = 15
	LENGHT = 15

	maze_grid = []

	index = 0

	for line_maze_grid in range(LENGHT):
		maze_grid.append([0] * WIDTH)

	maze_file = open("maze_grid.txt", "r")
	contenu_maze_file = maze_file.read()
	contenu_maze_file = contenu_maze_file.split()

	for column_maze_grid in range(WIDTH):
		for line_maze_grid in range(LENGHT):
			if (column_maze_grid, line_maze_grid) != (0,0):
				index += 1
			maze_grid[column_maze_grid][line_maze_grid] = contenu_maze_file[index]

	maze_file.close()

	def get_position_player():
		for column_maze_grid in range(Map.WIDTH):
			for line_maze_grid in range(Map.LENGHT):
				if Map.maze_grid[column_maze_grid][line_maze_grid] == "1":
					position = (line_maze_grid,column_maze_grid)
					return position

	def get_position_Guardian():
		for column_maze_grid in range(Map.WIDTH):
			for line_maze_grid in range(Map.LENGHT):
				if Map.maze_grid[column_maze_grid][line_maze_grid] == "2":
					position = (line_maze_grid,column_maze_grid)
					return position

	def take_object(self, movement):

		position = Map.get_position_player()

		if movement == "right" and Map.maze_grid[position[1]][position[0]+1] == "3":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]][position[0]+1] = "1"
			return True

		if movement == "left" and Map.maze_grid[position[1]][position[0]-1] == "3":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]][position[0]-1] = "1"
			return True

		if movement == "up" and Map.maze_grid[position[1]-1][position[0]] == "3":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]-1][position[0]] = "1"
			return True

		if movement == "down" and Map.maze_grid[position[1]+1][position[0]] == "3":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]+1][position[0]] = "1"
			return True

	def player_next_square(self, allowed_movements, movement):

		position = Map.get_position_player()

		if allowed_movements[0] == True and movement == "right":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]][position[0]+1] = "1"

		if allowed_movements[1] == True and movement == "left":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]][position[0]-1] = "1"

		if allowed_movements[2] == True and movement == "up":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]-1][position[0]] = "1"

		if allowed_movements[3] == True and movement == "down":
			Map.maze_grid[position[1]][position[0]] = "0"
			Map.maze_grid[position[1]+1][position[0]] = "1"
