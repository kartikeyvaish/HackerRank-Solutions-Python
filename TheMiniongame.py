from collections import defaultdict

def minion_game(s):
    '''
    Kevin=0
    Stuart=0
    n = len(string)
    k = 0
    c=0
    Scores = {}
    v="AEIOU"
    ch=""
    for i in range(0,len(string)):
        for j in range(0,len(string)):
            if (j+i)<len(string):
                ch=string[j:j+i+1]
                if ch not in Scores:
                    Scores[ch] = 1
                else:
                    Scores[ch] = Scores[ch] + 1
    print(Scores)
    for key in Scores:
        value = Scores[key]
        if v.find(key[0]) >= 0:
            Kevin = Kevin + value
        else:
            Stuart = Stuart + value

    if Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Stuart", Stuart)
        '''

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
s = input()
minion_game(s)

