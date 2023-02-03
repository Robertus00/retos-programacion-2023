""" 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

import math

num=int(input("Numero (entero y mayor que cero)? "))

if num%2==0:
    checkpar="es par"
else:
    checkpar="es impar"

if num==2:
	checkprimo="es primo"
elif checkpar=="es par":
	checkprimo="no es primo"
else:
	checkprimo="es primo"
	i=num-1
	while i>=2:
		if num%i==0:
			checkprimo="no es primo"
			break
		else:
			i=i-1

if math.sqrt(5*num*num+4)%1==0 or math.sqrt(5*num*num-4)%1==0:
    checkfibo="es Fibonacci"
else:
    checkfibo="no es Fibonacci"

print("%s %s, %s y %s" %(num, checkprimo, checkfibo, checkpar))
