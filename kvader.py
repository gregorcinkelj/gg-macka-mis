#!/usr/bin/env python3

# http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
# http://steveasleep.com/pyglettutorial.html

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
macka0 = pyglet.resource.image('pic/gingerkitten-small-0.jpg')
macka1 = pyglet.resource.image('pic/gingerkitten-small-1.jpg')
macka2 = pyglet.resource.image('pic/gingerkitten-small-2.jpg')
macka3 = pyglet.resource.image('pic/gingerkitten-small-3.jpg')
macka0.width = 50
macka0.height = 50
macka1.width = 50
macka1.height = 50
macka2.width = 50
macka2.height = 50
macka3.width = 50
macka3.height = 50
mis = pyglet.resource.image('pic/mouse-small.jpg')
mis.width = 100
mis.height = 50
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

macka0_x = 0
macka0_y = 0
macka1_x = 50
macka1_y = 0
macka2_x = 100
macka2_y = 0
macka3_x = 150
macka3_y = 0

counter = 0.0
smer = key.DOWN

def dbg_izpisi_stanje():
    print("macka 0,1,2,3 (x,y) = (%d,%d) (%d,%d) (%d,%d) (%d,%d) " % (macka0_x, macka0_y, macka1_x, macka1_y, macka2_x, macka2_y, macka3_x, macka3_y))

def update_frames(dt):
    global counter
    counter = counter + dt
    print("counter = %f" % (counter))
    on_key_press(smer, None)


@window.event
def on_draw():
  # tu se vse slike narisejo
    window.clear()
    dbg_izpisi_stanje()
    mis.blit(400, 300)
    macka0.blit(macka0_x+0, macka0_y+0)
    macka1.blit(macka1_x, macka1_y)
    macka2.blit(macka2_x, macka2_y)
    macka3.blit(macka3_x, macka3_y)
    # todo - premakni macka1, na njeno mesto macka0
    # todo - premakni macka1, na njeno mesto macka2, na mesto macke2 gre macka1, itd
    # todo - (kaj je for zanka?)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    global macka0_x
    global macka0_y
    global macka1_x
    global macka1_y
    global macka2_x
    global macka2_y
    global macka3_x
    global macka3_y
    global smer
    print('A key was pressed')
    if symbol == key.LEFT or symbol == key.RIGHT or symbol == key.UP or symbol == key.DOWN:
        print("-----------------------")
        dbg_izpisi_stanje()
        macka3_x = macka2_x
        macka3_y = macka2_y
        dbg_izpisi_stanje()
        macka2_x = macka1_x
        macka2_y = macka1_y
        dbg_izpisi_stanje()
        macka1_x = macka0_x
        macka1_y = macka0_y
        dbg_izpisi_stanje()
        print("-----------------------")
    if symbol == key.LEFT:
        print('  key left')
        macka0_x -= 50
        smer = key.LEFT
    elif symbol == key.RIGHT:
        macka0_x += 50
        smer = key.RIGHT
    elif symbol == key.UP:
        macka0_y += 50
        smer = key.UP
    elif symbol == key.DOWN:
        macka0_y -= 50
        smer = key.DOWN

pyglet.clock.schedule_interval(update_frames,1/1.0)
pyglet.app.run()
