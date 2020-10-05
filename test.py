#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# test.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

from mazer import Mazer


def main():
    mazer = Mazer()
    com = ' '
    print("Welcome to Mazer a random maze generator")
    print("! width and height must be odd !")
    while com != 'q':
        x = input("\nEnter the maze width : ")
        y = input("Enter the maze height : ")
        print("\nGenerating maze...\n")

        maze = mazer.gen(int(x), int(y))
        maze.show()
        print("\nPress RETURN to generate an other one")
        print("Enter Q to quit\n")
        com = input(">>> ").lower()


if __name__ == "__main__":
    main()
