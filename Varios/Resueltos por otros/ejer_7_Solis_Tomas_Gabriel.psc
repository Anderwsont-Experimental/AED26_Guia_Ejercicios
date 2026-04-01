Algoritmo ejer_7_Solis_Tomas_Gabriel
	Definir n1,n2,n3 Como Entero
	Escribir "Ingrese 3 numeros enteros:"
	Leer n1,n2,n3
	Borrar Pantalla
	Escribir "Los valores son:"
	Escribir "n1:",n1,"| n2: ",n2," | n3:",n3
	Escribir "----------"
	si (n1>n2) y n1>n3 Entonces
		si n2 > n3 Entonces
			Escribir "el orden de los numeros es: Mayor:",n1," Medio: ",n2," Menor: ",n3
		SiNo
			Escribir "el orden de los numeros es: Mayor:",n1," Medio: ",n3," Menor: ",n2
		FinSi
	FinSi
	si (n2>n1) y n2>n3 Entonces
		si n1 > n3 Entonces
			Escribir "el orden de los numeros es: Mayor:",n2," Medio: ",n1," Menor: ",n3
		SiNo
			Escribir "el orden de los numeros es: Mayor:",n2," Medio: ",n3," Menor: ",n1
		FinSi
	FinSi
	si (n3>n1) y n3>n2 Entonces
		si n1 > n2 Entonces
			Escribir "el orden de los numeros es: Mayor:",n3," Medio: ",n1," Menor: ",n2
		SiNo
			Escribir "el orden de los numeros es: Mayor:",n3," Medio: ",n2," Menor: ",n1
		FinSi
	FinSi
FinAlgoritmo
