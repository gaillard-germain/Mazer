#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mazer.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

import random
from math import cos, sin, radians
from mazer_app import Maze


class Mazer:
    """A maze generator"""
    def __init__(self):
        self.maze = {}

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
            if self.get_neighbours(coord, 2):
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

    def gen(self, width, height, seed=None):
        """Generate the maze"""
        width, height = self.check_odd(width, height)
        if seed:
            random.seed(seed)
        for y in range(height):
            for x in range(width):
                self.maze[(x, y)] = 0
        current = (1, 1)
        while current:
            self.maze[current] = ' '
            for coord in self.get_neighbours(current, 1, 45):
                self.maze[coord] = '#'
            neighbours = self.get_neighbours(current, 2)
            if neighbours:
                choosen = neighbours.pop(random.randint(0,
                                         len(neighbours) - 1))
                self.maze[self.opening(current, choosen)] = ' '
                current = choosen
            else:
                current = self.break_wall()
        if random.getrandbits(1):
            self.maze[(random.randrange(1, width - 1, 2), 0)] = 's'
            self.maze[(random.randrange(1, width - 1, 2), height - 1)] = 'e'
        else:
            self.maze[(0, random.randrange(1, height - 1, 2))] = 's'
            self.maze[(width - 1, random.randrange(1, height - 1, 2))] = 'e'
        maze = self.maze.copy()
        self.maze.clear()
        return Maze(width, height, maze, seed)
