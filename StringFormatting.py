s=(int(input()))
b = "{0:b}".format(s)
d = "{0:d}".format(s)
x = "{0:X}".format(s)
o = "{0:o}".format(s)

width = len("{0:b}".format(s))
for i in range(1,s+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))





''' Syntax to convert a number to BINARY  =      "{0:b}".format(s) '''
''' Syntax to convert a number to OCTAL  =       "{0:o}".format(s) '''
''' Syntax to convert a number to HEXADECIMAL =  "{0:X}".format(s) '''
''' Syntax to convert a number to DECIMAL _=     "{0:d}".format(s) '''