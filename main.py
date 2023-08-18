from src.simulator import Simulator
from src.planet import Planet
import matplotlib.pyplot as plt
import numpy as np

simu = Simulator(dt=100)
simu.add(Planet(name='Soleil', radius=696340*10**3, mass=1.989*10**30, x=(0, 0), v=(0, 0)))
simu.add(Planet(name='Terre', radius=6371*10**3, mass=5.972*10**24, x=(149597870.7, 0), v=(0, 30000)))

prev_ang = 0
while simu.running:
    simu.step()
    if simu.iteration == 10**6:
        simu.stop()


plt.plot(simu.positions['Soleil'][:, 0], simu.positions['Soleil'][:, 1], 'or')
plt.plot(simu.positions['Terre'][:, 0], simu.positions['Terre'][:, 1], '-b')
plt.axis('equal')
plt.show()
