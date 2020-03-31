def count_substring(string, sub_string):
    c=""
    counter1=0
    smlen = len(string)
    sblen = len(sub_string)
    for i in range(0,smlen):
        c=""
        if (string[i] == sub_string[0]) and (i+sblen<=smlen):
            for j in range(i,i+sblen):
                c = c + string[j]
            if c == sub_string:
                counter1 = counter1 + 1

    print(counter1)



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count_substring(string, sub_string)