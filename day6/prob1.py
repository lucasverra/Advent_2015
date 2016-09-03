import re;
handler = open('instru.txt', 'r')
contador=0
acciones = 0

# create the 1000*1000 matrix
light_park = []
dim = []
for i in xrange(1000):
	dim = []
	for j in xrange(1000):
		dim.append(0)
	light_park.append(dim)
# end create the 1000*1000 matrix

for line in handler:

	# get the coordinates of the points , double cheked & worked
	line = line.rstrip()
	datos = re.findall(r'([0-9]+,[0-9]+)',line)
	punto_ini = datos[0]
	coor_punto_ini = datos[0].split(",")
	coor_punto_ini = map(int, coor_punto_ini)
	punto_fin = datos[1]
	coor_punto_fin = datos[1].split(",")
	coor_punto_fin = map(int, coor_punto_fin)
	# end get the coordinates of the points 


# actions to be taken
	if re.findall(r'^turn on', line):
		acciones = acciones+1
		for i in xrange(coor_punto_ini[0],coor_punto_fin[0]+1):
			for j in xrange(coor_punto_ini[1],coor_punto_fin[1]+1):
				light_park[i][j] = 1
	if re.findall(r'^turn off', line):
		acciones = acciones+1
		for i in xrange(coor_punto_ini[0],coor_punto_fin[0]+1):
			for j in xrange(coor_punto_ini[1],coor_punto_fin[1]+1):
				light_park[i][j] = 0
	if re.findall(r'^toggle', line):
		# print "toggle"
		acciones = acciones+1
		for i in xrange(coor_punto_ini[0],coor_punto_fin[0]+1):
			for j in xrange(coor_punto_ini[1],coor_punto_fin[1]+1):
				if light_park[i][j] == 1:
					light_park[i][j] = 0
				elif light_park[i][j] == 0:
					light_park[i][j] = 1	
# end actions to be taken			

# Counting part
totalizador = 0
for i in xrange(1000):
	for j in xrange (1000):
		totalizador = totalizador + 1
		if light_park[i][j]==1:
			contador = contador + 1
print totalizador
print contador
print acciones
