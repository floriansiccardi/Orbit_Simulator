import numpy as np
from math import atan2


class Simulator:

    def __init__(self, dt=1, save=True):
        self.dt = dt
        self.save = save
        self.running = True
        self.iteration = 0

        self.positions = {}
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def get(self, name):
        for pln in self.planets:
            if name == pln.name:
                return pln

    def get_angle(self, name):
        pln = self.get(name)
        if not pln is None:
            return atan2(pln.x[1], pln.x[0])

    def step(self):
        for pln in self.planets:
            pln.step(dt=self.dt, planets=self.planets)
        if self.save:
            for pln in self.planets:
                if not self.positions.get(pln.name):
                    self.positions[pln.name] = [list(pln.x0)]
                self.positions[pln.name].append(list(pln.x))
        self.iteration += 1

    def stop(self):
        self.running = False
        for key in self.positions.keys():
            self.positions[key] = np.array(self.positions[key])

