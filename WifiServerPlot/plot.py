
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
csv_file = 'data.csv'

x_vals = []
y_vals = []


def animate(i):
    data = pd.read_csv(csv_file)
    x = data['timestamp']
    y1 = data['value']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
