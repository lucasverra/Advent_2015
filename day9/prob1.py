import re
import itertools
datas = open("intru.txt", "r")
locations= []
matrix_dis=[]
merged=[]
distance = 0

for line in datas:
    line=line.rstrip()
    locations.append(re.findall(r'[a-zA-z]{3,}',line)) 



# get the list of destinations
merged = list(itertools.chain(*locations))
uni_dest = sorted(list(set(merged)))
# end get the list of destinations

#some testing
print uni_dest
#some testing


def get_dis(d1,d2) :
    datas = open("intru.txt", "r")
    # d1='Arbre'
    # d2='Tambi'
    for line in datas:
        line=line.rstrip()
        if (d1 in line) and (d2 in line):
            distance = re.findall(r'[0-9]+',line)
            distance = int(distance[0])
            return distance


# distance = get_dis()
# print distance

#lets build that matrix

matrix_dis = []
dim = []
for i in xrange(len(uni_dest)):
	dim = []
	for j in xrange(len(uni_dest)):
		dim.append(0)
	matrix_dis.append(dim)

for i in xrange(len(uni_dest)):
    for j in xrange(len(uni_dest)):
        d1=uni_dest[i]
        d2=uni_dest[j]
        if i==j :
            matrix_dis[i][j]=0
        else:
            matrix_dis[i][j]=get_dis(d1,d2)



    

print matrix_dis

print list(itertools.permutations(uni_dest,3))


