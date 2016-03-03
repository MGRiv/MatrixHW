import math

def make_translate( x, y, z ):
    m = new_matrix()
    m = ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m

def make_scale( x, y, z ):
    m = new_matrix()
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    m[3][3] = 1
    return m
    
def make_rotX( theta ):   
    m = new_matrix()
    m[0][0] = 1
    m[1][1] = math.cos(theta)
    m[1][2] = math.sin(theta)
    m[2][1] = -1 * math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    return m

def make_rotY( theta ):
    m = new_matrix()
    m[0][0] = math.cos(theta)
    m[1][1] = 1
    m[0][2] = math.sin(theta)
    m[2][0] = -1 * math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    return m

def make_rotZ( theta ):
    m = new_matrix()
    m[0][0] = math.cos(theta)
    m[0][1] = math.sin(theta)
    m[1][0] = -1 * math.sin(theta)
    m[1][1] = math.cos(theta)
    m[2][2] = 1
    m[3][3] = 1
    return m


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ""
    row = len(matrix[0])
    col = len(matirx)
    for r in range(row):
        for c in range(col):
            s += str(matrix[c][r]) + " "
        s += "\n"
    print s

def ident( matrix ):
    for c in range(4):
        for r in range(4):
            if(r != c ):
                matrix[c][r] = 0
            else:
                matrix[c][r] = 1
    return matrix

def scalar_mult( matrix, x ):
    for c in range(4):
        for r in range(4):
            matrix[c][r] = matrix[c][r] * x
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    l = len(m2)
    c = 0
    while(c < l):
        sx = sy = sz = sn = 0
        for r in range (4):
            sx += (m2[c][r] * m1[r][0])
            sy += (m2[c][r] * m1[r][1])
            sz += (m2[c][r] * m1[r][2])
            sn += (m2[c][r] * m1[r][3])
        m2[c][0] = sx
        m2[c][1] = sy
        m2[c][2] = sz
        m2[c][3] = sn
        c += 1
