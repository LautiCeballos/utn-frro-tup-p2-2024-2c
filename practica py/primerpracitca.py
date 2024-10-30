"""1. Hola Mundo 
o Escribe un programa en Python que imprima en pantalla el mensaje 
"Hola Mundo". Luego modifica el mensaje para que diga "Bienvenidos a 
la programación en Python". 

print("Bienvenido a la programacion en python")

2. Salida por pantalla 
o Escribe un programa que muestre tu nombre, tu edad y tu ciudad en 
líneas separadas usando la función print. 


nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
print(nombre)
print(edad)
print(ciudad)


3. Lectura por teclado 
o Escribe un programa que solicite al usuario su nombre, edad y ciudad. 
Luego, muestra un mensaje de saludo personalizado utilizando esos 
datos. 


nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
print(f"Hola mi nombre es {nombre}, tengo {edad} anios y vivo en {ciudad}")

4. Tipo de datos 
o Crea un programa que le pida al usuario ingresar dos números enteros y 
un número flotante. Luego muestra la suma de los dos enteros y el 
producto del entero con el flotante. 
num1 = int(input("Ingrese 1er nro(ENTERO): "))
num2 = int(input("Ingrese 2do nro(ENTERO): "))
num3 = float(input("Ingrese 3er nro(FLOTANTE): "))
print(f"El resultado de {num1} + {num2} * {num3} = ")
print((num1+num2)*num3)

5. Tipo de operadores: Aritméticos 
o Diseña un programa que tome dos números enteros del usuario y 
muestre: 
▪ La suma. 
▪ La resta. 
▪ La multiplicación. 
▪ La división (ten en cuenta que uno puede ser 0, verifica esto antes 
de dividir). 
▪ El módulo (resto de la división). 


num1 = int(input("Ingrese primer nro "))
num2 = int(input("Ingrese segundo nro "))
print(f"SUMA: {num1+num2} ")
print()
print(f"RESTA: {num1-num2} ")
print()
print(f"PROD: {num1*num2} ")
print()
print(f"DIV: {num1/num2} ")

6. Variables 
o Escribe un programa en el que declares una variable para almacenar tu 
nombre, otra para tu edad y otra para la calificación de tu última prueba. 
Luego muestra un mensaje que diga: "Mi nombre es X, tengo X años y 
mi última calificación fue X." 
"""

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nota = input("Ingrese su ultima nota: ")
print(f"Hola mi nombre es {nombre}, tengo {edad} anios y mi ultima nota fue {nota}")
"""
Controladores de flujo 
1. Condicionales: sentencia if 
o Crea un programa que solicite la edad de una persona e indique si es 
mayor de edad (18 años o más) o no. 
o Variante: Modifica el programa para que además indique si es un 
adolescente (entre 13 y 17 años). 
2. Condicionales anidadas 
o Escribe un programa que le pida al usuario ingresar su nota en una 
prueba (un número entre 0 y 10). El programa debe mostrar: 
▪ "Insuficiente" si la nota es menor que 4. 
▪ "Regular" si la nota es mayor o igual a 4 pero menor que 6. 
▪ "Bueno" si la nota es mayor o igual a 6 pero menor que 8. 
▪ "Muy Bueno" si la nota es mayor o igual a 8 pero menor que 10. 
▪ "Excelente" si la nota es igual a 10. 
3. Estructuras iterativas: while 
o Escribe un programa que solicite al usuario un número entero positivo e 
imprima todos los números desde 1 hasta ese número. 
o Variante: Haz que el programa también sume todos los números 
impresos y muestre el total al final. 
4. Estructuras iterativas: for 
o Escribe un programa que imprima la tabla de multiplicar del número que 
el usuario elija. Usa la sentencia for. 
5. Iteración controlada con while y input 
o Crea un programa que solicite al usuario una contraseña (puedes definir 
una tú). El programa debe pedir la contraseña hasta que el usuario la 
escriba correctamente. 
6. Operadores lógicos y relacionales 
o Escribe un programa que le pida al usuario ingresar tres números enteros 
y muestre cuál es el mayor. Usa operadores lógicos para verificar si 
todos los números son diferentes o si algunos son iguales. 
7. Condicionales con operadores lógicos 
o Crea un programa que pida al usuario su edad y si tiene licencia de 
conducir (sí/no). El programa debe indicar si puede alquilar un coche, 
sabiendo que: 
▪ Debe tener al menos 21 años. 
▪ Debe tener una licencia de conducir válida. // """