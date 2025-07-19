import matplotlib.pyplot as plt
from functions import *
import random as rp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


class orbital():

    def __init__(self, m, l, n):
        self.m = m
        self.l = l
        self.n = n

        self.a_0 = 1

        self.bound = bound(self.n, self.l)

        self.points = []
        self.calcpoints()

        self.axis = np.linspace(-self.bound*a_0, self.bound*a_0, 75)

    def calcpoints(self):

        for x in self.axis:
            for y in self.axis:
                for z in self.axis:
                    if x > 0 and y > 0:
                        None
                    else:
                        P = PsiCart(x, y, z, self.m, self.l, self.n)
                        if P > rp.uniform(0, 1):
                            c = P * 50
                            self.points.append(np.array([x, y, z, c]))
        
        self.points = np.transpose(self.points)
    
    def plotImage(self):
        xp = self.points[0]
        yp = self.points[1]
        zp = self.points[2]
        cr = self.points[3]

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.scatter(xp, yp, zp, c=cr, cmap='viridis', alpha=1)
        ax.scatter(0, 0, 0, color="red")

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        ax.view_init(elev=10, azim=45, roll=0)
        plt.show()

    def plotInteractive(self):
        %matplotlib widget
        self.plotIm()
