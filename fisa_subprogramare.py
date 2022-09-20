a=int(input("a="))
b=int(input("b="))
def suma(x,y):
    s=x+y
    return s
print('a)',a,'+',b,'=',suma(a,b))

def prod(x,y):
    p=x*y
    return p
print('b)',a,'*',b,'=',prod(a,b))

def media(x,y):
    med=(x+y)/2
    return med
print('c) Media aritmetica a numerelor:',a,'si',b,'=',media(a,b))

def divizor(x,y):
    listax=[]
    listay=[]
    for i in range(1,x+1):
        if x%i==0 :
            listax.append(i)
    for k in range(1,y+1):
        if y%k==0 :
            listay.append(k)
    comun=set(listax).intersection(listay)      
    cel_mai_mare=max(comun)
    return cel_mai_mare
print('d) Cel mai mare divizor comun al nr:',a,'si',b,'=',divizor(a,b))

def multiplu(x,y):
    multiples=[]
    if(x>y):
        i=x
    if(y>x):
        i=y
    else:
        i=x
    multiple=0
    while len(multiples)<5:
        if(i%x==0 and i%y==0):
            multiples.append(i)
            i+=1
        else:
            i+=1  
    return min(multiples)
print('e) Cel mai mic multiplu comun al nr:',a,'si',b,'=',multiplu(a,b))

def minim(x,y):
    if x<y :
        minimul=x
    else:
        minimul=y    
    return minimul
print('f) Minimul dintre numerele:',a,'si',b,'=',minim(a,b))

def maxim(x,y):
    if x>y :
        maximul=x
    else:
        maximul=y    
    return maximul
print('g) Maximul dintre numerele:',a,'si',b,'=',maxim(a,b))

def suma2():
    x=int(input('Introduceti primul nr: '))  
    y=int(input('Introduceti al doilea nr: '))  
    print('h)',x,'+',y,'=', x+y)
suma2()

def produs2():
    x=int(input('Introduceti primul nr: '))  
    y=int(input('Introduceti al doilea nr: '))  
    print('i)',x,'*',y,'=', x*y)
produs2()

def div_comuni(x,y):
    listax=[]
    listay=[]
    for i in range (1,x+1):
        if (x%i==0):
            listax.append(i)
    for k in range (1,y+1):
        if (y%k==0):
            listay.append(k)
    comuni=set(listax).intersection(listay)
    afisare=list(comuni)
    return afisare
print("j) divizorii comuni ai nr:",a," si ",b," sunt: ",div_comuni(a,b))

def mult_comuni(x,y):
    multiples=[]
    if x>y:
        i=a
    elif y>x:
        i=b
    else:
        i=a
    while len(multiples)<5:
        if ((i%a==0)and(i%b==0)):
            multiples.append(i)
            i +=1
        else:
            i +=1
    return multiples
print("k) 5 multipli comuni ai nr:",a," si ",b," sunt: ",mult_comuni(a,b))

def cifre_comune(x,y):
    listax=[]
    listay=[]
    for i in str(x):
        listax.append(int(i))
    for k in str(y):
        listay.append(int(k))
    comuni=set(listax).intersection(listay)
    afisare=list(comuni)
    if len(afisare)!=0:
        return afisare
print("l) Cifrele comune care se contin in nr ",a," si ",b," sunt: ",cifre_comune(a,b))

def cifre_numai_in_primul(x,y):
    listax=[]
    listay=[]
    for i in str(x):
        listax.append(int(i))
    for k in str(y):
        listay.append(int(k))
    comuni=set(listax).difference(listay)
    afisare=list(comuni)
    return afisare
print("m) Cifrele care se contin numai in nr ",a," si nu se contin in numarul ",b," sunt: ",cifre_numai_in_primul(a,b))

def num_div(n):
    div=[]
    for i in range(1, n+1):
        if n%i==0:
            div.append(i)
    nr_de_div=len(div)
    return nr_de_div
if num_div(a)==num_div(b):
    print("n) prietene")
else:
    print("n) nu sunt prietene ")