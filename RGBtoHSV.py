import sys

#DIRECTIONS:
#Replace YOUR_CSV_FILE with the path of your CSV file from your output directory after running Color.ijm code.
#Example: fileName="C:\\Users\\..."
##################
fileName=YOUR_CSV_FILE
##################

f=open(fileName,'r')
text=f.read()

#Replace NUM_LEAVES with the number of leaves on your grid of leaves.

####################
numLeaves=NUM_LEAVES;
####################

def makeList(a):
    a=a.split("\n")
    temp=[]
    for i in range(len(a)):
        b=a[i]
        b=b.split(",")
        temp.append(b)
    a=temp
    return a

listNums=makeList(text)

        
def convertToHSV(i,a,b,c):
    R=float(a)
    G=float(b)
    B=float(c)
    var_R=R/255.0
    var_G=G/255.0
    var_B=B/255.0
    if (var_R>var_B) and (var_R>var_G):
        if(var_B<var_G):
            Cmin=var_B
        else:
            Cmin=var_G
        H=60*(((var_G-var_B)/(var_R-Cmin))%6)
        if var_R==0:
            S=0
        else:
            S=(var_R-Cmin)/var_R
        V=var_R
    elif (var_B>var_R) and (var_B>var_G):
        if(var_R<var_G):
            Cmin=var_R
        else:
            Cmin=var_G
        H=60*((var_R-var_G)/(var_B-Cmin)+4)
        if var_B==0:
            S=0
        else:
            S=(var_B-Cmin)/var_B
        V=var_B
    else:
        if(var_B<var_R):
            Cmin=var_B
        else:
            Cmin=var_R
        H=60*((var_B-var_R)/(var_G-Cmin)+2)
        if var_G==0:
            S=0
        else:
            S=(var_G-Cmin)/var_G
        V=var_G
    HList.append(H);
    SList.append(S);
    VList.append(V); 
    ##print str(L)
    ##print str(a)
    ##print str(b)
    print "\n"

HList=[]
SList=[]
VList=[]

for i in range(1,numLeaves+1):
    index=i
    blueindex=i+numLeaves
    greenindex=i+numLeaves*2
    area=0
    r=0
    g=0
    b=0
    intDen=0
    innerListWithInfo=listNums[index]
    blueList=listNums[blueindex]
    greenList=listNums[greenindex]
    if innerListWithInfo[0]!= ' ':
        area=innerListWithInfo[1]
        r=innerListWithInfo[2]
        intDen=innerListWithInfo[3]
        g=blueList[2]
        b=greenList[2]
        convertToHSV(index,r,g,b)

print "H Values";
for hVal in HList:
    print hVal;

print "\n";

print "S Values";
for sVal in SList:
    print sVal;

print "\n";

print "V Values";
for vVal in VList:
    print vVal;

##Formula for RGB=>HSV from: http://www.rapidtables.com/convert/color/rgb-to-hsv.htm
    

