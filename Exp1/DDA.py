import matplotlib.pyplot as plt
def DDA(x1,y1,x2,y2):
    dy=y2-y1
    dx=x2-x1
    m=dy/dx
    x=x1
    y=y1
    X=[]
    Y=[]
    while(x<=x2 or y<=y2):
        if(m<1):
            x=x1+1
            y=y1+m
        if(m>1):
            y=y1+1
            x=x1+1/m
        if(m==1):
            x=x1+1
            y=y1+1
        print(x,y)
        X.append(x)
        Y.append(y)
        x1=x
        y1=y
        
    plt.scatter(X,Y)
    plt.show()
DDA(1,2,6,4)
