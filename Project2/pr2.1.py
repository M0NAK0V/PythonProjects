def f(x):
    if(x[1] == 'sass'):
        return 9
    elif(x[1] == 'cson'):
        return 10
    elif(x[1] == 'java'):
        if(x[0] == 'org'):
            return 3
        elif(x[0]== 'smali'):
            if(x[3]=='abnf'):
                return 0
            elif(x[3]=='mql5'):
                return 1
            elif (x[3] == 'idl'):
                return 2
        elif (x[0] == 'golo'):
            if (x[3] == 'abnf'):
                return 4
            elif (x[3] == 'idl'):
                return 8
            elif (x[3] == 'mql5'):
                if(x[4] == 1991):
                    return 5
                elif (x[4] == 1975):
                    return 6
                elif (x[4] == 2011):
                    return 7

print(f(['smali', 'java', 'kicad', 'idl', 2011]))
print(f(['org', 'sass', 'dm', 'idl', 1991]))