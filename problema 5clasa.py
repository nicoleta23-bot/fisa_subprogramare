lista=['Ion','Ivan','Nicolea','Andrei','Alexei','Sanea']
def cautare(n):
    for i in lista:
        i=input("NUmele elevului:")
        if i in lista:
            return print('Numele see contine in lista')
        else:
            return print('Numele nu se contine in lista')
            
cautare(lista)
