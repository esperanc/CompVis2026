"""
Interactive demonstration of Bézier Curves.
Drag control points to adjust curve.
Click and drag to add another control point (and increase curve degree).
Hit delete key to delete selected control point.
"""

from math import comb, pow

def bernstein(n,k,t):
    return comb(n,k)*pow(t,k)*pow(1-t,n-k)
    
def setup():
    global pts, selected
    create_canvas(windowWidth, windowHeight)
    w,h = width,height
    pts = [[w*0.2,h*0.8],
           [w*0.4,h*0.2],
           [w*0.6,h*0.2],
           [w*0.8,h*0.8]]
    selected = None

def mouse_pressed():
    global selected, pts, moved, new_point
    selected = None
    new_point = False
    if mouse_button != LEFT: return
    moved = False
    for p in pts:
        x, y = p
        if dist(x,y,mouse_x, mouse_y) < 10:
            selected = p
    if not selected:
        new_point = True
        j = -1
        min_d = 1e10
        p = [mouse_x, mouse_y]
        n = len(pts)
        #k = n+1 if gui.closed else n
        k = n
        for i in range (1,k):
            d = dist_segment (p, pts[i-1], pts[i%n])
            if d < min_d:
                min_d = d
                j = i
        pts = pts[:j] + [p] + pts[j:]
        selected = pts[j]


def key_pressed():
    if key in ["D","d", "X","x", "Delete"] and selected:
        pts.remove(selected)
        
def mouse_dragged():
    global selected, moved
    if selected:
        moved = True
        p = selected
        p[0]+=mouse_x-pmouse_x
        p[1]+=mouse_y-pmouse_y

def dist_segment (p, a, b):
    p = create_vector (*p)
    a = create_vector (*a)
    b = create_vector (*b)
    v = b.copy().sub(a)
    u = p.copy().sub(a)
    vlen = v.mag()
    vnorm = v.copy().normalize()
    proj_size = vnorm.dot(u)
    if proj_size > vlen: return p.dist(b)
    if proj_size < 0: return p.dist(a)
    return p.sub(a.lerp(b, proj_size / vlen)).mag()
    
def draw():
    background(245)
    global pts
    
    push()
    fill('white')
    stroke_weight(2)
    n = len(pts)-1
    begin_shape()
    for i in range(100):
        t = i / 99
        p = createVector(0,0)
        for k in range(n+1):
            poly = bernstein(n,k,t)
            v = createVector (poly*pts[k][0], poly*pts[k][1])
            p.add(v)
        vertex(p.x,p.y)
    end_shape()
    pop()
    
    push()
    stroke_weight(1)
    no_fill()
    drawingContext.setLineDash([2, 5]);
    begin_shape()
    for x,y in pts: vertex(x,y)
    end_shape()
    pop()
    
    for p in pts:
        if p == selected: fill('red')
        else: fill('white')
        circle (*p, 10, 10)
        

    
    
    
