import numpy as np
import matplotlib.pyplot as plot

plot.plot(*np.loadtxt("dino.dat",unpack=True), linewidth=2.0)
plot.show()
