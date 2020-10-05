#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# maze.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

import random


class Maze:
    """A randomly generated maze"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = {}
        for y in range(self.height):
            for x in range(self.width):
                self.maze[(x, y)] = 0
        self.walls = []
        self.corridors = []
        self.start = (1, 1)
        self.end = None
        self.gen()

    def available(self, current, reach):
        """Yield the reachables squares"""
        x, y = current
        west = (x - reach, y)
        north = (x, y - reach)
        east = (x + reach, y)
        south = (x, y + reach)
        if west in self.maze:
            if self.maze[west] == 0:
                yield west
        if north in self.maze:
            if self.maze[north] == 0:
                yield north
        if east in self.maze:
            if self.maze[east] == 0:
                yield east
        if south in self.maze:
            if self.maze[south] == 0:
                yield south

    def diagonal(self, current):
        """Yield the diagonal squares"""
        x, y = current
        north_west = (x - 1, y - 1)
        north_east = (x + 1, y - 1)
        south_east = (x + 1, y + 1)
        south_west = (x - 1, y + 1)
        if north_west in self.maze:
            if self.maze[north_west] == 0:
                yield north_west
        if north_east in self.maze:
            if self.maze[north_east] == 0:
                yield north_east
        if south_east in self.maze:
            if self.maze[south_east] == 0:
                yield south_east
        if south_west in self.maze:
            if self.maze[south_west] == 0:
                yield south_west

    def opening(self, current, choosen):
        """Return the square between two others"""
        x, y = current
        a, b = choosen
        return ((x + a) / 2, (y + b) / 2)

    def pathfinder(self):
        """Return the last openable wall"""
        self.corridors.reverse()
        for coord in self.corridors:
            if list(self.available(coord, 2)):
                self.corridors.reverse()
                return coord
        self.corridors.reverse()
        return None

    def gen(self):
        """Generate the maze"""
        current = self.start
        while current:
            area = list(self.available(current, 1))
            area += list(self.diagonal(current))
            squares = list(self.available(current, 2))
            if self.maze[current] != ' ':
                self.maze[current] = ' '
                self.corridors.append(current)
            for coord in area:
                self.maze[coord] = 'w'
                self.walls.append(coord)
            if squares:
                choosen = squares.pop(random.randint(0, len(squares) - 1))
                doorway = self.opening(current, choosen)
                self.maze[doorway] = ' '
                self.corridors.append(doorway)
                self.walls.remove(doorway)
                current = choosen
            else:
                if not self.end:
                    self.end = current
                current = self.pathfinder()
        self.maze[self.start] = 's'
        self.maze[self.end] = 'e'

    def show(self):
        """Display the maze in the console"""
        line = ''
        for coord, value in self.maze.items():
            line += str(value)
            if coord[0] == self.width - 1:
                print(line)
                line = ''
        print('     ')


if __name__ == "__main__":
    maze = Maze(45, 19)
    maze.show()
