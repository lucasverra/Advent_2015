import re
 # I needed to add into my program the concept of string incrementation, found it here http://ubuntuforums.org/showthread.php?t=1584242
class MyString(str):
    def __add__(self, x):
        # If we're trying to add anything but an int, do normal string
        # addition.
        if type(x) is not int:
            return str.__add__(self, x)

        res = ''
        i = len(self)-1
        while x > 0:
            # Get the ASCII code of the i-th letter and "normalize" it
            # so that a is 0, b is 1, etc.
            # If we are at the end of the string, make it -1, so that if we
            # need to "add" 1, we get a.
            if i >= 0:
                c = ord(self[i]) - 97
            else:
                c = -1

            # Calculate the number of positions by which the letter is to be
            # "rotated".
            pos = x % 26

            # Calculate x for the next letter, add a "carry" if needed.
            x //= 26
            if c + pos >= 26:
                x += 1

            # Do the "rotation".
            c = (c + pos) % 26

            # Add the letter at the beginning of the string.
            res = chr(c + 97) + res

            i -= 1

        # If we didn't reach the end of the string, add the rest of the string back.
        if i >= 0:
            res = self[:i+1] + res

        return MyString(res)


# define the 3 alphabeticaly consecutive letters to match in regex rule
s = "abcdefghjkmnpqrstuvxyz"
ls_ok_alphabet = []
[ls_ok_alphabet.append(i) for i in s]
# regexes = [s[i:i+3] for i in range(len(s)-2)]
regexes = ['abc', 'bcd', 'cde', 'def', 'efg', 'npq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvx', 'vxy', 'xyz']
combined = "(" + ")|(".join(regexes) + ")" #for later use un regex
# combined = " (abc)|(bcd)|(cde)|(def)|(efg)|(fgh)|(pqr)|(qrs)|(rst)|(stu)|(tuv)|(uvx)|(vxy)|(xyz) "
print regexes
print combined

# define the 3 alphabeticaly consecutive letters to match in regex rule

found_nw_pass = 0




def fn_checker(str_poss_pass):
    str_poss_pass = str_poss_pass
    if re.findall(r'[oil]',str_poss_pass):
        found_nw_pass = 0
        return found_nw_pass
    elif len(re.findall(r'([\w])\1',str_poss_pass))>1  and not re.match(r'([\w])\1\1\1',str_poss_pass) :
        if re.findall(combined, str_poss_pass):
            found_nw_pass = 1
            print str_poss_pass
            return found_nw_pass
    found_nw_pass = 0 
    return found_nw_pass







i=0     
s = MyString("hepxxyzz")
while found_nw_pass == 0 and len(s+i) < 9 :
    i += 1
    str_poss_pass = (s+i)
    print str_poss_pass;
    found_nw_pass = fn_checker(str_poss_pass)

# found_nw_pass = fn_checker("ghjaabcc")
# print found_nw_pass









