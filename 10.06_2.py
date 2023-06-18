def end_with(str1, str2):
    s = len(str2)
    return str1[-s:] == str2   

print(end_with('vip', 'ip')) # True a tpelu
print(end_with('urax', 'pix')) # False a tpelu 
