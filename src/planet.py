import numpy as np
from random import randint


class Planet:

    def __init__(self, radius, mass, x, v, a=(0, 0), name=''):
        self.radius = radius
        self.mass = mass
        self.x, self.v, self.a = np.array(x), np.array(v), np.array(a)
        self.name = name

        self.g = 6.67*10**-11
        self.id = randint(1, 9999)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def get_F(self, planets):
        F = np.array([0, 0])
        for pln in planets:
            if pln != self:
                d = self.x - pln.x
                u = -d / np.linalg.norm(d)
                F = F + u * self.g * self.mass * pln.mass / (np.linalg.norm(d) ** 2)
        return F

    def step(self, dt, planets):
        self.v = self.v + dt * self.get_F(planets=planets) / self.mass / 1000
        self.x = self.x + dt * self.v
