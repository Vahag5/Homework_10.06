def convert_to_int(str1):
    if str1.isdigit():
        return int(str1)
    else:
        raise Exception('Hnaravor chi poxakerpel')

try:
    string2 = '123'
    print(convert_to_int(string2))
    string1 = '33gntewft'
    print(convert_to_int(string1))
except Exception as s:
    print('Exception occurred:', str(s))
