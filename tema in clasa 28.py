a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def div_comuni(x,y,z):
    listx=[]
    listy=[]
    listz=[]
    for i in range (1,x+1):
        if (x%i==0):
            listx.append(i)
    for k in range (1,y+1):
        if (y%k==0):
            listy.append(k)
    for j in range (1,z+1):
        if (z%j==0):
            listz.append(j)
    comuni=set(listx).intersection(listy)
    comuni2=set(comuni).intersection(listz)
    afisare=list(comuni2)
    return afisare
print("divizorii comuni ai nr:",a,b,c," sunt  ",div_comuni(a,b,c))

def mult_comuni(x,y,z):
    listx=[]
    listy=[]
    listz=[]
    list=[]
    for i in range(1,1000):
        mx=x*i
        my=y*i
        mz=z*i
        listx.append(mx)
        listy.append(my)
        listz.append(mz)
    list.extend(listx)
    list.extend(listy)
    list.extend(listz)
    o=sorted(list)
    return o
w= mult_comuni(a,b,c)
import collections
print('Cei mai mici 3 multipli comuni sunt',[item for item, count in collections.Counter(w).items() if count > 2][:3])


def triunghi(x,y,z):
    if ( (x+y>z) and (x+z>y) and (z+y>x) ):
        t='poate fi format triunghiul din numerele date'
    else:
        t='nu poate  fi format triunghiul'
    return t
print(triunghi(a,b,c))

def aria(x,y,z):
    if ( (x+y>z) and (x+z>y) and (z+y>x) ):
        s=(x+y+z)/2 
        S=(s*(s-x)*(s-y)*(s-z))**0.5   
    else:
        S='nu poate fi format triunghiul'
    return S
print('g.1). Aria triughiului este de:',aria(a,b,c),'cm2')
def perimetru(x,y,z):
    if ( (x+y>z) and (x+z>y) and (z+y>x) ):
        p=x+y+z
    else:
        p='nu exista triunghiul'
    return p
print(' Perimetrul triughiului este :',perimetru(a,b,c),'cm')

def ecuatie(x,y,z):
    if x!=0:
        d=(y**2)-(4*x*z)
        if d>0:
            sol1=(-y-(d**0.5))/(2*x)
            sol2=(-y+(d**0.5))/(2*x)
        elif d==0:
            sol1=sol2=(-y)/(2*x)
        else:
            sol1=sol2='Ecuatia nu are solutii'
    else:
        sol1=sol2='Ecuatia  nu are solutii'

    return sol1,sol2
print(' Ecuatia',a,'x2 +',b,'x +',c,'are solutiile reale ',ecuatie(a,b,c))
