import numpy as np
import matplotlib.pyplot as plt


def plot_complex(plt, c, text = '', xlim=[-3,3], ylim=[-3,3],
                 color='black', linestyle='-'):
    plt.grid()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.text(np.real(c), np.imag(c), text, size='16')

    plt.xlabel(r'$\mathrm{Re}$')
    plt.ylabel(r'$\mathrm{Im}$')
    plt.arrow(0.0, 0.0, np.real(c), np.imag(c),
              head_width=0.1, fc=color, ec=color,
              overhang=0.5, length_includes_head=True)

figsize = (6,6)
plt.figure(figsize=figsize)
c = 0.5 + 2j
d = 0.5 + 0.5*1j

plot_complex(plt, c, text='c', linestyle='|',color='blue')
plot_complex(plt, d, text='d', color='blue')
plot_complex(plt, c+d, text='c+d', color='red')
plot_complex(plt, c*d, text='c*d', color='orange')
plt.savefig('complex_plotting.png')


# Returns a list of complex numbers corresponding to hands positions.
# This is the function you need to write 
def clock_positions(nhands: int) -> list:
    hands = []
    for n in range(nhands):
        hands.append(np.exp(1j*2*np.pi*n/nhands))
    return hands


clist1 = clock_positions(12)

# Use a plot to check your solution
figsize = (4,4)
plt.figure(figsize=figsize)
for (n,c) in enumerate(clist1):
    plot_complex(plt, c, text=str(n), linestyle='|',color='green')
plt.savefig('clock_positions.png')
plot = plt.gca()


