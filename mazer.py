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

    def get_neighbours(self, current, radius, step):
        '''yield the squares in radius of the centered one'''
        x,y = current
        angle = 0
        while angle < 360:
            next_x = x + radius*round(cos(radians(angle)))
            next_y = y + radius*round(sin(radians(angle)))
            angle += step
            coord = ((next_x, next_y))
            if coord in self.maze:
                if self.maze[coord] == 0:
                    yield coord

    def opening(self, current, choosen):
        """Return the square between two others"""
        x, y = current
        a, b = choosen
        return ((x + a) / 2, (y + b) / 2)

    def pathfinder(self):
        """Return the last openable wall"""
        corridors = list(self.get_coord(' '))
        corridors.reverse()
        for coord in corridors:
            if list(self.get_neighbours(coord, 2, 90)):
                return coord
        return None

    def check_odd(self, width, height):
        """Check if width and height are odd numbers"""
        try:
            width = int(width)
            height = int(height)
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
        start = (1, random.randrange(1, height - 1, 2))
        end = None
        current = start
        while current:
            squares = list(self.get_neighbours(current, 2, 90))
            if self.maze[current] != ' ':
                self.maze[current] = ' '
            for coord in list(self.get_neighbours(current, 1, 45)):
                self.maze[coord] = '#'
            if squares:
                choosen = squares.pop(random.randint(0, len(squares) - 1))
                doorway = self.opening(current, choosen)
                self.maze[doorway] = ' '
                current = choosen
            else:
                print(current)
                if not end and current[0] == width - 2:
                    end = current
                current = self.pathfinder()
        self.maze[start] = 's'
        self.maze[end] = 'e'
        maze = self.maze.copy()
        self.maze.clear()
        return Maze(width, height, maze, seed)
