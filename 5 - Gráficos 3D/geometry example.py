def setup():
    createCanvas(800,800, WEBGL)
    
    beginGeometry()
    sphere(200)
    geom = endGeometry()
    
    background(200)
    translate (-200,0,0); model(geom)
    translate (400,0,0);  model(geom)
    
    freeGeometry(geom)
