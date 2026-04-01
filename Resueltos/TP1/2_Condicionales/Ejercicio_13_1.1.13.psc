Algoritmo billetes
	Definir dinero,a Como Entero
	Escribir "Ingrese un monto de dinero para saber cuantos billetes necesita:"
	leer dinero
	Escribir "Billetes de $1: ", dinero mod 10
	dinero <- trunc (dinero/10)
	Escribir "Billetes de $10: ",dinero mod 10
	a<-trunc (dinero/10)
	Escribir "Billetes de $100: ", a
FinAlgoritmo
