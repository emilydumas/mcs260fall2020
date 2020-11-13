"""
Demonstration of making simple APIs with Flask
MCS 260 Fall 2020 Lecture 35
"""

import flask
import random

# Create a new Flask application that will listen for
# HTTP requests.
app = flask.Flask("Erlenmeyer")

# Make it so that this function is called
# when HTTP request "GET /" is received
@app.route("/")
def hello():
    """
    Return a simple HTML document displaying "Hello World"
    """
    return "<!doctype html><html><body><h1>Hello World</h1></body></html>"

@app.route("/forbidden")
def beans():
    """
    Return 403 status code and a message
    """
    return "That's not allowed", 403

@app.route("/tea")
def short_stout():
    """
    Return 418 I'm a Teapot
    """
    return "I am short and stout", 418

metal_data = [
    { "name": "copper",
      "atomic_number": 29,
      "ferromagnetic": False },
    { "name": "aluminium",
      "atomic_number": 13,
      "ferromagnetic": False },
    { "name": "gold",
      "atomic_number": 79,
      "ferromagnetic": False },
    { "name": "iron",
      "atomic_number": 26,
      "ferromagnetic": True },
    { "name": "nickel",
      "atomic_number": 28,
      "ferromagnetic": True },
]

@app.route("/metal/random")
def thats_so_metal():
    """Choose a metal at random and return as JSON"""
    # Select one of the metals at random
    m = random.choice(metal_data)
    return flask.jsonify(m)

appledata = [
    {
        "name": "McIntosh",
        "stars": 5
    },
    {
        "name": "Honeycrisp",
        "stars": 3
    },
    {
        "name": "Red Delicious",
        "stars": -10
    },
]

@app.route("/apple/random")
def stanley():
    """Choose an apple variety and return JSON data about it"""
    # Select one item from appledata, at random
    a = random.choice(appledata)
    # Return the object a as a JSON HTTP reply
    return flask.jsonify(a)

# This function call is not expected to return
# because it starts the main loop that waits for
# incoming HTTP requests
app.run(port=3000)

# 127.0.0.1 is an IP address that always refers to 
# the localhost, using the loopback network interface
