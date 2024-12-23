
print(f"suma 13 + 3 = {10+3}") #suma aritmetica

#defino variable numericas
N1=8 
N2=2
print(f"{N1 - N2}") # resta de variables
print(f"{N1 * N2}") # operador multiplicar
print(f"{N1 / N2}") # operador divicion
print(f"{N1 % N2}") # operador modulo. resto de una divicion entera
print(f"{N1 ** N2}") # operador exponente 
print(f"{N1 // N2}") # operador divicion con numero entero

#operadores de comparacion 
print(f"igualdad: 10 == 2? {10==2}")
print(f"desigualdad 10 != 2 ? {10!=2}")
print(f"mayor que: 10 > 2? {10>2}")
print(f"menor que: 1 < 2?{1<2}")
print(f"menor e igual: 2 <= 3{2<=3}")
print(f"mayor e igual: 2>=3 {2>=3}")

#operadores logicos
print(f"and: 10+2 == 12 and 10-1 == 9{10 + 2 == 12 and 10 - 1 == 9}") # and si ambos cumplen es verdadero
print(f"or: 10+ 2 == 12 or 10 - 1 == 2{10 + 2 == 12 or 10 - 1 == 2}") # or solo unos basta para que sea verdadero
print(f"not: 10+1 ==2 {not 10+1==2}")

#operadores de asignacion

patos_en_la_laguna= 12 #asignacion
print(f"numero de patos en la laguna: {patos_en_la_laguna}")

patos_en_la_laguna += 1 #suma y asignacion 
print(f"12 patos + 1 = {patos_en_la_laguna}")

patos_en_la_laguna -= 2 #resta y asignacion
print(f"12 patos - 2 = {patos_en_la_laguna}")


patos_en_la_laguna *= 2 #multilicacion y asignacion
print(f"12 patos * 2 = {patos_en_la_laguna}")

patos_en_la_laguna /= 2 #divicion y asignacion
print(f"12 patos / 2 = {patos_en_la_laguna}")

patos_en_la_laguna %= 2 #modulo y asignacion
print(f"12 patos %/ 2 = {patos_en_la_laguna}")

patos_en_la_laguna //= 2 #divicion entera y asignacion
print(f"12 patos // 2 = {patos_en_la_laguna}")

#operadores de identidad
edad_de_Juan = 10
print(f"edad_de_juan is  12 es:{edad_de_Juan is 12}.") # is es true si el valor es literalmente igual al de la variable
print(f"edad_de_juan is not  12 es:{edad_de_Juan is not 12}.")
      # is puede aplicar a cadenas de texto u oriebtada a objetos

#operadores de pertenencia
print(f" 'u' in 'uriel' ?: {'u'  in 'uriel' }")   
print(f" 'u' not in 'uriel' ?: {'u' not in 'uriel' }")     

#operadores de bit
"""
Integer numbers to binary numbers
AND (&)
OR (|)
XOR (^)
NOT (~)
MOVE TO RIGHT (>>)
MOVE TO LEFT (<<)
"""

a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {a & b}") # 0010 = 2
print(f"OR: 10 | 3 = {a | b}") # 1011 = 11
print(f"XOR: 10 ^ 3 = {a ^ b}") # 1001 = 9
print(f"NOT: {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010 = 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000 = 40

#condicionales

num_1 = 40
num_2 = 50
num_3 = num_1

if num_1 == num_3:
    print(f"El numero {num_1} es igual a {num_3}")
elif num_1 != num_2 and num_2 != num_3:
    print(f"el {num_1} es distinto de {num_2} y {num_2} es distinto de {num_3}")
else:
    print("ninguna de las afirmaciones anteriores son reales")

#iterativas
for i in range(11):
    print(i)

i = 1

while i <=10:
    print(i)
    i += 1


#manejo de exepciones

try:
    print(10/0)
except:
    print("se produjo un error")
finally: 
    print("ha finalizado el programa")

#extra
for numeros in range(10,56):
    if numeros % 2 == 0 and numeros != 16 and numeros % 3 != 0:
        print(numeros)
