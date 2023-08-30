#TODO


x1= 1
y1= 6
x2= 15
y2= 11
x_max = 12
y_max = 14
x_min = 4
y_min = 2

def findLine(x1,y1,x2,y2,x_max,y_max,x_min,y_min):
  a = checkCase(x1,y1,x_max,y_max,x_min,y_min)
  b = checkCase(x2,y2,x_max,y_max,x_min,y_min)

  if(a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]==0):
    return(1) #visible
  elif(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]==0):
    return(2) #clipped
  return(0) #invisible


array=[]

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
  midx=(x1+x2)//2
  midy=(y1+y2)//2
  
  print((x1,y1,x2,y2))
  if(x1==midx or x2==midx or y1==midy or y2==midy):
    #end of recursion
    
    return 0

  firstHalf=findLine(x1,y1,midx,midy,x_max,y_max,x_min,y_min)
  if(firstHalf == 2 ):# if half is clipped recurse
    print((x1,y1,midx,midy,x_max,y_max,x_min,y_min))
    mid(x1,y1,midx,midy,x_max,y_max,x_min,y_min) 
  elif(firstHalf == 1 ): # if first half is visible, return the coordinates
     Ax1=x1
     Ay1=y1
     Ax2=midx 
     Ay2=midy
     array.append((Ax1,Ay1,Ax2,Ay2))


  secondHalf=findLine(midx,midy,x2,y2,x_max,y_max,x_min,y_min)
  if(secondHalf == 2 ):# if half is clipped recurse
    print((midx,midy,x2,y2,x_max,y_max,x_min,y_min))
    mid(midx,midy,x2,y2,x_max,y_max,x_min,y_min) 
  elif(secondHalf == 1 ): # if first half is visible, return the coordinates
     
     Ax1=midx 
     Ay1=midy
     Ax2=x2
     Ay2=y2
     array.append((Ax1,Ay1,Ax2,Ay2))



print(mid(x1,y1,x2,y2,x_max,y_max,x_min,y_min))
print(array)

print("final coordinates -- ")
print(min(tup[0] for tup in array),min(tup[1] for tup in array),max(tup[2] for tup in array),min(tup[3] for tup in array))
