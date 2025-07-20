from orbitalclass import orbital

test1 = orbital(1, 1, 2)

print(test1.points)
#print(test1.pointsDF)
test1.plotImageDissect()
#test1.plotAnimation(frames=50, interval=100)

'''
orbitlist = []

for n in range(5):
    for l in range(0, n):
        for m in range(-l, l+1):
            orbitlist.append(orbital(l, m, n))
            orbitlist[-1].plotImageDissect()
'''