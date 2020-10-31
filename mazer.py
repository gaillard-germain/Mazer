#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mazer.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

import random
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

    def available(self, current, reach):
        """Yield the reachables squares"""
        x, y = current
        cardinal = {}
        cardinal['west'] = (x - reach, y)
        cardinal['north'] = (x, y - reach)
        cardinal['east'] = (x + reach, y)
        cardinal['south'] = (x, y + reach)
        for key in cardinal:
            if cardinal[key] in self.maze:
                if self.maze[cardinal[key]] == 0:
                    yield cardinal[key]

    def diagonal(self, current):
        """Yield the diagonal squares"""
        x, y = current
        cardinal = {}
        cardinal['north_west'] = (x - 1, y - 1)
        cardinal['north_east'] = (x + 1, y - 1)
        cardinal['south_east'] = (x + 1, y + 1)
        cardinal['south_west'] = (x - 1, y + 1)
        for key in cardinal:
            if cardinal[key] in self.maze:
                if self.maze[cardinal[key]] == 0:
                    yield cardinal[key]

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
            if list(self.available(coord, 2)):
                return coord
        return None

    def check_odd(self, number):
        """Check if number is a odd number"""
        if not number % 2:
            number += 1
            return number
        elif number == 1:
            number += 2
            return number
        else:
            return number

    def gen(self, width, height, seed = None):
        """Generate the maze"""
        width = self.check_odd(width)
        height = self.check_odd(height)
        if seed:
            random.seed(seed)
        for y in range(height):
            for x in range(width):
                self.maze[(x, y)] = 0
        start = (random.randrange(1, width - 1, 2),
                 random.randrange(1, height - 1, 2))
        end = None
        current = start
        while current:
            area = list(self.available(current, 1))
            area += list(self.diagonal(current))
            squares = list(self.available(current, 2))
            if self.maze[current] != ' ':
                self.maze[current] = ' '
            for coord in area:
                self.maze[coord] = '#'
            if squares:
                choosen = squares.pop(random.randint(0, len(squares) - 1))
                doorway = self.opening(current, choosen)
                self.maze[doorway] = ' '
                current = choosen
            else:
                if not end:
                    end = current
                current = self.pathfinder()
        self.maze[start] = 's'
        self.maze[end] = 'e'
        maze = self.maze.copy()
        self.maze.clear()
        return Maze(width, height, maze, seed)
