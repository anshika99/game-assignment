def setup():
    size(500,500)
    background(255)
    
    global x,y,xSpeed, ySpeed, col, colChange
    x = 100
    y = 100 
    xSpeed = 2
    ySpeed = 1
    col = 50
    colChange = 2
def draw(): 
    global x,y,xSpeed, ySpeed, col, colChange
    x = x+xSpeed
    y = y+ySpeed
    col = col + colChange
    
    if x < 0 or x > width:
        xSpeed = xSpeed * -1
        colChange = colChange * -1
    if y < 0 or y >height:
        ySpeed = ySpeed * -1
    fill(0, col, 0)
    ellipse(x,y,16,16)
