from orbitalclass import orbital


orbitlist = []

for n in range(8):
    for l in range(0, n):
        for m in range(-l, l+1):
            orbitlist.append(orbital(n, l, m, id, 200))
            orbitlist[-1].plotImageDissect()
