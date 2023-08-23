x1= 7
y1= 9
x2= 11
y2= 4
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

def laingBaserkey(x1,y1,x2,y2,x_max,y_max,x_min,y_min):
    dx=x2-x1 
    dy=y2-y1
    p1 = -dx
    p2 = dx
    p3 = -dy
    p4 = dy
    q1 = x1 - x_min
    q2 = x_max - x1
    q3 = y1 - y_min
    q4 = y_max - y1
    if(p1==0):
        return("parallel line")
    if(p3==0):
        return("parallel line")
    #If p1 < 0 and p3 < 0, or if p2 < 0 and p4 < 0, the line lies completely outside the clipping window. In this case, the algorithm terminates.
    if((p1 < 0 and p3 < 0) or (p2 < 0 and p4 < 0)):
        return("out of window")
    tin = max(q1 / p1 ,q3 / p3, 0)

    tout = min(q2 / p2 ,q4 / p4, 1)

    answer=[]
    if(tin>tout):
        return("Invisible line case 2")
    x= x1+tin*dx
    y= y1+tin*dy
     
    answer.append((x,y))
    x= x1+tout*dx
    y= y1+tout*dy
    
    answer.append((x,y))
    return("Clipped",answer)

print(laingBaserkey(x1,y1,x2,y2,x_max,y_max,x_min,y_min))
