#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# test.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

from mazer import Mazer


def command():
    print("\nEnter solve to see the path to the exit")
    print("Enter save to save the maze in a .txt file")
    print("Enter gen to generate an other one")
    print("Enter quit to quit\n")
    return input(">>> ").lower()


def main():
    mazer = Mazer()
    com = 'gen'
    saved = False
    print("Welcome to Mazer a random maze generator")
    print("! width and height must be odd numbers !\n")

    while True:
        if com == 'quit':
            break
        elif com == 'gen':
            x = input("Enter maze width (31): ")
            y = input("Enter maze height (31): ")
            seed = input("Enter a seed (optional) : ")
            maze = mazer.gen(x, y, seed)
            maze.show()
            saved = False
            com = command()
        elif com == 'solve':
            maze.solve()
            maze.show()
            com = command()
        elif com == 'save':
            if saved:
                print("\nmaze already saved !\n")
            else:
                maze.export_txt()
                saved = True
                print("\nMaze saved as maze.txt")
            com = command()
        else:
            print("\nWrong entry ! Please enter one of the command below:")
            com = command()


if __name__ == "__main__":
    main()
