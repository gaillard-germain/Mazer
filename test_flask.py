#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request
from mazer import Mazer


app = Flask(__name__)
app.debug = True
mazer = Mazer()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        width = request.args.get('width', '31')
        height = request.args.get('height', '31')
        maze = mazer.gen(int(width), int(height))
        maze.set_square(10)
    return render_template('index.html', square_x = maze.square_x,
                           square_y = maze.square_y, maze_width = maze.width,
                           maze_height = maze.height, maze = maze.maze)


if __name__ == '__main__':
    app.run()
