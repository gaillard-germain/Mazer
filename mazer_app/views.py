#! /usr/bin/python3
# -*- coding:utf-8 -*-

# views.py
# Author: Germain GAILLARD <gaillard.germain@gmail.com>
# Version: 0.1
# License: MIT

from flask import Flask, render_template, request, jsonify
from mazer_app import Mazer

app = Flask(__name__)

mazer = Mazer()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen', methods=['POST'])
def gen():
    seed = request.form['seed']
    width = request.form['width']
    height = request.form['height']
    size = request.form['size']
    maze = mazer.gen(int(width), int(height), seed)
    maze.solve()
    maze.set_square(int(size))
    return maze.get_svg_tag()
