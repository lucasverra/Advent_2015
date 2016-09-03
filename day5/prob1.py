import re;
handler = open('texttoread.txt', 'r')
nice_list=[];


for line in handler:

    line = line.rstrip();
    pepe = []
    pepe.append(re.findall('([a-z])\1', line))

    if  len(pepe)>0 : # re.findall('[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]', line) and 
        description = "nice"
        print line
        
    if bool(re.findall('[x][y]|[c][d]|[p][q]|[a][b]', line)):
        desc = "naughty"
        
        
    # if desc == "nice":
    #     print line
    #     nice_list.append(line)
        

