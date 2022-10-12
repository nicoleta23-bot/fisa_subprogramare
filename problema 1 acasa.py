from random import choice
bile=['Albe', 'Negre']
n=int(input('Numarul de extragerea bilelor:'))
a=0
b=0
for i in range (n):
    x=choice(bile)
    print (x)
    if x=='Albe':
        a+=1
    elif x=='Negre':
        b+=1
print("Numarul de bile albe e:", a , "Numarul de bile negre e:", b)   