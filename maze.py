#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# maze.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT


class Maze:
    """A ramdomly generated maze"""
    def __init__(self, width, height, maze):
        self.width = width
        self.height = height
        self.maze = maze
        self.square_size = 1

    def set_square(self, size):
        """Change the size of the squares, so the coords in the dict"""
        new_maze = {}
        for coord, char in self.maze.items():
            x, y = coord
            x = (x / self.square_size) * size
            y = (y / self.square_size) * size
            new_maze[(x, y)] = char
        self.square_size = size
        self.maze = new_maze

    def get_coord(self, request):
        """Yield the square which matches the request"""
        for coord, char in self.maze.items():
            if char == request:
                yield coord

    def show(self):
        """Display the maze in the console"""
        line = ''
        for coord, value in self.maze.items():
            line += str(value)
            if coord[0] / self.square_size == self.width - 1:
                print(line)
                line = ''
        print('     ')
