#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# maze.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

from math import cos, sin, radians


class Maze:
    """A ramdomly generated maze"""
    def __init__(self, width, height, maze, seed):
        self.width = width
        self.height = height
        self.square_x = width
        self.square_y = height
        self.square_size = 1
        self.maze = maze
        self.seed = seed

    def set_square(self, size):
        """Change the size of the squares, so the coords in the dict"""
        new_maze = {}
        self.width = self.square_x * size
        self.height = self.square_y * size
        for coord, char in self.maze.items():
            x, y = coord
            x = int(x / self.square_size) * size
            y = int(y / self.square_size) * size
            new_maze[(x, y)] = char
        self.square_size = size
        self.maze = new_maze

    def get_coord(self, request):
        """Yield the square which matches the request"""
        for coord, char in self.maze.items():
            if char == request:
                yield coord

    def get_neighbours(self, current, radius, angle=90, char=0):
        """return the squares in radius of the centered one"""
        neighbours = []
        compass = 0
        while compass < 360:
            coord = (current[0] + radius*round(cos(radians(compass))),
                     current[1] + radius*round(sin(radians(compass))))
            compass += angle
            if coord in self.maze and self.maze[coord] == char:
                neighbours.append(coord)
        return neighbours

    def show(self):
        """Display the maze in the console"""
        line = ''
        for coord, value in self.maze.items():
            line += str(value)
            if coord[0] / self.square_size == self.width - 1:
                print(line)
                line = ''

    def export_txt(self):
        """Save the maze in a txt file"""
        with open("maze.txt", "w") as file:
            line = ''
            for coord, value in self.maze.items():
                line += str(value)
                if coord[0] / self.square_size == self.width - 1:
                    file.write(line + '\n')
                    line = ''

    def solve(self):
        """Solve the maze (added '.' on the path)"""
        current = next(self.get_coord('s'))
        end = next(self.get_coord('e'))
        self.maze[end] = ' '
        marker = 1
        while current != end:
            neighbours = self.get_neighbours(current, self.square_size,
                                             char=' ')
            if len(neighbours) == 1:
                self.maze[current] = marker
                current = neighbours[0]
            elif len(neighbours) > 1:
                marker += 1
                self.maze[current] = str(marker) + 'x'
                current = neighbours[0]
            elif not neighbours:
                self.maze[current] = marker
                for coord, char in self.maze.items():
                    if char == marker:
                        self.maze[coord] = 0
                current = next(self.get_coord(str(marker) + 'x'))
                marker -= 1
        self.maze[end] = '.'
        for coord, char in self.maze.items():
            if char == 0:
                self.maze[coord] = ' '
            elif char != '#' and char != ' ':
                self.maze[coord] = '.'
