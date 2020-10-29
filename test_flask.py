#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request, redirect
from mazer import Mazer


app = Flask(__name__)
app.debug = True
mazer = Mazer()


@app.route('/mazer', methods = ['POST', 'GET'])
def maze_gen():
    if request.method == 'POST':
        width = request.form.get('width')
        height = request.form.get('height')
        maze = mazer.gen(int(width), int(height))
        maze.set_square(10)
        return render_template('gen.html', square_x = maze.square_x,
                                square_y = maze.square_y, maze_width = maze.width,
                                maze_height = maze.height, maze = maze.maze)
    else:
        return render_template('index.html', square_x = 3, square_y = 3)


if __name__ == '__main__':
    app.run()
