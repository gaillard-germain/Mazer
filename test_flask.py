#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request
from mazer import Mazer


app = Flask(__name__)
mazer = Mazer()

@app.route('/', methods = ['GET', 'POST'])
def maze_gen():
    if request.method == 'GET':
        seed = request.args.get('seed', 'Mazer')
        width = request.args.get('width', '31')
        height = request.args.get('height', '31')
        maze = mazer.gen(int(width), int(height), seed)
        maze.set_square(10)
        maze.solve()
        return render_template('index.html', maze = maze, seed = seed)


if __name__ == '__main__':
    app.run(debug = True)
