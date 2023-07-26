import matplotlib.pyplot as plt
def MLD(x1,y1,x2,y2):
    dy=y2-y1
    dx=x2-x1
    d=2*dy-dx
    dd =2*dy-2*dx
    x=x1
    y=y1
    X=[]
    Y=[]
    while(x<=x2 or y<=y2):
        if(d<0):
            x=x1+1
            y=y1
            d=d+2*dy
        if(d>=0):
            y=y1+1
            x=x1+1
            d=d+dd
        print(x,y,d)
        X.append(x)
        Y.append(y)
        x1=x
        y1=y
        
    plt.scatter(X,Y)
    plt.show()
MLD(20,10,30,18)
