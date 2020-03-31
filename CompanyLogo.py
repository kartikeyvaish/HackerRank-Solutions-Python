import operator
Letters = {'a': 0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

s = input()
c=0
for i in range(0,len(s)):
    if s[i] in Letters:
        Letters[s[i]] = Letters[s[i]] + 1

'''SortedLetters = sorted(Letters.items(), key=operator.itemgetter(1))
SortedLetters.reverse()'''
SortedLetters = dict(sorted(Letters.items(), key=operator.itemgetter(1),reverse=True))
for r in SortedLetters:
    if Letters[r] > 0:
        c = c + 1
        print(r, Letters[r])

    if c==3:
        break