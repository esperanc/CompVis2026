joints = [[100,50],[100,-20],[100,90]]

def setup():
    createCanvas(600, 600)
    angleMode (DEGREES)
    create_ui()

def draw_joints (joints):
    for s_slider,a_slider in zip(s,a):
        sz,ang = s_slider.value(),a_slider.value()
        rotate(ang)
        rect(0,-5,sz,10)
        translate(sz,0)
    
def draw():
    background(220)
    fill (255,50)
    translate(width/2,height/2)
    draw_joints(joints)
    
def create_ui():
    global s, a
    s,a = [],[]
    for i,[sz,ang] in enumerate(joints):
        s_slider = createSlider(10,200,1)
        s_slider.position(20,20*(i+1))
        s_slider.value(sz)
        s.append(s_slider)
        a_slider = createSlider(-180,180,1)
        a_slider.position(200,20*(i+1))
        a_slider.value(ang)
        a.append(a_slider)
        
