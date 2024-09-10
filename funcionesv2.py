print("mas sobre funciones")
#aqui se escriben las funciones 
def sumas(a,b):
    men=a+b
    return men

def resta(a,b):
    pepe=a-b
    return pepe

def multi(a,b):
    u=a*b
    return u

def divicion(a,b):
    v=a/b
    return v
#llamadas a funciones
print("calculando suma")
n1=float(input("ingresa el primer numero"))
n2=float(input("ingresa el segundo numero"))
suma=sumas(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
print("calculando resta")
restas=resta(n1,n2)
print(f"la resta de {n1} - {n2} es {restas}")
print("calculando multiplicacion")
multip=multi(n1,n2)
print(f"la multiplicacion de {n1} * {n2} es {multip}")
print("calculando divicion")
divi=divicion(n1,n2)
print(f"la divicion de {n1} / {n2} es {divi}")


