from display import *
from matrix import *
import math


def draw_lines( matrix, screen, color ):
    l = len(matrix)
    c = 0
    while(l - c > 1):
        p = matrix[c]
        e = matrix[c + 1]
        draw_line(screen,int((p[0] - p[2]) * math.sqrt(3)/2),int(p[1] - .5 * (p[0] + p[2])),int((e[0] - e[2]) * math.sqrt(3)/2),int(e[1] - .5 * (e[0] + e[2])),color)
        c += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    d1 = []
    d1.append(x0)
    d1.append(y0)
    d1.append(z0)
    d1.append(1)
    matrix.append(d1)
    d2 = []
    d2.append(x1)
    d2.append(y1)
    d2.append(z1)
    d2.append(1)
    matrix.append(d2)

m1 = []
add_edge( m1 , 2 , 1 , 0 , 3 , 4 , 0)
print_matrix(m1)
scalar_mult(m1,3)
print_matrix(m1)


def add_point( matrix, x, y, z=0 ):
    d = []
    d.append(x)
    d.append(y)
    d.append(z)
    d.append(1)
    matrix.append(d)

def draw_line( screen, x0, y0, x1, y1, color ):
    if(x0 > x1):
        draw_line(screen,x1,y1,x0,y0,color)
    else:
        a = y1 - y0
        b = x0 - x1
        if(a > 0):
            if(a > (b*-1)):
                #2nd
                d = a + 2*b
                a *= 2
                b *= 2
                while(y0 <= y1):
                    plot(screen,color,x0,y0)
                    if(d < 0):
                        x0 += 1
                        d += a
                    y0 += 1
                    d += b
            else:
                #1st
                d = b + 2*a
                a *= 2
                b *= 2
                while(x0 <= x1):
                    plot(screen,color,x0,y0)
                    if(d > 0):
                        y0 += 1
                        d += b
                    x0 += 1
                    d += a
        else:
            if((a*-1) > (b*-1)):
                #7th
                d = a - 2*b
                a *= 2
                b *= 2
                while(y0 >= y1):
                    plot(screen,color,x0,y0)
                    if(d > 0):
                        x0 += 1
                        d += a
                    y0 -= 1
                    d -= b
            else:
                #8th
                d = 2*a - b
                a *= 2
                b *= 2
                while(x0 <= x1):
                    plot(screen,color,x0,y0)
                    if(d < 0):
                        y0 -= 1
                        d -= b
                    x0 += 1
                    d += a
