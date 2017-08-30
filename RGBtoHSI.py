import sys
import math

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
   
def convertToHSI(i,a,b,c):
    R=float(a)
    G=float(b)
    B=float(c)
    rn=R/(R+G+B)
    gn=G/(R+G+B)
    bn=B/(R+G+B)
    if(B>G):       
        h=math.acos((0.5 * ((rn - gn) + (rn - bn))) / (math.sqrt((rn - gn) * (rn - gn)+(rn-bn)*(gn-bn))))
        h=2*math.pi-h;
    else:
        h=math.acos((0.5 * ((rn - gn) + (rn - bn))) / (math.sqrt((rn - gn) * (rn - gn)+(rn-bn)*(gn-bn))))
    i=(R+G+B)/3
    s=1-3*min(rn,min(gn,bn));
    HList.append(h);
    SList.append(s);
    IList.append(i); 
    ##print str(L)
    ##print str(a)
    ##print str(b)
    print "\n"

HList=[]
SList=[]
IList=[]

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
        convertToHSI(index,r,g,b)

print "H Values";
for hVal in HList:
    print hVal;

print "\n";

print "S Values";
for sVal in SList:
    print sVal;

print "\n";

print "I Values";
for iVal in IList:
    print iVal;

##Formula for RGB=>HSV from: http://fourier.eng.hmc.edu/e161/lectures/ColorProcessing/node2.html
    

