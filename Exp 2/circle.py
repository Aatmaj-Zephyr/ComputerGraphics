import matplotlib.pyplot as plt
X=[]
Y=[]

def drawcircle(cx,cy,x,y):
   X.append(cx+x)
   Y.append(cy+y)

   X.append(cx-x)
   Y.append(cy+y)
   
   X.append(cx+x)
   Y.append(cy-y)
   
   X.append(cx-x)
   Y.append(cy-y)
   
   X.append(cx+y)
   Y.append(cy+x)
   
   X.append(cx-y)
   Y.append(cy+x)

   X.append(cx+y)
   Y.append(cy-x)

   X.append(cx-y)
   Y.append(cy-x)
   
import math
def draw(cx,cy,r):
   x=0
   y=r
  
   d=3-(2*r)
   drawcircle(cx,cy,x,y)
   while(x<=y):
        x=x+1
        if(d<0):
            d = d + (4*x) + 6
        else:
            d = d + 4 * (x - y) + 10
            y=y-1
        drawcircle(cx,cy,x,y)


draw(50,50,30)

plt.scatter(X,Y)
plt.show()
