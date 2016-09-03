import re
word = "3113322113"
letterlist = list(word)
print letterlist

for char in letterlist:
    for item in re.findall('%s+' % char, word):
        print len(item), item
    