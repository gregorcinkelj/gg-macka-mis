#!/bin/bash

# https://www.eastcottvets.co.uk/uploads/Animals/gingerkitten.jpg
convert pic/gingerkitten-orig.jpg -trim -resize 170x113 pic/gingerkitten-small.jpg

# https://www.criver.com/sites/default/files/2017-10/129-Mouse_417x235.jpg
convert pic/mouse-orig.jpg -trim -resize 208x118 pic/mouse-small.jpg

#convert pic/prikolica-1.png -trim +repage -fuzz 1% -transparent black pic/prikolica-1-small.png
convert pic/prikolica-1.png -trim +repage pic/prikolica-1-small.png
convert pic/tractor-1.png -trim +repage pic/tractor-1-small.png
