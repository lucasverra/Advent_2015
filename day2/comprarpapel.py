# este ejercicio viene de la pagina http://adventofcode.com/ del dia 2

dimensiones = open('dimensiones.txt', 'r')
cantidadtotal = 0
ribbonapedir = 0

for line in dimensiones:
	line = line.rstrip()
	arrdim = line.split("x")
	wrapper = 2*int(arrdim[0])*int(arrdim[1]) + 2*int(arrdim[1])*int(arrdim[2]) + 2*int(arrdim[0])*int(arrdim[2])
	cantidadtotal = cantidadtotal + wrapper
	arrpapelito = [];
	arrpapelito.append(int(arrdim[0])*int(arrdim[1]))
	arrpapelito.append(int(arrdim[1])*int(arrdim[2]))
	arrpapelito.append(int(arrdim[0])*int(arrdim[2]))
	cantidadtotal = cantidadtotal + min(arrpapelito)
	

	
	

	perimetrospossibles=[]
	perimetrospossibles.append(2*int(arrdim[0])+2*int(arrdim[1]))
	perimetrospossibles.append(2*int(arrdim[1])+2*int(arrdim[2]))
	perimetrospossibles.append(2*int(arrdim[0])+2*int(arrdim[2]))

	minperim = min(perimetrospossibles)

	

	bow = int(arrdim[0])*int(arrdim[1])*int(arrdim[2])
	ribbonapedir = ribbonapedir + bow + minperim






print "la cantidad de papel a pedir es",cantidadtotal
print "la cantidad de ribbon a pedir es",ribbonapedir


