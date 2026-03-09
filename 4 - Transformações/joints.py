joints = [[100,50],[100,-20],[100,90]]

def setup():
    createCanvas(600, 600)
    angleMode (DEGREES)

def draw_joints (joints):
    for sz,ang in joints:
        rotate(ang)
        rect(0,-5,sz,10)
        translate(sz,0)
    
def draw():
    background(220)
    fill (255,50)
    translate(width/2,height/2)
    draw_joints(joints)
