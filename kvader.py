#!/usr/bin/env python

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
macka0 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka1 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka2 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka3 = pyglet.resource.image('pic/gingerkitten-small.jpg')
macka3.width = 50
macka3.height = 50
mis = pyglet.resource.image('pic/mouse-small.jpg')
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

macka_x = 0
macka_y = 0
macka1_x = 50
macka1_y = 0

@window.event
def on_draw():
  # tu se vse slike narisejo
    window.clear()
    print "macka x,y = %d,%d" % (macka_x, macka_y)
    macka0.blit(macka_x+0, macka_y+0)
    macka1.blit(macka1_x, macka1_y )
    macka2.blit(100, 0)
    macka3.blit(150, 0)
    # todo - premakni macka0, na njeno mesto macka1
    # todo - premakni macka0, na njeno mesto macka1, na mesto macke1 gre macka2, itd
    # todo - (kaj je for zanka?)
    mis.blit(400, 300)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    global macka_x
    global macka_y
    global macka1_x
    global macka1_y
    print('A key was pressed')
    if symbol == key.LEFT:
        print('  key left')
        macka_x -= 50
        macka1_x -= 50
    elif symbol == key.RIGHT:
        macka_x += 50
        macka1_x += 50
    elif symbol == key.UP:
        macka_y += 50
    elif symbol == key.DOWN:
        macka_y -= 50

pyglet.app.run()
