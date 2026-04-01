Algoritmo Ejercicio_7
	//Ambiente
	Definir a,b,c,x Como Entero
	//Proceso
	Escribir "Este programa ordena 3 enteros cualesquiera"
	Escribir "Ingrese los 3 numeros:"
	Leer a,b,c
	//compara a y b, y los intercambia para ordenarlos
	si a>b Entonces
		x<-a
		a<-b
		b<-x
	FinSi
	//compara a y c, y los intercambia para ordenarlos
	SI ( a>c ) ENTONCES
		x<-a
		a<-c
		c<-x
	FINSI
	//compara b y c, y los intercambia para ordenarlos
	SI ( b>c ) ENTONCES
		x:=b
		b:=c
		c:=x
	FINSI
	ESCRIBIR"Menor: ",a," Medio: ",b," Mayor: ",c
FinAlgoritmo
