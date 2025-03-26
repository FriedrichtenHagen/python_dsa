class Maze():
    def __init__(self):
        self.maze = [
            ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
            ['+', ' ', ' ', ' ', '+', ' ', '+', ' ', ' ', 'S'],
            ['+', ' ', '+', ' ', ' ', ' ', '+', ' ', '+', '+'],
            ['+', ' ', '+', ' ', '+', ' ', '+', ' ', '+', '+'],
            ['+', '+', '+', ' ', '+', ' ', '+', ' ', ' ', '+'],
            ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
            ['+', '+', '+', '+', '+', '+', '+', '+', ' ', '+'],
            ['+', ' ', ' ', ' ', ' ', ' ', ' ', '+', ' ', '+'],
            ['+', ' ', '+', '+', '+', '+', ' ', ' ', ' ', '+'],
            ['+', ' ', ' ', ' ', ' ', '+', ' ', '+', '+', '+'],
            ['+', '+', '+', '+', 'X', '+', ' ', '+', '+', '+']
        ]
    
    def __str__(self):
        maze_rows = [''.join(row) for row in self.maze]  # Join each row into a string
        return '\n'.join(maze_rows)  # Join all rows with a newline character

class Adventurer():
    def __init__(self, maze):
        self.maze = maze.maze
        self.starting_position = self.find_starting_point()

    def find_starting_point(self):
        for row_index, row in enumerate(self.maze):
            for col_index, col in enumerate(self.maze[row_index]):
                if self.maze[row_index][col_index] == 'S':
                    self.current_pos = [row_index, col_index]
                    return [row_index, col_index]
        print('Starting point not found')
    
    def find_exit(self):
        self.attempt_steps(self.starting_position)

    def attempt_steps(self, position):
        print(f'Current pos: row {position[0]}, column {position[1]}')
        # base case: goal is reached
        if self.maze[position[0]][position[1]] == 'X':
            return position
        # mark previously reached fields
        self.maze[position[0]][position[1]] = '.'

        # go through all 4 possible steps:
        # down
        new_position = [None, None]
        new_position[0] = position[0] + 1
        new_position[1] = position[1] + 0
        if self.field_is_valid(new_position):
            self.attempt_steps(new_position)
        # up            
        # if self.maze[position[0] - 1][position[1]]:
        #     position[0] = position[0] - 1
        #     position[1] = position[1] + 0
        # # right
        # if self.maze[position[0]][position[1] + 1]:
        #     position[0] = position[0] + 0
        #     position[1] = position[1] + 1
        #     # left
        # if self.maze[position[0]][position[1] - 1]:    
        #     position[0] = position[0] + 0
        #     position[1] = position[0] - 1



    def field_is_valid(self, position):
        '''make sure the field is a valid part of the maze'''
        field_is_valid = self.maze[position[0]][position[1]] and self.maze[position[0]][position[1]] != '+' and self.maze[position[0]][position[1]] != '.'
        return field_is_valid





my_maze = Maze()
print(my_maze)

friedrich = Adventurer(my_maze)
starting_point = friedrich.find_starting_point()
print(starting_point)
friedrich.find_exit()
