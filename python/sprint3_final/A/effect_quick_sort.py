alla = [4, 10, 'alla']
gena = [4, 100, 'gena']

result = []
if alla[0] > gena[0]:
    result.append(alla[2])
if alla[0] == gena[0]:
    if alla[1] < gena[1]:
        result.append(alla[2])
    if alla[1] == gena[1]:
        if alla[2] < gena[2]:
            result.append(alla[2])
        else:
            result.append(gena[2])
    else:
        result.append(gena[2])
else:
    result.append(gena[2])

if len(result) > 0:
    print(result[0])
else:
    print(result)
