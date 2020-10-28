#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request
from mazer import Mazer


app = Flask(__name__)
app.debug = True
mazer = Mazer()


@app.route('/', methods=['GET', 'POST'])
def index():
    width = request.args.get('width')
    height = request.args.get('height')
    maze = mazer.gen(31, 31)
    maze.set_square(10)
    if width and height:
        if width.isdigit() and height.isdigit():
            maze = mazer.gen(int(width), int(height))
            maze.set_square(10)
    return render_template('index.html', square_x = maze.square_x,
                           square_y = maze.square_y, width = maze.width,
                           height = maze.height, maze = maze.maze)


if __name__ == '__main__':
    app.run()
