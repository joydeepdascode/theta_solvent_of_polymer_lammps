#1.TWO BEADS

"""
Here, n beads for one chain can be located, but no bonds defined b/w them.
"""
from numpy import array,zeros,linspace
from sys import exit

##LAMMPS DATA FILE ##

#Open data file

f=open('data2.twobeads','w')


#Writing in data file begins

f.write('LAMMPS DATA FILE FOR 1.TWO BEADS\n\n')

n=10
tchain=20                                       #Total number of chains
ychain_end=4
zchain_end=tchain/ychain_end
b=int(tchain*(n/tchain)-tchain)
atom_perchain=n/tchain


b=n-1
######### SECTION A ##########
"""
n=int(input('Enter number of atoms '))
if(n==0):
    print("Number of atoms can't be zero")
    exit()
"""
f.write('\n')
f.write(str(int(n)))
f.write(' atoms\n')


"""
b=int(input('Enter number of bonds '))
"""
f.write(str(int(b)))
f.write(' bonds\n')

ang=int(input('Enter number of angles '))
if(ang!=0):
    f.write(str(ang))        
    f.write(' angles\n')
#####################################    
f.write('\n')
#####################################

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

print("Enter mass of atom type 1")
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
x=zeros(n)
y=zeros(n)
z=zeros(n)


if(n!=1):
    d=(xhi-xlo-10.0)/float((n-1))
else:
    exit()

    
diff=linspace(0,(n-1)*d,n)

x=xlo+5+diff
y=ylo+5+y
z=zlo+5+z

f.write('Atoms\n\n')
for i in range(1,n+1):
    f.write(str(i))
    f.write('\t1\t1\t')
    f.write(str(x[i-1]))
    f.write('\t')
    f.write(str(y[i-1]))
    f.write('\t')
    f.write(str(z[i-1]))
    f.write('\n')
    



#################################
f.write('\n')
#################################

######## BONDS

f.write('Bonds\n\n')

for i in range(1,b+1):
    f.write(str(i))
    f.write('')
f.close()    