#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mazer.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

import random
from math import cos, sin, radians
from maze import Maze


class Mazer:
    """A maze generator"""
    def __init__(self):
        self.maze = {}

    def get_coord(self, request):
        """Yield the square which matches the request"""
        for coord, char in self.maze.items():
            if char == request:
                yield coord

    def get_neighbours(self, current, radius, step, char = 0):
        """yield the squares in radius of the centered one"""
        angle = 0
        while angle < 360:
            coord = (current[0] + radius*round(cos(radians(angle))),
                     current[1] + radius*round(sin(radians(angle))))
            angle += step
            if coord in self.maze and self.maze[coord] == char:
                yield coord

    def opening(self, current, choosen):
        """Return the square between two others"""
        x, y = current
        a, b = choosen
        return ((x + a) / 2, (y + b) / 2)

    def break_wall(self):
        """Return the last position where a wall can be openable"""
        corridors = list(self.get_coord(' '))
        corridors.reverse()
        for coord in corridors:
            if list(self.get_neighbours(coord, 2, 90)):
                return coord
        return None

    def check_odd(self, width, height):
        """Check if width and height are odd numbers"""
        try:
            width, height = int(width), int(height)
            if width % 2 == 0:
                width += 1
            if height % 2 == 0:
                height += 1
            return width, height
        except ValueError:
            print('\nUnexpected values for width and height !')
            print('Generating default maze : 31 x 31\n')
            return 31, 31

    def gen(self, width, height, seed = None):
        """Generate the maze"""
        width, height = self.check_odd(width, height)
        if seed:
            random.seed(seed)
        for y in range(height):
            for x in range(width):
                self.maze[(x, y)] = 0
        current = (random.randrange(1, width - 1, 2),
                   random.randrange(1, height - 1, 2))
        while current:
            self.maze[current] = ' '
            for coord in list(self.get_neighbours(current, 1, 45)):
                self.maze[coord] = '#'
            squares = list(self.get_neighbours(current, 2, 90))
            if squares:
                choosen = squares.pop(random.randint(0, len(squares) - 1))
                self.maze[self.opening(current, choosen)] = ' '
                current = choosen
            else:
                current = self.break_wall()
        self.maze[(0, random.randrange(1, height - 1, 2))] = 's'
        self.maze[(width - 1, random.randrange(1, height - 1, 2))] = 'e'
        maze = self.maze.copy()
        self.maze.clear()
        return Maze(width, height, maze, seed)
