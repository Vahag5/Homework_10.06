def convert_to_int(str1):
    if str1.isdigit():
        return int(str1)
    else:
        raise Exception('Hnaravor chi')

string2 = "123"
print(convert_to_int(string2))


string1 = "gntt"
print(convert_to_int(string1))