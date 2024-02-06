#!/usr/bin/env python3
"""
flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet() -> str:
    """ index
    """
    return render_template('0-index.html')
