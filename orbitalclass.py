import matplotlib.pyplot as plt
from functions import *
import random as rp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import os


class orbital():

    def __init__(self, n, l, m, id="test1", density=100):
        self.m = m
        self.l = l
        self.n = n

        self.a_0 = 1

        self.datafile = f"C:/Users/hzpet/Documents/Uni/kode/oribtalsillustrator/data/n{n}_l{l}_m{m}.txt"

        self.bound = bound(self.n, self.l)

        self.axis = np.linspace(-self.bound*a_0, self.bound*a_0, density)

        self.points = np.array([["X-coordinate", "Y-coordinate", "Z-coordinate", "Color"]])
        
        self.makepoints()
    
    def makepoints(self):
        if os.path.exists(self.datafile):
            data = pd.read_csv(self.datafile, sep=";", header=0)
            print(f"Existing data already found at {self.datafile}")
            data = data.to_numpy()
            self.points = np.append(self.points, data, axis=0)
            self.pointsDF = pd.DataFrame(self.points[1:], columns=self.points[0])
        else:
            self.calcpoints()
            self.pointsDF = pd.DataFrame(self.points[1:], columns=self.points[0])
            self.pointsDF.to_csv(self.datafile, sep=";", index=False)
            print(f"Printed data to {self.datafile}")

    def calcpoints(self):
        counter = 0
        length = len(self.axis)**3
        percent = 100 * counter / length
        bar = 5

        for x in self.axis:
            for y in self.axis:
                for z in self.axis:
                    self.PointGen(x, y, z)
                    counter += 1
                    percent = 100 * counter / length
                    if percent >= bar:
                        print(f"Progress (n={self.n}, l={self.l}, m={self.m}): {percent} %")
                        bar += 5

    def randPointDelete(self, n):
        global point
        def check():
            bar = rp.uniform(0, 1)
            point = np.random.choice(self.points[1:])
            if PsiCart(point[0], point[1], point[2], self.m, self.l, self.n) >= bar:
                np.delete(self.points, point)
                return True
            else:
                return False
        
        bol = False
        while bol == False:
            bol = check()
    
    def randPointGen(self):
        global x, y, z
        P = PsiCart(x, y, z, self.m, self.l, self.n)

        def check():
            x = np.random.choice(self.axis)
            y = np.random.choice(self.axis)
            z = np.random.choice(self.axis)
            if P > rp.uniform(0, 1):
                c = P * 50
                self.points = np.append(self.points, np.array([[x, y, z, c]]), axis=0)
                return True
            else:
                return False
        
        bol = False
        while bol == False:
            bol == check()
    
    def PointGen(self, x, y, z):
        P = PsiCart(x, y, z, self.m, self.l, self.n)
        if P > rp.uniform(0, 1):
            c = P * 50
            self.points = np.append(self.points, np.array([[x, y, z, c]]), axis=0)

    def plotImage(self, elev=0, azim=45, roll=0):
        xp = self.pointsDF["X-coordinate"].astype(float)
        yp = self.pointsDF["Y-coordinate"].astype(float)
        zp = self.pointsDF["Z-coordinate"].astype(float)
        cr = self.pointsDF["Color"].astype(float)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.scatter(xp, yp, zp, c=cr, cmap='viridis', alpha=1, edgecolors='black')
        ax.scatter(0, 0, 0, color="red", edgecolors='black')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        ax.set_title(f'Orbital: n={self.n}, l={self.l}, m={self.m}')
    
        ax.set_xlim([-self.bound*self.a_0, self.bound*self.a_0])
        ax.set_ylim([-self.bound*self.a_0, self.bound*self.a_0])
        ax.set_zlim([-self.bound*self.a_0, self.bound*self.a_0])

        ax.view_init(elev=elev, azim=azim, roll=roll)
        plt.show()
    
    def plotImageDissect(self, elev=0, azim=45, roll=0):
        pointsDissect = self.pointsDF[(self.pointsDF['X-coordinate'].astype(float) <= 0) | (self.pointsDF['Y-coordinate'].astype(float) <= 0)]

        xp = pointsDissect["X-coordinate"].astype(float)
        yp = pointsDissect["Y-coordinate"].astype(float)
        zp = pointsDissect["Z-coordinate"].astype(float)
        cr = pointsDissect["Color"].astype(float)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.scatter(xp, yp, zp, c=cr, cmap='viridis', alpha=1, edgecolors='black')
        ax.scatter(0, 0, 0, color="red", edgecolors='black')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        ax.set_title(f'Orbital: n={self.n}, l={self.l}, m={self.m}')
    
        ax.set_xlim([-self.bound*self.a_0, self.bound*self.a_0])
        ax.set_ylim([-self.bound*self.a_0, self.bound*self.a_0])
        ax.set_zlim([-self.bound*self.a_0, self.bound*self.a_0])

        ax.view_init(elev=elev, azim=azim, roll=roll)
        plt.show()

    
    def plotAnimation(self, interval=100):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        def update(frame):
            ax.clear()
            self.plotImage(elev=0, azim=frame, roll=0)
            return ax,

        ani_func = ani.FuncAnimation(fig, update, frames=np.arange(0, 360, 4), interval=interval)
        plt.show()

'''
    def plotInteractive(self):
        %matplotlib widget
        self.plotImage()
'''