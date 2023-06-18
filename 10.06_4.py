def convert_to_int(string):
    str1 = ' '
    for x in string:
        str1 = str1 + str(ord(x))
    return str1


st = 'AAa'                              
print(convert_to_int(st))   # ktpri 656597   65-A, 65-A, a- 97    
