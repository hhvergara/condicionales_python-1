print("ingrese el numero 1 ")
primer= int(input())
print("ingrese el numero 2 ")
segundo= int(input())
print("ahora ingrese alguno de estas operaciones:") 

operacion = str(input())    
if operacion == "+":
    print("la suma del primer numero y el segundo numero da:", primer + segundo)
elif operacion == "-":
    print("la resta del primer numero y el segundo numero da:", primer - segundo)
elif operacion == "*":    
    print("la multiplicacion del primer numero y el segundo numero da:", primer * segundo)
elif operacion == "/":
    print("la division del primer numero y el segundo numero da:", primer / segundo)
else: 
    operacion == "**"
    print("La exponenciancion del primer numero y el segundo numero da:", primer ** segundo)
