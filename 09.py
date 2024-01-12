
n = 7

for x in range(7):
    serie = ""
    if(x >= 5):
        n += 2
    for c in range(n - x):
        serie += "*" 

    print(serie)