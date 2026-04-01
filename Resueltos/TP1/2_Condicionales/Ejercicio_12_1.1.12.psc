Algoritmo componentes_mult_3
	//ambiente
	Definir num Como Entero
	//Proceso
	Escribir "ingrese un numero para descomponer"
	leer num
	si num >100 y num < 1000 Entonces
		si num mod 3 = 0 Entonces
			Escribir "el numero es divisible por 3"
		FinSi
		Escribir "Unidades:", num mod 10
		num <- trunc( num/10 )
		Escribir "decenas:", num mod 10
		Escribir "Centenas:", trunc(num/10)
	FinSi
FinAlgoritmo
