#1.TWO BEADS

from numpy import array,zeros,linspace
from sys import exit

##LAMMPS DATA FILE ##

#Open data file

f=open('data.twobeads','w')


#Writing in data file begins

f.write('LAMMPS DATA FILE FOR 1.TWO BEADS\n\n')

######### SECTION A ##########
n=int(input('Enter number of atoms '))
if(n==0):
    print("Number of atoms can't be zero")
    exit()
f.write('\n')
f.write(str(int(n)))
f.write(' atoms\n')


b=int(input('Enter number of bonds '))
f.write(str(int(b)))
f.write(' bonds\n')

ang=int(input('Enter number of angles '))
if(ang!=0):
    f.write(str(ang))        
    f.write(' angles\n')
#####################################    
f.write('\n')
#####################################

########## SECTION B ##############
atype=int(input('Enter number of atom types '))
if(atype>n):
    print('Number of atom types cant exceed total number of atoms, type again')
    atype=int(input('Enter number of atom types '))
if(atype>n):
    exit()
f.write(str((atype)))
f.write(' atom types\n')

if(b!=0):
    btype=int(input('Enter number of bond types '))
    if(btype>b):
        print("Number of bond types can't exceed total number of bonds, type again")
        btype=int(input('Enter number of bond types '))
    if(btype>b):
        exit()
    f.write(str((btype)))
    f.write(' bond types\n')


if(ang!=0):
    angtype=int(input('Enter number of angle types '))
    if(angtype>ang):
        print("Number of angle types can't exceed total number of angles, type again")
    f.write(str(angtype))
    f.write(' angle types\n')

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


##### MASSES #####
print('\n')
f.write('Masses\n\n')


natype=zeros(atype)

for i in range(1,atype+1):
    print("Enter mass of atom type",i)
    m=float(input())
    if(m==0.0):
        print("Mass cant be zero, enter again")
        m=float(input())
    if(m==0.0):
        exit()
    print('Enter number of atoms of atom type',i)
    numa=int(input())
    if(numa==0):
        print("Mass cant be zero, enter again")
        numa=int(input())
    if(numa==0):
        exit()
    natype[i-1]=numa
    tempa=numa
    f.write(str(i))
    f.write('\t')
    f.write(str(m))
    f.write('\n')
    """
    for j in range(0,numa):
        #f.write(str(tempa+j))
        #f.write('\t')
        f.write(str(i))
        f.write('\t')
        f.write(str(m))
        f.write('\n')
    tempa=numa
    """

"""
for i in range(1,atype+1):
    print("Enter number of atoms type ",i)
    
for i in range(1,atype+1):
    print("Enter mass of atom type ",i)
    m=input()    

for i in range(1,n+1):
    f.write(str(i))
    f.write('\t')
    print('\n')
    print('Enter mass of',i,'atom ')
    m=input()
    f.write(str(m))
    f.write('\n')

"""
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


"""
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
"""
tempa=0
f.write('Atoms\n\n')
for i in range(0,atype):
    for j in range(1,int(natype[i])+1):
        f.write(str(int(j+tempa)))
        f.write('\t')
        f.write('1\t')
        f.write(str(int(i+1)))
        f.write('\t')
        f.write(str(x[i-1]))
        f.write('\t')
        f.write(str(y[i-1]))
        f.write('\t')
        f.write(str(z[i-1]))
        f.write('\n')
    tempa=tempa+int(natype[i])

f.close()

