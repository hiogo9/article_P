

a = [[1, 2, 4], [2, 5], [0, 3, 7, 8], [12, 3, 6], [18, 14]]

result = []
for s in a:
    s = set(s)
    for t in result:
        if t & s:
            t.update(s)
            break
    else:
        result.append(s)

print(result)