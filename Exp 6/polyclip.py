polygon = [(100,150), (200,250), (300,200)]
clipping = [(150,150), (150,200), (200,200), (200,150)] #works only for squares. else edit isin

def isintwo(p1):
    x=p1[0]
    y=p1[1]
    if(x in range(clipping[0][0],clipping[2][0]+1) and y in range(clipping[0][1],clipping[2][1]+1) ):
            return True 
    return False
def isin(p1,case):
    if(case==0):
        #left
        return p1[0]>clipping[0][0]
    if(case==1):
        #top
        return p1[1]<clipping[1][1]
    if(case==2):
        #right
        return p1[0]<clipping[1][1]
    if(case==3):
        #bottom
        return p1[1]>clipping[0][0]

def intersect(p1,p2,p3,p4,case):
    
    x= ( (p1[0]*p2[1]-p1[1]*p2[0])*(p3[0]-p4[0]) - (p1[0]-p2[0])*(p3[0]*p4[1]-p3[1]*p4[0]) ) / ((p1[0]-p2[0])*(p3[1]-p4[1]) - (p1[1] - p2[1])*(p3[0]-p4[0]))
    y= ( (p1[0]*p2[1]-p1[1]*p2[0])*(p3[1]-p4[1]) - (p1[1]-p2[1])*(p3[0]*p4[1]-p3[1]*p4[0]) ) / ((p1[0]-p2[0])*(p3[1]-p4[1]) - (p1[1] - p2[1])*(p3[0]-p4[0]))
    ans=[] # of points
    if(isin(p1,case) and isin(p2,case)):
       #print("case1")
       ans.append(p2)
    elif(isin(p1,case) and not isin(p2,case)):
        #print("case2")
        ans.append((x,y))
    elif(not isin(p1,case) and isin(p2,case)):
        #print("case3")
        ans.append((x,y))
        ans.append(p2)
    else:
        ans = -1
        #print(p1)
    return ans

answer = polygon
for i in range(0,4):
    answer_temp=[]
    for j in range(len(answer)):
         
         try:
             val = intersect(answer[j],answer[(j+1)%len(answer) ],clipping[i%4],clipping[(i+1) %4],i)
         except:
             val=(answer[j],answer[(j+1)%len(answer)])
         if(val != -1):
            for vali in val:
               answer_temp.append(vali)
    
    answer = list(set(answer_temp))

print(answer)
