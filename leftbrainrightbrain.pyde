def setup():
    size(500,500)
    background(255)
    print random(10,10)
    
def draw():
    w = random(width/2,width)
    x = random(0,width/2)
    y = random(0,height)
    size = random(100)
    colorA = random(255)
    colorB = random(255)
    colorC = random(255)
 
    noStroke()
    fill(random(255))
    rect(x,y,size,size)
    
    noStroke()
    fill(colorA,colorB,colorC)
    ellipse(w,y,size,size)
