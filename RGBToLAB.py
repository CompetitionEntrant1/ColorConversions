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

        
def convertToLAB(i,a,b,c):
    R=float(a)
    G=float(b)
    B=float(c)
    var_R=R/255.0
    var_G=G/255.0
    var_B=B/255.0
    if var_R>0.0405:
        var_R=((var_R+0.055)/1.055)**2.4
    else:
        var_R=var_R/12.92
        
    if var_G>0.0405:
        var_G=((var_G+0.055)/1.055)**2.4
    else:
        var_G=var_G/12.92
        
    if var_B>0.0405:
        var_B=((var_B+0.055)/1.055)**2.4
    else:
        var_B=var_B/12.92
    var_R=var_R*100
    var_G=var_G*100
    var_B=var_B*100
    X=(0.412453*var_R)+(0.357580*var_G)+(0.180423*var_B)
    Y=(0.21267*var_R)+(0.715160*var_G)+(0.072169*var_B)
    Z=(0.019334*var_R)+(0.119193*var_G)+(0.950227*var_B)
    ref_X=95.047
    ref_Y=100
    ref_Z=108.883
    var_X=X/ref_X
    var_Y=Y/ref_Y
    var_Z=Z/ref_Z
    if var_Y>0.008856:
        var_Y=var_Y**(1.0/3)
    else:
        var_Y=(7.787*var_Y)+(16.0/116.0)
    L=(116.0*var_Y)-16.0
    if var_X>0.008856:
        var_X=var_X**(1.0/3)
    else:
        var_X=(7.787*var_X)+(16.0/116.0)        
    if var_Z>0.008856:
        var_Z=var_Z**(1.0/3)
    else:
        var_Z=(7.787*var_Z)+(16.0/116.0)
    a=500.0*(var_X-var_Y)
    b=200.0*(var_Y-var_Z)
    LList.append(L);
    AList.append(a);
    BList.append(b); 
    print "\n"

LList=[]
AList=[]
BList=[]

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
        convertToLAB(index,r,g,b)

print "L Values";
for lVal in LList:
    print lVal;

print "\n";

print "A Values";
for aVal in AList:
    print aVal;

print "\n";

print "B Values";
for bVal in BList:
    print bVal;

#The conversion from RGB to LAB are based on the mathematical formulas from this website: http://www.easyrgb.com/index.php?X=MATH



