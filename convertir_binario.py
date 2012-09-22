# -*- coding: utf-8 -*-
def decimal_binario(numero):
	numero_binario = ""
	while numero != 1	:
		numero_binario = str(numero%2) + numero_binario 
		numero = int(numero/2)
	numero_binario = str(numero) + numero_binario
	return numero_binario

def binario_decimal(numero):
	potencia = len(numero) - 1
	resultado = 0
	for n in numero:
		resultado = resultado + (int(n)*pow(2,potencia))
		potencia = int(potencia)-1
	return resultado


valor = raw_input("Ingrese número decimal a ser convertido a binario: ")
print "el número binario es: " + str(decimal_binario(int(valor)))

valor = raw_input("Ingrese número binario a ser convertido a decimal: ")
print "el número decimal es: " + str(binario_decimal(valor))