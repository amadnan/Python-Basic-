import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
def plot_vect(x, b, xlim, ylim):
    
    
    plt.figure(figsize = (10, 6))
    plt.quiver(0,0,x[0],x[1],color='k',angles='xy',scale_units='xy',scale=1,label='Original vector')
    plt.quiver(0,0,b[0],b[1],color='g',angles='xy',scale_units='xy',scale=1,label ='Transformed vector')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    
A = np.array([[2, 0],[0, 1]])

x = np.array([[1],[1]])
b = np.dot(A, x)
plot_vect(x,b,(0,3),(0,2))

x = np.array([[1], [0]])
b = np.dot(A, x)

plot_vect(x,b,(0,3),(-0.5,0.5))