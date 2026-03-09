def setup():
    createCanvas(600, 600, WEBGL)

def draw():
    background(220)
    rotateX(radians(frameCount))
    box(400,400,50)
