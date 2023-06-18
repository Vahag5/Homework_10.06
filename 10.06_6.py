def rotate_by(arr, qanak):
    qanak = qanak % len(arr)           # vor ete qanak@ mec exav massivi erkarytyunic tarberutyan chapov frcni
    farr = arr[qanak:] + arr[:qanak]   #farr = frcrac arr
    return farr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
qanak= 10
print(rotate_by(arr, qanak))  
