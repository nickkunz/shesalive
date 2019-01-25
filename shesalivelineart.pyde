# environment
def setup():
    size(800, 500)
    background(255)
    stroke(0)
    strokeWeight(1)
    noFill()
# general axis references (not used for curve control points)
    alist = [0, 100, 200, 300, 400, 500, 600, 700, 800]
    
    # right eyebrow
    strokeWeight(2)
    curve(0, 400, alist[4], alist[2], alist[5], alist[1]+85, 500, 200)
    
    # left eyebrow
    strokeWeight(2)
    curve(565, 290, alist[3]+60, alist[2]+03, alist[3], alist[2]+05, 310, 210)
# nose
    strokeWeight(1)
    curve(445, 0, alist[3]+72, alist[2]+60, alist[4], alist[2]+80, 300, 318)
# silhouette
    strokeWeight(1)
    curve(390, 300, alist[3]+70, alist[3]+30, alist[4]+35, alist[3]+30, 640, 130)
    curve(350, -95, alist[2]+95, alist[1]+95, alist[3]+70, alist[3]+30, 400, 350)
    curve(340, 410, alist[4]+35, alist[3]+30, alist[4]+90, alist[2]+70, 590, 150)
    curve(340, 410, alist[4]+90, alist[2]+70, alist[5]+10, alist[1]+70, 495, 150)
# hair
    strokeWeight(1)
    curve(-900, 390, alist[3]+85, alist[0]+90, alist[5], alist[4]+50, 600, 600)
    curve(-500, 405, alist[3]+85, alist[0]+95, alist[5]+05, alist[4]+50, 600, 600)
    curve(-1300, 405, alist[3]+85, alist[0]+85, alist[5]+35, alist[4]+50, 1000, 600)
    curve(-800, 405, alist[3]+89, alist[0]+80, alist[5]+50, alist[4]+10, 400, 400)
    curve(1200, 390, alist[3]+70, alist[0]+90, alist[3], alist[4]+25, 600, 600)
    curve(800, 390, alist[3]+70, alist[0]+95, alist[2]+50, alist[4], 300, 600)
    curve(1200, 390, alist[3]+70, alist[0]+85, alist[3], alist[4]+40, 50, 600)
# neck
    strokeWeight(1)
    curve(250, 300, alist[3]+48, alist[3]+05, alist[3]+65, alist[4], 300, 425)
    curve(500, 305, alist[4]+60, alist[3]+05, alist[4]+60, alist[4], 500, 550)
   
    # mouth
    strokeWeight(1)
    curve(370, 310, alist[3]+65, alist[3]+05, alist[4]+25, alist[2]+97, 600, 160)
    curve(370, 310, alist[3]+65, alist[3]+05, alist[4]+25, alist[2]+97, 600, 230)
    
    # eyeball right
    strokeWeight(1)
    curve(400, 200, alist[4]+9, alist[2]+19, alist[4]+87, alist[2]+12, 700, 90)
        
    # eyeball left
    strokeWeight(1)
    curve(360, 220, alist[3]+60, alist[2]+20, alist[3]+10, alist[2]+18, 190, 125)
    
# movement    
def draw():
# mouth axis references (mouth movement only, used for curve control points)
    mlist = [370, 310, 365, 305, 425, 297, 600, 100]
    if  mouseX >= mlist[2]-20 and mouseX <= mlist[4]+20 and mouseY >= mlist[5]-40 and mouseY <= mlist[3]+40:
        stroke(0)
        strokeWeight(0)
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]) 
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]-150)
        
        stroke(255)
        strokeWeight(0)
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]-100)
    
    else:
        stroke(255)
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7])
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]-150)
        
        stroke(0)
        strokeWeight(0)
        curve(mlist[0], mlist[1], mlist[2], mlist[3], mlist[4], mlist[5], mlist[6], mlist[7]-100)
# eye movement axis reference (not used for curve control points in curve, eye movement only)
    elist = [0, 100, 200, 300, 400, 500]
    if  mouseY > elist[2]:
        # eyeball right
        stroke(235)
        strokeWeight(2)
        curve(200, 410, elist[4]+9, elist[2]+19, elist[4]+87, elist[2]+12, 492, 200)
        
        # eyeball left
        stroke(235)
        strokeWeight(2)
        curve(515, 300, elist[3]+60, elist[2]+20, elist[3]+10, elist[2]+18, 350, 210)
    else:
        # right eyeball
        stroke(0)
        strokeWeight(1.5)
        curve(200, 410, elist[4]+9, elist[2]+19, elist[4]+87, elist[2]+12, 492, 200)
        
        # left eyeball
        stroke(0)
        strokeWeight(1.5)
        curve(515, 300, elist[3]+60, elist[2]+20, elist[3]+10, elist[2]+18, 350, 210)
