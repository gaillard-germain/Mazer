#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mazer.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

from mazer import Mazer


def main():
    print("Wecome to Mazer a random maze generator")
    print("! width and height must be odd !\n")
    x = input("Enter the maze width : ")
    y = input("Enter the maze height : ")
    print("\nGenerating maze...\n")

    maze = Mazer().gen(int(x), int(y))
    maze.show()


if __name__ == "__main__":
    main()
