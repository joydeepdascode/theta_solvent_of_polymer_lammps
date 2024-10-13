#1.TWO BEADS

"""
Succesfully created for 20 chains, with 20 atoms per atom
"""
from numpy import array,zeros,linspace
from sys import exit

##LAMMPS DATA FILE ##

#Open data file

f=open('data.polymer','w')


#Writing in data file begins

f.write('LAMMPS DATA FILE FOR POLYMER CHAINS\n\n')

n=400
tchain=20                                      #Total number of chains
zchain_end=5
ychain_end=int(tchain/zchain_end)
#ychain_end=4
#zchain_end=tchain/ychain_end

atoms_perchain=n/tchain


#b=n-1
######### SECTION A ##########

f.write('\n')
f.write(str(int(n)))
f.write(' atoms\n')



b=int(tchain*(atoms_perchain)-tchain)
f.write(str(int(b)))
f.write(' bonds\n')

ang=int(tchain*(atoms_perchain)-2*tchain)
f.write(str(ang))        
f.write(' angles\n')


#####################################    
f.write('\n')
#####################################

######### SECTION B ##########

f.write('1 atom types\n')
if(b!=0):
    f.write('1 bond types\n')
if(ang!=0):
    f.write('1 angle types\n')


##################################################
f.write('\n')
##################################################

########### SECTION C ################

xlo=float(input('Enter x low value '))
xhi=float(input('Enter x high value '))
ylo=float(input('Enter y low value '))
yhi=float(input('Enter y high value '))
zlo=float(input('Enter z low value '))
zhi=float(input('Enter z high value '))


## X-Axes
f.write(str(xlo))
f.write('\t')
f.write(str(xhi))
f.write('\txlo\txhi\n')

## Y-Axes
f.write(str(ylo))
f.write('\t')
f.write(str(yhi))
f.write('\tylo\tyhi\n')

## Z-Axes
f.write(str(zlo))
f.write('\t')
f.write(str(zhi))
f.write('\tzlo\tzhi\n')

##############################
f.write('\n\n')
##############################

####### SECTION D #########

f.write('Masses\n\n')

print("\n\nEnter mass of atom type 1")
m=float(input())
if(m==0.0):
    print("Mass cant be zero, enter again")
    m=float(input())
if(m==0.0):
    exit()
#f.write(str(i))
f.write('1\t')
f.write(str(m))
f.write('\n')

################################
f.write('\n')
################################

### Atoms


### Evaluate their positions

f.write('Atoms\n\n')

def g(i,j,zce,apc,xlo,ylo,zlo,dx,dy,dz):
    for k in range(1,int(apc)+1):
        aid=int((i-1)*zce*apc+(j-1)*apc+k)
        f.write(str(aid))
        f.write('\t1\t1\t')
        x=float(xlo+5+(k-1)*dx)
        f.write(str(x))
        f.write('\t')
        y=float(ylo+5+(i-1)*dy)
        f.write(str(y))
        f.write('\t')
        z=float(zlo+5+(j-1)*dz)
        f.write(str(z))
        f.write('\n')

sigma=1.0
dx=sigma+0.5
dy=4
dz=4
for i in range(1,int(ychain_end)+1):
    for j in range(1,int(zchain_end)+1):
        g(i,j,zchain_end,atoms_perchain,xlo,ylo,zlo,dx,dy,dz)
        


#################################
f.write('\n')
#################################

######## BONDS

f.write('Bonds\n\n')

def bo(i,j,zce,apc,xlo,ylo,zlo,dx,dy,dz):
    for k in range(1,int(apc)):
        bid=int((i-1)*zce*(apc-1)+(j-1)*(apc-1)+k)
        f.write(str(bid))
        f.write('\t1\t')
        aid=int((i-1)*zce*apc+(j-1)*apc+k)
        f.write(str(aid))
        f.write('\t')
        f.write(str(aid+1))
        f.write('\n')

for i in range(1,int(ychain_end)+1):
    for j in range(1,int(zchain_end)+1):
        bo(i,j,zchain_end,atoms_perchain,xlo,ylo,zlo,dx,dy,dz)
        


###################


#################################
f.write('\n')
#################################

####### Angles

f.write('Angles\n\n')

def ang(i,j,zce,apc,xlo,ylo,zlo,dx,dy,dz):
    for k in range(1,int(apc)-1):
        angid=int((i-1)*zce*(apc-2)+(j-1)*(apc-2)+k)
        f.write(str(angid))
        f.write('\t1\t')
        aid=int((i-1)*zce*apc+(j-1)*apc+k)
        f.write(str(aid))
        f.write('\t')
        f.write(str(aid+1))
        f.write('\t')
        f.write(str(aid+2))
        f.write('\n')

for i in range(1,int(ychain_end)+1):
    for j in range(1,int(zchain_end)+1):
        ang(i,j,zchain_end,atoms_perchain,xlo,ylo,zlo,dx,dy,dz)


f.close()    