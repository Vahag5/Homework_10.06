def swap_strings(str1, str2):
    str1, str2 = str2, str1
    return str1, str2


str1 = 'shun'
str2 = 'katu'
str1, str2 = swap_strings(str1, str2)  # kpoxi texerov
print(str1)   # ktpi katu
print(str2)   # ktpi shun  