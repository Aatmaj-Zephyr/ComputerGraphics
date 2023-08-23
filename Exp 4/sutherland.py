x1= 1
y1= 5
x2= 4
y2= 1
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

def cohen_sutherland(x1,y1,x2,y2,x_max,y_max,x_min,y_min):
  a = checkCase(x1,y1,x_max,y_max,x_min,y_min)
  b = checkCase(x2,y2,x_max,y_max,x_min,y_min)

  if(a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]==0):
    return("visible Line")
    pass 
  elif(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]==0):
    m=(y2-y1)/(x2-x1)
    ans=[]
    #line clipped
    if(a[3]+b[3]==1):
      #left boundary of rectangle window
      y=y1+m*(x_min-x1)
      x=x_min
      ans.append((x,y))
      if(y<y_min or y>y_max):
        return("Invisible line case 2")

    if(a[2]+b[2]==1):
      #right boundary of rectangle window
      y=y1+m*(x_max-x1)
      x=x_max
      ans.append((x,y))
      if(y<y_min or y>y_max):
        return("Invisible line case 2")

    if(a[1]+b[1]==1):
      #bottom boundary of rectangle window
       x=x1+(y_min-y1)/m
       y=y_min
       ans.append((x,y))
       if(x<x_min or x>x_max):
        return("Invisible line case 2")

    if(a[0]+b[0]==1):
      #top boundary of rectangle window
      x=x1+(y_max-y1)/m
      y=y_max
      ans.append((x,y))
      if(x<x_min or x>x_max):
        return("Invisible line case 2")

    return("Clipped line ", ans,a,b)
    pass 
  
  return("Invisible line")


  

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

print(cohen_sutherland(x1,y1,x2,y2,x_max,y_max,x_min,y_min))
