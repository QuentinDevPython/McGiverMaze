from maze_map import Map

class Player:

    def __init__(self, position, inventory):
        self.position=position
        self.inventory=inventory

    def get_inventory(self):
        return self.inventory

    def can_be_moved_list(self):
        right_movement=False
        left_movement=False
        up_movement=False
        down_movement=False
        position_x,position_y=Map.get_position_player()

        if Map.maze_grid[position_y][position_x + 1] == "0":
            right_movement=True

        if Map.maze_grid[position_y][position_x - 1] == "0":
            left_movement=True

        if Map.maze_grid[position_y - 1][position_x] == "0":
            up_movement=True

        if Map.maze_grid[position_y + 1][position_x] == "0":
            down_movement=True

        return [right_movement,left_movement,up_movement,down_movement]

    def can_be_moved(self, movement):
        position=Map.get_position_player()
        can_be_moved=False

        if movement == "right":
            if Map.maze_grid[position[1]][position[0] + 1] == "0":
                can_be_moved = True
            if Map.maze_grid[position[1]][position[0] + 1] == "3":
                can_be_moved = True

        if movement == "left":
            if Map.maze_grid[position[1]][position[0] - 1] == "0":
                can_be_moved = True
            if Map.maze_grid[position[1]][position[0] - 1] == "3":
                can_be_moved = True

        if movement == "up":
            if Map.maze_grid[position[1] - 1][position[0]] == "0":
                can_be_moved = True
            elif Map.maze_grid[position[1] - 1][position[0]] == "3":
                can_be_moved = True

        if movement == "down":
            if Map.maze_grid[position[1] + 1][position[0]] == "0":
                can_be_moved = True
            elif Map.maze_grid[position[1] + 1][position[0]] == "3":
                can_be_moved = True

        return can_be_moved

    def player_inventory(self):

        Player.get_inventory(self).append(True)
        print(Player.get_inventory(self))

    def player_movement(self,direction, add_floor_x, add_floor_y, add_player_x,
    	add_player_y, screen, floor, McGyver, player):
        if Map.take_object(self, direction):
            player.player_inventory()
            screen.blit(floor,(Map.get_position_player()[0] * 40 + add_floor_x,
            	Map.get_position_player()[1] * 40 + add_floor_y))
            screen.blit(floor,(Map.get_position_player()[0] * 40,
            	Map.get_position_player()[1] * 40))
            screen.blit(McGyver, (Map.get_position_player()[0] * 40 + 3,
            	Map.get_position_player()[1] * 40 - 1))

        elif player.can_be_moved(direction):
            screen.blit(floor,(Map.get_position_player()[0] * 40,
            	Map.get_position_player()[1] * 40))
            screen.blit(McGyver, (Map.get_position_player()[0] * 40 + add_player_x + 3,
            	Map.get_position_player()[1] * 40 + add_player_y - 1))
            player.move(direction)

    def move(self, movement):
        allowed_movements=Player.can_be_moved_list(self)
        Map.player_next_square(self, allowed_movements, movement)

    def is_victorious(self):
        win=False

        if Map.get_position_player()[0] == Map.get_position_Guardian()[0] - 1:
            if Map.get_position_player()[1] == Map.get_position_Guardian()[1]:
                if self.inventory == [True, True, True]:
                    print('Victory')
                    win = True

        elif Map.get_position_player()[0] == Map.get_position_Guardian()[0] - 1:
            if Map.get_position_player()[1] == Map.get_position_Guardian()[1]:
                if self.inventory != [True, True, True]:
                    print('Defeat')
                    win = True

        return win
