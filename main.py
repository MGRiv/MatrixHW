from display import *
from draw import *
import math

screen = new_screen()
colorg = [ 0, 255, 0 ]
colorr = [255,0,0]
colorb = [0,0,225]

m1 = []
add_edge(m1,0,0,1,0,1,0)
add_edge(m1,0,1,0,1,0,0)
add_edge(m1,1,0,0,0,0,1)
draw_lines(m1,screen,colorb)
for s in range(69):
    sc = make_scale(1.1,1.1,1.1)
    matrix_mult(sc,m1)
    draw_lines(m1,screen,colorb)

m = []
add_edge(m,0,0,0,100,0,0)
add_edge(m,0,0,0,0,100,0)
add_edge(m,0,0,0,0,0,100)
draw_lines(m,screen,colorr)
t = make_translate(100,0,0)
tp = make_translate(-100,0,0)
matrix_mult(t,m)
draw_lines(m,screen,colorr)
matrix_mult(tp,m)
t = make_translate(0,100,0)
tp = make_translate(0,-100,0)
matrix_mult(t,m)
draw_lines(m,screen,colorr)
matrix_mult(tp,m)
t = make_translate(0,0,100)
tp = make_translate(0,0,-100)
matrix_mult(t,m)
draw_lines(m,screen,colorr)

m3 = []
add_edge(m,0,0,0,300,0,0)
add_edge(m,0,0,0,0,300,0)
add_edge(m,0,0,0,0,0,300)
draw_lines(m,screen,colorr)

m2 = []
rad1 = []
rad2 = []
rad3 = []
add_edge(rad1,100,0,0,100,1,0)
add_edge(rad2,0,100,0,0,100,1)
add_edge(rad3,0,0,100,1,0,100)

rotz = make_rotZ(math.pi / 180)
rotx = make_rotX(math.pi / 180)
roty = make_rotY(math.pi / 180)

for r in range(360):
    matrix_mult(rotz,rad1)
    matrix_mult(rotx,rad2)
    matrix_mult(roty,rad3)
    draw_lines(rad1,screen,colorg)
    draw_lines(rad2,screen,colorg)
    draw_lines(rad3,screen,colorg)




display(screen)
