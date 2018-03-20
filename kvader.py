#!/usr/bin/env python

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
macka = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka1 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka2 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka3 = pyglet.resource.image('pic/gingerkitten-small.jpg')
mis = pyglet.resource.image('pic/mouse-small.jpg')
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

macka_x = 0
macka_y = 0

@window.event
def on_draw():
    window.clear()
    macka.blit(macka_x, macka_y)
    macka1.blit(0, 0)
    # todo
    mis.blit(400, 300)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    global macka_x
    global macka_y
    print('A key was pressed')
    if symbol == key.LEFT:
        print('  key left')
        macka_x -= 20
    elif symbol == key.RIGHT:
        macka_x += 20
    elif symbol == key.UP:
        macka_y += 20
    elif symbol == key.DOWN:
        macka_y -= 20

pyglet.app.run()
