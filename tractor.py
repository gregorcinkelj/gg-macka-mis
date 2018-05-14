#!/usr/bin/env python3

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

# narises tractor-blue.png trailer-blue.png

window = pyglet.window.Window()
window.width = 1200
window.height = 900
tracktor = pyglet.resource.image('pic/tractor-blue.png')
trailer = pyglet.resource.image('pic/trailer-blue.png')

# tracktor.width = 678
# tracktor.height = 455
trailer.width = 250
trailer.height = 250

tracktor_x = 0
tracktor_y = 0
trailer_x = 50
trailer_y = 0

@window.event
def on_draw():
  # tu se vse slike narisejo
    window.clear()
    tracktor.blit(tracktor_x + 0, tracktor_y + 0)
    #dbg_izpisi_stanje()

@window.event
def on_key_press(symbol, modifiers):
    global tracktor_x
    global tracktor_y
    global trailer_x
    global trailer_y


#pyglet.clock.schedule_interval(update_frames,1/1.0)
pyglet.app.run()
