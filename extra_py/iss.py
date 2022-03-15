from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

iss = np.asarray(Image.open('iss.tif'))

fig,ax = plt.subplots()
ax.imshow(iss,extent=[0,360,-90,90]) #Positive East Coordinates
plt.show()