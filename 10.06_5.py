def find_last_not_of(str1, simvolner):
    d = 'chka ham@nknox'
    s = len(str1)
    for i in range(s - 1, - 1, -1):  # (star, stop(end) ,step)
        if str1[i] not in simvolner:
            return str1[i]
    return d


print (find_last_not_of('1sxndz3', '1!23r')) # True a tpelu  z
print (find_last_not_of('12345!', '12345!')) # True a tpelu  chka ham@nknox
