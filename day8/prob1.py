import re
d1 = 0 
d2 = 0
cumul_raw = 0
cumul_view = 0

with open('instru.txt', 'r') as f:

    for line in f:
        line=line.rstrip()
        d2+=4

        cumul_raw+=len(line)
        print line

        for i in range(1,len(line)):
            print d2
            if line[i] == "\\" and not (i ==len(line)-2 ):
                if (line[i+1] == "\""):
                    d2+=2
                    print "add 2 cause of \""
                elif line[i+1] == '\\' and line[i+2] == '\\' and line[i+3] == '\\' : 
                	d2+=4
                	print "add 4 by crazy"
                elif line[i+1] == '\\' and (not line[i-1] == '\\'):
                    d2+=2
                    print "add 2 cause of \\"
                elif line[i+1] == "x":
                    if re.findall(r'[a-f0-9]{2}',line[i+2:i+4]):
                        d2+=1
                        print "add 1 cause of hex"
                


print "el total number nuevo es",6310+d2,"a eso le resto el raw anterior de 6310 me queda D2 =",d2
print  "el acumulado total inicial de char es",cumul_raw




# import re

# encoded = 0
# with open('instru.txt', 'r') as file:
#     data = file.read()
#     for line in data.splitlines():
#         encoded += len(re.escape(line)) + 2

#     characters = len(data.replace('\n',''))

# print encoded-characters