#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request
from mazer import Mazer


app = Flask(__name__)
app.debug = True
mazer = Mazer()

@app.route('/mazer')
def maze_gen():
    seed = request.args.get('seed', 'Mazer')
    width = request.args.get('width', '31')
    height = request.args.get('height', '31')
    maze = mazer.gen(int(width), int(height), seed)
    maze.set_square(10)
    return render_template('index.html', maze = maze, seed = seed)


if __name__ == '__main__':
    app.run()
