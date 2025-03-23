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


my_maze = Maze()
print(my_maze)