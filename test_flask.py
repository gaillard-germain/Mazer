#! /usr/bin/python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template, url_for, request
from mazer import Mazer


app = Flask(__name__)
app.debug = True
mazer = Mazer()


@app.route('/', methods=['GET', 'POST'])
def index():
    lines = []
    width = request.args.get('width')
    height = request.args.get('height')
    if width and height:
        if width.isdigit() and height.isdigit():
            maze = mazer.gen(int(width), int(height))
            line = []
            for coord, value in maze.maze.items():
                line.append(str(value))
                if coord[0] / maze.square_size == maze.width - 1:
                    lines.append(line)
                    line = []
    return render_template('index.html', lines = lines)


if __name__ == '__main__':
    app.run()
