#TODO


x1= 1
y1= 5
x2= 4
y2= 1
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

def findLine(x1,y1,x2,y2,x_max,y_max,x_min,y_min):
  a = checkCase(x1,y1,x_max,y_max,x_min,y_min)
  b = checkCase(x2,y2,x_max,y_max,x_min,y_min)

  if(a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]==0):
    return(1) #visible
  elif(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]==0):
    return(2)
  return(0) #invisible


  

def checkCase(x,y,x_max,y_max,x_min,y_min):
    bit=[0,0,0,0]
    if(x<x_min):
     bit[3]=1
    if(x>x_max):
     bit[2]=1
    if(y<y_min):
     bit[1]=1
    if(y>y_max):
     bit[0]=1
    return bit
def mid(x1,y1,x2,y2,x_max,y_max,x_min,y_min):
  midx=(x1+x2)/2
  midy=(y1+y2)/2
  if(findLine(x1,y1,midx,midy,x_max,y_max,x_min,y_min)!=0):
    mid(x1,y1,midx,midy,x_max,y_max,x_min,y_min) 
  if(findLine(midx,midy,x2,y2,x_max,y_max,x_min,y_min)!=0):
    mid(midx,midy,x2,y2,x_max,y_max,x_min,y_min)
  return(x1,y1)

print(mid(x1,y1,x2,y2,x_max,y_max,x_min,y_min))
