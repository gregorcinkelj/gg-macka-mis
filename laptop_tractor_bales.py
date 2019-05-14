#!/usr/bin/env python

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

# narises tractor-blue.png trailer-blue.png

window = pyglet.window.Window()
window.width = 640
window.height = 640
tracktor = pyglet.resource.image('pic/tractor-blue.png')
bale = pyglet.resource.image('pic/trailer-blue.png')

tracktor.width = 200
tracktor.height = 100
bale.width = 100
bale.height = 100

tracktor_x = 0
tracktor_y = 0
bale_x = 50
bale_y = 1000  # 1000, to je enako window.height - bale.height  == 1100-100 == 1000
# TODO scoreboard

@window.event
def on_draw():
  # tu se vse slike narisejo
    window.clear()
    tracktor.blit(tracktor_x + 0, tracktor_y + 0)
    bale.blit(bale_x + 0, bale_y + 0)
    #dbg_izpisi_stanje()

@window.event
def on_key_press(symbol, modifiers):
    global tracktor_x
    global tracktor_y
    global bale_x
    global bale_y


#pyglet.clock.schedule_interval(update_frames,1/1.0)
pyglet.app.run()
