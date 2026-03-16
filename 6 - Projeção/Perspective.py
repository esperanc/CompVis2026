def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    perspective(atan(height/2/800), 
        width/height, 750, 800*10)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)

