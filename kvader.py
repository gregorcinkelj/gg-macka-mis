#!/usr/bin/env python

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
macka = pyglet.resource.image('pic/gingerkitten-small.jpg')
mis = pyglet.resource.image('pic/mouse-small.jpg')
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    macka.blit(0,0)
    mis.blit(400, 300)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    if symbol == key.LEFT:
        print('  key left')
    elif symbol == key.RIGHT:
        pass
    elif symbol == key.UP:
        pass
    elif symbol == key.DOWN:
        pass

pyglet.app.run()
